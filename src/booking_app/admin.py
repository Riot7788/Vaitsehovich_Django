from django.contrib import admin

from .models import (
    Person, Profile,
    Hotel, HotelsComment,
    BookInfo, Hobby,
    Hotel_owner,
    PersonComment, User,
)


class BookInfoInLine(admin.TabularInline):
    model = BookInfo


class HotelAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "owners"]
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "address"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": [("star", "rating"), "owners"],
            },
        ),
    ]
    list_filter = ["address", "star"]
    inlines = [
        BookInfoInLine,
    ]


class HobbyInline(admin.TabularInline):
    model = Hobby.owners.through
    extra = 3


class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "age", "sex"]
    search_fields = ["first_name", "last_name"]
    list_editable = ["age"]
    list_filter = ["age", "sex"]
    list_per_page = 30
    inlines = [
        HobbyInline,
    ]


class PersonAdminInLine(admin.TabularInline):
    model = Profile


class PersonAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "age", "sex"]
    list_filter = ["age", "sex"]
    inlines = [
        PersonAdminInLine,
    ]


class HobbyAdmin(admin.ModelAdmin):
    list_display = ["name", "detail"]


class HotelsCommentAdmin(admin.ModelAdmin):
    list_display = ["hotels", "comment"]
    list_filter = ["hotels"]
    list_per_page = 30


class PersonCommentAdmin(admin.ModelAdmin):
    list_display = ["hotels", "person_rating"]
    list_per_page = 30


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id_card_number", "serial", "persons"]


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["persons", "detail"]


class HotelInline(admin.TabularInline):
    model = Hotel


class HotelOwnerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "age", "sex"]
    search_fields = ['first_name', 'last_name']
    list_editable = ["age"]
    list_filter = ["last_name", "age", "sex"]
    inlines = [
        HotelInline,
    ]


admin.site.register(Person, PersonAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelsComment, HotelsCommentAdmin)
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(Hobby, HobbyAdmin)
admin.site.register(PersonComment, PersonCommentAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Hotel_owner, HotelOwnerAdmin)
