from order.models import Order
from client.models import Client
from client.forms import ClientAddForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .forms import OrderAddForm
from .helper import count_sauna_price
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from sauna.models import Sauna, SaunaPriceTypes
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User
import json


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('sauna:calendar_view')
        return render(request, 'signin.html')

    def post(self, request):
        user = authenticate(username=str(request.POST.get('login')), password=str(request.POST.get('password')))
        if user is not None:
            login(request, user)
            return redirect('sauna:calendar_view')
        return render(request, 'signin.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('sauna:login')


class CalendarView(ListView):
    model = Order
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderAddForm
        context['order'] = Order.objects.all()
        context['clients'] = Client.objects.all()
        context['client_form'] = ClientAddForm
        context['sauna'] = Sauna.objects.all()
        return context


class OrderAddView(CreateView):
    model = Order
    fields = ['hours']
    success_url = reverse_lazy('sauna:calendar_view')

    def form_valid(self, form):
        action = 'add'
        count_sauna_price(self, form, action)
        return super().form_valid(form)


def get_sauna_type_ajax(request):
    data = json.loads(request.body)
    queryset = SaunaPriceTypes.objects.filter(sauna_id=int(data['sauna_id']))
    context = serializers.serialize('json', queryset)
    return HttpResponse(context)


class ChangePassword(UpdateView):
    model = User
    fields = ['username', 'first_name', 'password']
    template_name = 'change_password.html'
    success_url = reverse_lazy('sauna:calendar_view')

    def form_valid(self, form):
        if self.request.POST.get('use_current_password'):
            form.instance.username = str(self.request.POST.get('username'))
            form.instamce.first_name = str(self.request.POST.get('first_name'))
            current_password = User.objects.get(id=int(self.kwargs['pk']))
            form.instance.password = current_password
        return form

    def form_invalid(self, form):
        print('lala')
        return HttpResponse(form.errors)
