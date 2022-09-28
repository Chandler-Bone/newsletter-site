from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('registered/', views.registered, name='registered'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    # login panel
    path('dashboard/', views.dashboard, name='dashboard'),

    # login panel functions
    path('create_sub/', views.create_sub, name='create_sub'),
    path('edit_sub/<int:id>/', views.edit_sub, name='edit_sub'),
    path('delete_sub/<int:id>/', views.delete_sub, name='delete_sub'),
    path('delete_all_sub/', views.delete_all_sub, name='delete_all_sub'),
    path('send_newsletter/', views.send_newsletter, name='send_newsletter'),
]