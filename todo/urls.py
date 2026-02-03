from django.urls import path,include
from . import views
urlpatterns =[
    path('index/', views.index, name='index'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('del/<str:item_id>', views.remove, name='del'),
]