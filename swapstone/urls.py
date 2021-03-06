"""swapstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from capstone import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('load_csv/', views.csv, name='csv'),
    path('', views.home, name='home'),  
    path('<int:index>/', views.home, name='home_withIndex'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/create_account', views.create_account, name='create_account'),
    path('accounts/reset_password', views.reset_password, name='reset_password'),
    path('accounts/change_password', views.change_password, name='change_password'),
    path('accounts/change_allocation', views.change_allocation, name='change_allocation'),
]
