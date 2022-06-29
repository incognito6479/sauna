import django_filters
from .models import PaymentLog
from .choices import PAYMENT_TYPE, PAYMENT_METHOD


class PaymentLogFilters(django_filters.FilterSet):
    # created = django_filters.CharFilter(label='Дата создания')
    # payment_type = django_filters.ChoiceFilter(label='Тип оплаты', choices=PAYMENT_TYPE)
    # payment_method = django_filters.CharFilter(label='Метод оплаты', choices=PAYMENT_METHOD)

    class Meta:
        model = PaymentLog
        fields = ['created', 'payment_type', 'payment_method']
