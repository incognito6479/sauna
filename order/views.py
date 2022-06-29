from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import View
from django.shortcuts import redirect
from .models import Order, OrderItem, Penalty
from product.models import Product, ProductCategory
from sauna.helper import count_sauna_price
from sauna.models import Sauna
from paymentlog.forms import PaymentLogForm
from paymentlog.models import PaymentLog
from datetime import date


class OrderList(ListView):
    model = Order
    template_name = 'order_list.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['orders_today'] = Order.objects.filter(start_time__contains=date.today().today())
        context['sauna'] = Sauna.objects.all()
        return context


class OrderEachView(DetailView):
    model = Order
    template_name = 'order_view.html'

    def get_context_data(self, **kwargs):
        context = super(OrderEachView, self).get_context_data()
        context['product'] = Product.objects.all()
        context['payment_form'] = PaymentLogForm
        context['payment_log'] = PaymentLog.objects.filter(order_id=self.kwargs['pk'])
        context['product_category'] = ProductCategory.objects.all()
        context['order_item'] = OrderItem.objects.filter(order_id=self.kwargs['pk'])
        context['penalty'] = Penalty.objects.filter(order_id=self.kwargs['pk'])
        context['id'] = self.kwargs['pk']
        return context


class OrderPenaltyAdd(CreateView):
    model = Penalty
    fields = ['reason', 'sum']
    template_name = 'penalty_add.html'

    def get_success_url(self):
        return reverse_lazy('order:each', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super(OrderPenaltyAdd, self).get_context_data()
        context['id'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        form.instance.order = Order.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)


class OrderPenaltyDelete(DeleteView):
    model = Penalty

    def get_success_url(self):
        pk = self.request.POST.get('id')
        return reverse_lazy('order:each', kwargs={'pk': pk})


class OrderPaymentCreate(CreateView):
    model = PaymentLog
    fields = ('discount', 'payment_type', 'payment_method')

    def get_success_url(self):
        pk = self.request.POST.get('id')
        return reverse_lazy('order:each', kwargs={'pk': pk})

    def form_valid(self, form):
        order = Order.objects.get(id=int(self.request.POST.get('order_id')))
        form.instance.order = order
        form.instance.total = int(self.request.POST.get('total').replace(" ", ""))
        form.instance.amount = int(self.request.POST.get('amount').replace(" ", ""))
        form.instance.user = self.request.user
        if form.instance.payment_type == 'payment':
            form.instance.comment = 'Оплата за заказ: ' + str(order.id)
        else:
            form.instance.comment = 'Аванс за заказ: ' + str(order.id)
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse(form.errors)


class OrderPaymentDeleteView(DeleteView):
    model = PaymentLog

    def get_success_url(self):
        pk = self.request.POST.get('id')
        return reverse_lazy('order:each', kwargs={'pk': pk})


class OrderProductAddView(View):
    def post(self, request):
        id_ = request.POST.getlist('product_id')
        count = request.POST.getlist('count')
        price = request.POST.getlist('price')
        order_id = request.POST.get('order_id')
        for i in range(0, len(id_)):
            obj, created = OrderItem.objects.get_or_create(product_id=int(id_[int(i)]),
                                                           order_id=int(order_id),
                                                           count=int(count[int(i)]),
                                                           price=int(price[int(i)]),
                                                           total=int(count[int(i)]) * int(price[int(i)]),
                                                           )
            if not created:
                obj.count += int(count[int(i)])
                obj.total = obj.count * int(price[int(i)])
                obj.save()
        return redirect(request.META['HTTP_REFERER'])


class OrderItemDeleteView(DeleteView):
    model = OrderItem

    def get_success_url(self):
        pk = self.request.POST.get('id')
        return reverse_lazy('order:each', kwargs={'pk': pk})


class OrderCloseView(View):
    def get(self, request, pk):
        Order.objects.filter(id=int(pk)).update(status='inactive')
        return redirect('order:each', pk=pk)


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('sauna:calendar_view')


class OrderEditView(UpdateView):
    model = Order
    fields = ['client', 'sauna', 'people_count', 'hours', 'status']
    template_name = 'order_edit.html'

    def get_success_url(self):
        id_ = int(self.kwargs['pk'])
        return reverse_lazy('order:each', kwargs={'pk': id_})

    def get_context_data(self, **kwargs):
        context = super(OrderEditView, self).get_context_data()
        context['order'] = Order.objects.get(id=self.kwargs['pk'])
        context['id'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        action = 'edit'
        count_sauna_price(self, form, action)
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse(form.errors)
