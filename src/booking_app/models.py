from django.db import models
from django.core.exceptions import ValidationError


def validate_persons_age(value):
    if int(value) < 18 or int(value) > 90:
        raise ValidationError(
            f"Введенный возраст {value} введен некорректно, от 18 до 90"
        )

# Create your models here.
class User(models.Model):
    SEX_PERSON = {
        "m": "male",
        "f": "female",
    }
    first_name = models.CharField(max_length=30, null=True, verbose_name="Имя")
    last_name = models.CharField(max_length=50, null=True, verbose_name="Фамилия")
    age = models.PositiveIntegerField(null=True, verbose_name="Возраст", validators=[validate_persons_age])
    sex = models.CharField(max_length=1, choices=SEX_PERSON, null=True, verbose_name="Пол")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=["last_name", "first_name"]),
            models.Index(fields=["last_name"], name="first_name_idx"),
            models.Index(fields=["age"], name="age_idx"),
            models.Index(fields=["sex"], name="sex_idx"),
        ]

    def __str__(self):
        return f" {self.first_name} {self.last_name}"


class Person(User):
    guest_rating = models.IntegerField(null=True)


class Hotel_owner(User):
    owner_exp_status = models.IntegerField(null=True)


class Hotel(models.Model):
    name = models.CharField(max_length=50, null=True)
    star = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=40, null=True)
    rating = models.FloatField(null=True)
    owners = models.ForeignKey(
        to="Hotel_owner",
        on_delete=models.SET_NULL,
        null=True,
        related_name="hotels"
    )

    class Meta:
        indexes = [
            models.Index(fields=["name", "address"]),
            models.Index(fields=["name"], name="name_idx"),
            models.Index(fields=["star"], name="star_idx"),
            models.Index(fields=["address"], name="address_idx"),
        ]

    def __str__(self):
        return f" {self.name} {self.rating}"


class BookInfo(models.Model):
    detail = models.CharField(max_length=200, null=True)
    book_time = models.DateTimeField(auto_now_add=True)
    persons = models.ForeignKey(
        to="Person",
        on_delete=models.SET_NULL,
        null=True,
        related_name="book_info"
    )
    hotels = models.ForeignKey(
        to="Hotel",
        on_delete=models.SET_NULL,
        null=True,
        related_name="book_info"
    )


class Comment(models.Model):
    comment = models.CharField(max_length=200, null=True)
    comment_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True


class HotelsComment(Comment):
    hotel_rating = models.PositiveIntegerField(null=True)
    hotels = models.ForeignKey(
        to="Hotel",
        on_delete=models.SET_NULL,
        null=True,
        related_name="hotel_comments"
    )
    persons = models.ForeignKey(
        to="Person",
        on_delete=models.SET_NULL,
        null=True,
        related_name="hotel_comments"
    )

    def __str__(self):
        return f" {self.comment}"


class PersonComment(Comment):
    person_rating = models.PositiveIntegerField(null=True)
    hotels = models.ForeignKey(
        to="Hotel",
        on_delete=models.SET_NULL,
        null=True,
        related_name="person_comments"
    )
    persons = models.ForeignKey(
        to="Person",
        on_delete=models.SET_NULL,
        null=True,
        related_name="person_comments"
    )

    def __str__(self):
        return f" {self.comment}"


class Profile(models.Model):
    photo = models.ImageField(null=True, blank=True)
    id_card_number = models.IntegerField(null=True)
    serial = models.CharField(null=True, max_length=30)
    persons = models.OneToOneField(
        to="User",
        on_delete=models.CASCADE,
        null=True,
        related_name="profile"
    )


class Hobby(models.Model):
    name = models.CharField(max_length=50, null=True)
    detail = models.CharField(max_length=200, null=True)
    owners = models.ManyToManyField(
        to="User",
        related_name="hobbies",
    )

    def __str__(self):
        return f" {self.name}"
