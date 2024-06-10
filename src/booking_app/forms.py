from django import forms

from .models import Person, HotelsComment


class UserForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "age", "sex", "photo"]



class HotelCommentForm(forms.ModelForm):
    class Meta:
        model = HotelsComment
        fields = ['hotels', 'persons', 'comment', 'photo']
        widgets = {
            'comment': forms.Textarea(attrs={"size": 500, 'class': 'special', "required": False})
        }