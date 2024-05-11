from django.db import models


# Create your models here.

class Person(models.Model):
    SEX_PERSON = {
        "m": "male",
        "f": "female",
    }
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=1, choices=SEX_PERSON)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.first_name} {self.last_name}"

class Hotel(models.Model):
    name = models.CharField(max_length=40)
    star = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=40)
    rating = models.FloatField(null=True)
    persons = models.ManyToManyField(
        to="Person",
    )
    def __str__(self):
        return f" {self.name} {self.address}"


class Book_order_info(models.Model):
    detail = models.CharField(max_length=200, null=True)
    book_time = models.DateTimeField(auto_now_add=True)
    persons = models.ForeignKey(
        to="Person",
        on_delete=models.SET_NULL,
        null=True,
    )
    hotels = models.ForeignKey(
        to="Hotel",
        on_delete=models.SET_NULL,
        null=True,
    )

class HotelsComment(models.Model):
    comment = models.CharField(max_length=200,null=True)
    comment_time = models.DateTimeField(auto_now_add=True)
    hotels = models.ForeignKey(
        to="Hotel",
        on_delete=models.SET_NULL,
        null=True,
    )
    persons = models.ForeignKey(
        to="Person",
        on_delete=models.SET_NULL,
        null=True,
    )
    def __str__(self):
        return f" {self.comment}"

class Profile(models.Model):
    photo = models.ImageField(null=True, blank=True)
    id_card_number = models.IntegerField(null=True)
    serial = models.CharField(null=True, max_length=30)
    persons = models.OneToOneField(
        "Person",
        on_delete=models.CASCADE,
        null=True,
    )
    hotel_owner = models.OneToOneField(
        "Hotel_owner",
        on_delete=models.CASCADE,
        null=True,
    )

class Hobbies(models.Model):
    name = models.CharField(max_length=100, null=True)
    experience = models.IntegerField(null=True)
    persons = models.ManyToManyField(
        to="Person",
        null=True,
    )
    hotel_owner = models.ManyToManyField(
        to="Hotel_owner",
        null=True,
    )
    def __str__(self):
        return f" {self.name} {self.experience}"

class Hotel_owner(models.Model):
    m_or_f = {
        "m": "male",
        "f": "female",
    }
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50)
    hotels = models.ForeignKey(
        to="Hotel",
        on_delete=models.SET_NULL,
        null=True,
    )
    def __str__(self):
        return f" {self.first_name} {self.last_name}"