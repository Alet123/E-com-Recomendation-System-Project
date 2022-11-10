"""shopping URL Configuration

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
from django.urls import path
from shoppingapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login',views.login),
    path('registration',views.registration),

    path('adminhome',views.adminhome),
    path('admincategory',views.admincategory),
    path('updatecategory',views.updatecategory),
    path('deletecategory',views.deletecategory),
    path('adminsubcategory',views.adminsubcategory),
    path('updatesubcategory',views.updatesubcategory),
    path('deletesubcategory',views.deletesubcategory),
    path('adminbrand',views.adminbrand),
    path('updatebrand',views.updatebrand),
    path('deletebrand',views.deletebrand),
    path('adminproduct',views.adminproduct),
    path('deleteproduct',views.deleteproduct),
    path('getsub',views.getsub),
    path('adminorders',views.adminorders),

    path('customerhome',views.customerhome),
    path('customerviewproduct',views.customerviewproduct),
    path('customercart',views.customercart),
    path('customerreview',views.customerreview),
    path('payment',views.payment),
    path('customerorders',views.customerorders),
    path('customerallproducts',views.customerallproducts),
]
