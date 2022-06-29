from django.shortcuts import render
from outlay.models import Outlay
from django.core.paginator import Paginator
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import PaymentLog
from django.db.models import Sum
from datetime import date, datetime
from .filters import PaymentLogFilters


# class PaymentLogView(ListView):
#     model = PaymentLog
#     template_name = 'paymentlog.html'
#     paginate_by = 10
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         qs = PaymentLogFilters(self.request.POST, queryset=qs)
#         return qs
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         cash = PaymentLog.objects.filter(payment_method='cash', created=datetime.today().strftime('%Y-%m-%d'))
#         cashless = PaymentLog.objects.filter(payment_method='cashless', created=datetime.today().strftime('%Y-%m-%d'))
#         cashless_count = cashless.count()
#         cashless_sum = cashless.aggregate(sum=Sum('amount'))['sum']
#         cash_count = cash.count()
#         cash_sum = cash.aggregate(sum=Sum('amount'))['sum']
#         context['cash_count'] = cash_count
#         context['cash_sum'] = cash_sum
#         context['cashless_count'] = cashless_count
#         context['cashless_sum'] = cashless_sum
#         context['today'] = datetime.today
#         context['filter'] = PaymentLogFilters
#         if cash_sum is None:
#             cash_sum = 0
#         if cashless_sum is None:
#             cashless_sum = 0
#         context['total_sum'] = int(cash_sum) + int(cashless_sum)
#         return context


def payment_log_view(request):
    today = date.today()
    cash = PaymentLog.objects.filter(payment_method='cash', created=today.today())
    cashless = PaymentLog.objects.filter(payment_method='cashless', created=today.today())
    outlay_for_today = Outlay.objects.filter(created=datetime.today().strftime('%Y-%m-%d'))
    outlay_sum = outlay_for_today.aggregate(sum=Sum('summa'))['sum']
    cashless_count_ = cashless.count()
    cashless_sum_ = cashless.aggregate(sum=Sum('amount'))['sum']
    cash_count_ = cash.count()
    cash_sum_ = cash.aggregate(sum=Sum('amount'))['sum']
    cash_count = cash_count_
    cash_sum = cash_sum_
    cashless_count = cashless_count_
    cashless_sum = cashless_sum_
    today = datetime.today
    if cash_sum_ is None:
        cash_sum_ = 0
    if cashless_sum_ is None:
        cashless_sum_ = 0
    total_sum = int(cash_sum_) + int(cashless_sum_)
    filters = PaymentLogFilters(request.POST, queryset=PaymentLog.objects.all())
    paginator = Paginator(filters.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'cash_count': cash_count,
        'cash_sum': cash_sum,
        'cashless_count': cashless_count,
        'cashless_sum': cashless_sum,
        'total_sum': total_sum,
        'today': today,
        'filters': filters,
        'outlay_sum': outlay_sum,
    }
    return render(request, 'paymentlog.html', context)


class PaymentLogDeleteView(DeleteView):
    model = PaymentLog
    success_url = reverse_lazy('payment_log:list')

