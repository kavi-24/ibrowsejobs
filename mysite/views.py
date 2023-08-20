from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.db.utils import IntegrityError

from .models import Student


def home(request):
    return render(request, 'mysite/home.html', context={"active": "Home", "is_logged_in": False})


def courses(request):
    return render(request, 'mysite/courses.html', context={"active": "Courses", "is_logged_in": True})


def contact_us(request):
    return render(request, 'mysite/contact-us.html', context={"active": "Contact Us", "is_logged_in": False})


def digital_services(request):
    return render(request, 'mysite/digital-services.html', context={"active": "Digital Services", "is_logged_in": True})


def sign_up(request):
    return render(request, 'mysite/login-signup.html', context={"active": "Login Signup", "is_logged_in": False})


def profile(request):
    return render(request, 'mysite/profile.html', context={"active": "Profile", "is_logged_in": True})


def create_user(request: HttpRequest):
    if request.method == "POST":
        data = request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        try:
            student = Student.objects.create(
                first_name=data["firstname"],
                last_name=data["lastname"],
                email=data["signupemail"],
                password=data["password"],
            )
        except IntegrityError:
            return HttpResponse("Such an email address already exists")
        return HttpResponse(str(student))

def login_user(request: HttpRequest):
    if request.method == "POST":
        data = request.POST.dict()
        email = data["logemail"]
        password = data["logpass"]

        student = Student.objects.filter(email=email).first()
        if student == None:
            return HttpResponse("No such email address exists")
        if student.password == password:
            return HttpResponse("Login Okie")
        return HttpResponse("Invalid username or passwprd")