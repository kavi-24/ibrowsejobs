from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=50)

class UsedCoupons(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    coupon_code = models.CharField(max_length=50)


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_desc = models.CharField(max_length=200)
    created_on = models.DateField()  # YYYY-MM-DD
    price = models.FloatField()
    discounted_price = models.IntegerField(default=0)
    rating = models.FloatField()
    num_of_rating = models.IntegerField()
    coupon_code = models.CharField(max_length=50, default="_")
    coupon_disc = models.IntegerField(default=0)

class CourseContent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    courseContent_name = models.CharField(max_length=100)
    courseContent_type = models.CharField(max_length=20)  # Video | Quiz | Notes
    courseContent_media = models.CharField(max_length=200)  # URL