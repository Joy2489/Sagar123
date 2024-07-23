from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('contact', views.contact),
    path('display', views.display, name="display"),
    path('delete/<int:id>',views.deleterecord),
    path('edit/<int:id>', views.updateform),
    path('Signupuser', views.signupuser),
    path('login', views.loginuser, name="login"),
    path('logout', views.logoutuser),
    path('subcategory/<int:id>',views.subcategory),
    path('product/<int:id>', views.products),
    path('description/<int:id>', views.productdetails),
    path('addtocart', views.addtocart),
    path('cart', views.displaycart, name="cart"),
    path('deletecart/<int:id>', views.deletecart),
    path('updatecart/<int:id>',views.updatecart),
    path('checkout',views.checkoutPage),
    path('stateList',views.stateList),
    path('cityList',views.cityList),
    path('complete-payment', views.complete_payment, name="complete-payment")
]