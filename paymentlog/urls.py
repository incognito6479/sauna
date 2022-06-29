from django.urls import path
from .views import PaymentLogDeleteView, payment_log_view
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('list/', login_required(payment_log_view), name='list'),
    path('delete/<int:pk>', login_required(PaymentLogDeleteView.as_view()), name='delete'),
]
