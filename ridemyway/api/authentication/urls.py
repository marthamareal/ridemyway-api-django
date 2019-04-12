from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserView.as_view(), name='create_and_list_users'),
    path('users/<pk>/', views.SingleUserView.as_view(), name='single_user'),
    path('user/login/', views.UserLoginView.as_view(), name='user_login'),
    path('user/activate/<str:token>/', views.ActivateUserView.as_view(), name='user_activate')

]
