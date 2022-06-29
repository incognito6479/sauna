from django.urls import path
from .views import CalendarView, LoginView, LogoutView, OrderAddView, get_sauna_type_ajax, ChangePassword
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', login_required(LogoutView.as_view()), name='logout'),
    path('pass_change/<int:pk>', login_required(ChangePassword.as_view()), name='password_change'),
    path('sauna/', login_required(CalendarView.as_view()), name='calendar_view'),
    path('order/add/', login_required(OrderAddView.as_view()), name='order-add'),
    path('sauna_type_ajax/', login_required(get_sauna_type_ajax), name='get_sauna_type_ajax'),
]
