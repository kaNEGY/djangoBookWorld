from datetime import date

from django import forms

from catalog.models import Book


class AuthorsForm(forms.Form):
    firstName = forms.CharField(label='Имя автора')
    lastName = forms.CharField(label='Фамилия автора')
    dateOfBirth = forms.DateField(label='Дата рождения', initial=format(date.today()),
                                  widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    dateOfDeath = forms.DateField(label='Дата смерти', initial=format(date.today()),
                                  widget=forms.widgets.DateInput(attrs={'type': 'date'}))


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'language', 'author', 'summary', 'isbn']
