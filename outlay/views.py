from django.views.generic.edit import CreateView, DeleteView
from .models import Outlay, OutlayCategory
from paymentlog.models import PaymentLog
from django.urls import reverse_lazy
from datetime import datetime
from django.db.models import Sum
from datetime import date


class OutlayListView(CreateView):
    model = Outlay
    fields = ('category', 'name', 'summa')
    success_url = reverse_lazy('outlay:list')
    template_name = 'outlay.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        outlay_for_today = Outlay.objects.filter(created=datetime.today().strftime('%Y-%m-%d'))
        outlay_count = outlay_for_today.count()
        outlay_sum = outlay_for_today.aggregate(sum=Sum('summa'))['sum']
        context['outlay_count'] = outlay_count
        context['outlay_sum'] = outlay_sum
        context['outlay'] = Outlay.objects.all()
        context['day'] = datetime.now()
        cash = PaymentLog.objects.filter(created=date.today().today())
        cash_sum = cash.aggregate(sum=Sum('amount'))['sum']
        context['money_for_today'] = cash_sum
        return context

    def form_valid(self, form):

        return super().form_valid(form)


class OutlayCategoryCreateView(CreateView):
    model = OutlayCategory
    fields = ('name', )
    success_url = reverse_lazy('outlay:list')


class OutlayDeleteView(DeleteView):
    model = Outlay
    success_url = reverse_lazy('outlay:list')
