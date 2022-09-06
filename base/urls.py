from django.urls import path
from . import views
from .views import AboutView,ShopView,HandleLoginView,HandleRegisterView, ContactFormView
urlpatterns = [
    #path('',views.index, name="index"),
    #path('About',views.about, name="about"),
    #path('Glasses',views.glasses, name="glasses"),
    #path('Shop',views.shop, name="shop"),

    #get data from template and pass in forms.py file using function base view
    #path('Contact_Us',views.contact, name="contact"),

    #path('Login',views.handlelogin, name="login"),
    #path('Register', views.handleregister, name="register"),
    #path('Logout', views.handlelogout, name="logout"),
    #class base path
    path('about', AboutView.as_view(), name="about"),
    path('shop', ShopView.as_view(), name="shop"),
    path('', views.IndexView.as_view(), name="index"),
    path('Glasses',views.GlassesView.as_view(), name="glasses"),
    path('Login',HandleLoginView.as_view(), name="login"),
    path('Logout', views.HandleLogoutView.as_view(), name="logout"),
    path('Register', HandleRegisterView.as_view(), name="register"),
    #path('Contact_Us',ContactView.as_view(), name="contact"),

    #get data from template and pass in forms.py file using class base view
    path('Contact_Us',ContactFormView.as_view(), name="contact"),
    

]
