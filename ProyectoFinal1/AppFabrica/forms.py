from django import forms
from .models import Zapato
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class MayoristaFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    telefono = forms.IntegerField()

# class ZapatoFormulario(forms.Form):
#     nombre = forms.CharField(max_length=50)
#     material = forms.CharField(max_length=50)
#     color = forms.CharField(max_length=50)
#     talle = forms.IntegerField()
#     stock = forms.IntegerField()
#     precio = forms.FloatField()
#     foto = forms.ImageField()

class ZapatoFormulario(forms.ModelForm):
    class Meta:
        model= Zapato
        fields=('nombre','material','color', 'talle', 'stock', 'precio', 'foto')

class FormProspecto(forms.Form):
    email = forms.EmailField()

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


    def clean_password2(self):

        print('self\n',self.cleaned_data)

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden!")
        return password2
