from django import forms

from .models import Person, HotelsComment


class UserForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "age", "sex"]



class HotelCommentForm(forms.ModelForm):
    class Meta:
        model = HotelsComment
        fields = ['hotels', 'persons', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'special', "required": False})
        }