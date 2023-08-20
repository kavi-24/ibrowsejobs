# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name='home'),
    path('courses/', views.courses, name="courses"),
    path('contact-us/', views.contact_us, name="contact-us"),
    path('digital-services/', views.digital_services, name="digital-services"),
    path('login-signup/', views.sign_up, name="login-signup"),
    path('profile/', views.profile, name="profile"),
]