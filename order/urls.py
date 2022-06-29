from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import OrderEachView, OrderProductAddView, OrderItemDeleteView, OrderCloseView, OrderDeleteView, \
    OrderEditView, OrderPaymentCreate, OrderPaymentDeleteView, OrderList, OrderPenaltyAdd, OrderPenaltyDelete


urlpatterns = [
    path('each/<int:pk>', login_required(OrderEachView.as_view()), name='each'),
    path('list/', login_required(OrderList.as_view()), name='list'),
    path('penalty_delete/<int:pk>', login_required(OrderPenaltyDelete.as_view()), name='penalty-delete'),
    path('penalty_add/<int:pk>', login_required(OrderPenaltyAdd.as_view()), name='penalty-add'),
    path('product-add/', login_required(OrderProductAddView.as_view()), name='product-add'),
    path('product-delete/<int:pk>', login_required(OrderItemDeleteView.as_view()), name='product-delete'),
    path('close/<int:pk>', login_required(OrderCloseView.as_view()), name='close'),
    path('delete/<int:pk>', login_required(OrderDeleteView.as_view()), name='delete'),
    path('edit/<int:pk>', login_required(OrderEditView.as_view()), name='edit'),
    path('payment-create/', login_required(OrderPaymentCreate.as_view()), name='payment-create'),
    path('payment-delete/<int:pk>', login_required(OrderPaymentDeleteView.as_view()), name='payment-delete'),
]
