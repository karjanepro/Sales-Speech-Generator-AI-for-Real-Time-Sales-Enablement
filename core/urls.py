from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_category, name='select_category'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('generate/<str:category>/', views.generate_prompt, name='generate_prompt'),
]

