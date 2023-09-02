#from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('records/<int:pk>', views.record_details, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
]
