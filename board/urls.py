from django.urls import path , re_path
from board import views

urlpatterns = [
    path('shop',viewsone.index, name="shop"),
    path('productdetails',viewstwo.index,name="productdetails"),
    path('index', views.index,name="index"),
    path('checkout', viewsthree.index,name="checkout"),
    path('cart', viewsfour.index,name="cart")
]
