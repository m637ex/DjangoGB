from django import forms # импортируем формы

class ImageForm(forms.Form):
    image = forms.ImageField()