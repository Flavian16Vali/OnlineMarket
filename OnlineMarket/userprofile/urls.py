from django.urls import path

from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('create_new_account', views.CreateNewAccountView.as_view(), name='create_user'),
    path('user_account', views.AccountView.as_view(), name='user_account'),
    path('<int:pk>/edit_account/', views.UpdateUserView.as_view(), name='edit_account'),
    path('<str:pk>/delete_account/', views.delete_user, name='delete_account'),
]