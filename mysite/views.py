from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'mysite/home.html', context={"active": "Home", "is_logged_in": False})

def courses(request):
    return render(request, 'mysite/courses.html', context={"active": "Courses", "is_logged_in": True})

def contact_us(request):
    return render(request, 'mysite/contact-us.html', context={"active": "Contact Us", "is_logged_in": False})

def digital_services(request):
    return render(request, 'mysite/digital-services.html', context={"active": "Digital Services", "is_logged_in": True})

def sign_up(request):
    return render(request, 'mysite/sign-up.html', context={"active": "Sign Up", "is_logged_in": False})

def profile(request):
    return render(request, 'mysite/profile.html', context={"active": "Profile", "is_logged_in": True})