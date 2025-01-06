from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        label='Введите логин',
        required=True
    )
    password = forms.CharField(
        min_length=8,
        label='Введите пароль',
        required=True,
        widget=forms.PasswordInput
    )
    repeat_password = forms.CharField(
        min_length=8,
        label='Повторите пароль',
        required=True,
        widget=forms.PasswordInput
    )
    age = forms.IntegerField(
        min_value=1,
        max_value=120,
        label='Введите свой возраст',
        required=True,
        widget=forms.NumberInput
    )