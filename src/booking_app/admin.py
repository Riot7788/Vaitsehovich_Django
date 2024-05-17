from django.contrib import admin

from .models import (
    Person, Profile,
    Hotel, HotelsComment,
    BookInfo, Hobby,
    Hotel_owner,
    PersonComment, User,
)

admin.site.register(Person)
admin.site.register(Profile)
admin.site.register(Hotel)
admin.site.register(HotelsComment)
admin.site.register(BookInfo)
admin.site.register(Hobby)
admin.site.register(PersonComment)
admin.site.register(User)
admin.site.register(Hotel_owner)
