from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name = 'login'),
    path('signup/', views.signup, name = 'register'),
    path('admin/', views.admin, name = 'admin'),
    path('addy/', views.addy, name = 'add'),
    path('update/', views.update, name = 'update'),
 

]