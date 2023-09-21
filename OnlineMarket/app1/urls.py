from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('add_item/', views.CreateItemView.as_view(), name='add_item'),
    path('', views.ItemView.as_view(), name='list_items'),
]
