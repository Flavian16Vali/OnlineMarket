from django.urls import path
from conversation import views

app_name = 'conversation'

urlpatterns = [
    path('new_conversation/<int:item_pk>/', views.new_conversation, name='new_conversation')
]
