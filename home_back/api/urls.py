from django.urls import path
from . import views

urlpatterns = [
    path('db/', views.DatabaseList.as_view()),
    path('login/', views.UserLogin.as_view()),
    path('user/', views.UserList.as_view()),
    path('admin/', views.AdminList.as_view()),
    path('logout/', views.UserLogout.as_view()),
]