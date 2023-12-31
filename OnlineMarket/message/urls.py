from django.urls import path
from message import views

app_name = 'message'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new_conversation/<int:item_pk>/', views.new_conversation, name='new_conversation'),
]
