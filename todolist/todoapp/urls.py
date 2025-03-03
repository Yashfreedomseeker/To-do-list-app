from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpg, name='login'),
    path('login/', views.logoutview, name='logout'),
    path('delete-task/<str:name>/', views.DeleteTasks, name='delete'),
    path('update-task/<str:name>/', views.UpdateTasks, name='update'),
]