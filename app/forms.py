"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    city = forms.CharField(label='Ваш город', min_length=2, max_length=100)
    job = forms.CharField(label='Профессия', min_length=2, max_length=100)
    gender = forms.ChoiceField(label='Пол',
                              choices = [('1', 'Мужской'), ('2', 'Женский'), ('3', 'Неважно')],
                              widget=forms.RadioSelect, initial=1)
    internet = forms.ChoiceField(label='Частота посещения сайта',
                                 choices=[('1', 'Часто'),('2', 'Нечасто'),
                                          ('3', 'Редко')], initial=1)
    notice = forms.ChoiceField(label='Уведомлять вас по почте?',
                               choices=[('1', 'Да'), ('2', 'Нет')], initial=1)
    email = forms.EmailField(label='Почта')
    message = forms.CharField(label='Расскажите о себе',
                              widget=forms.Textarea(attrs={'rows':12, 'cols':20}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('text',)
        labels = {'text':'Прокомментировать'}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'text':'Добавить блог',
                  'description':'Описание',
                  'content':'Содержание',
                  'image':'Картинка'}

