from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core import serializers
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Client
from product.models import Product
from order.models import Order, OrderItem
from .forms import ClientAddForm
import json


class ClientAddView(CreateView):
    model = Client
    template_name = 'client_add.html'
    form_class = ClientAddForm

    def get_success_url(self):
        return reverse('client:list')


class ClientView(ListView):
    model = Client
    paginate_by = 10
    template_name = 'clients_list.html'


class ClientEditView(UpdateView):
    model = Client
    template_name = 'client_edit.html'
    form_class = ClientAddForm

    def get_success_url(self):
        return reverse('client:list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client:list')


class ClientHistoryView(DetailView):
    model = Client
    template_name = 'client_history.html'
    context_object_name = 'client'

    def get_context_data(self, **kwargs):
        context = super(ClientHistoryView, self).get_context_data()
        context['order'] = Order.objects.filter(client_id=self.kwargs['pk'])
        return context


def client_order_item_ajax(request):
    data = json.loads(request.body)
    query = OrderItem.objects.filter(order_id=int(data['pk']))
    product = Product.objects.all()
    all_obj = [*query, *product]
    order_item = serializers.serialize('json', all_obj)
    return HttpResponse(order_item)




