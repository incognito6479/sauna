from django.urls import path
from .views import ClientAddView, ClientView, ClientEditView, ClientDeleteView, ClientHistoryView, client_order_item_ajax
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(ClientView.as_view()), name='list'),
    path('add/', login_required(ClientAddView.as_view()), name='add'),
    path('edit/<int:pk>', login_required(ClientEditView.as_view()), name='edit'),
    path('delete/<int:pk>', login_required(ClientDeleteView.as_view()), name='delete'),
    path('history/<int:pk>', login_required(ClientHistoryView.as_view()), name='history'),
    path('order-item/', login_required(client_order_item_ajax), name='order_item'),
]
