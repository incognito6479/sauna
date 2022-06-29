from django.urls import path
from .views import OutlayListView, OutlayCategoryCreateView, OutlayDeleteView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('list/', login_required(OutlayListView.as_view()), name='list'),
    path('category-add/', login_required(OutlayCategoryCreateView.as_view()), name='category-add'),
    path('category-delete/<int:pk>', login_required(OutlayDeleteView.as_view()), name='category-delete'),
]
