from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('add_item/', views.CreateItemView.as_view(), name='add_item'),
    path('', views.ItemView.as_view(), name='list_items'),
    path('<int:pk>/detail/', views.ItemDetailView.as_view(), name='detail_item'),
    path('<int:pk>/delete/', views.delete_item, name='delete_item'),
    path('<int:pk>/activate/', views.activate_item, name='activate_item'),
    path('<int:pk>/deactivate/', views.deactivate_item, name='deactivate_item'),
    path('<int:pk>/edit/', views.UpdateItemView.as_view(), name='edit_item'),
]
