from django import forms
from .models import Utilisateurs


class sign_upForm(forms.ModelForm):
    username = forms.CharField(label="Nom")
    email = forms.CharField(label="Email", widget=forms.EmailInput)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

    class Meta:
        model = Utilisateurs
        fields = ['username', 'email', 'password']
        labels = ['Nom utilisateur', 'Email', 'Mot de passe']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'w-full h-[25px] border-transparent rounded shadow-md ring ring-slate-300 hover:ring hover:ring-red-300 font-semibold',
                                                     'id': 'username'})
        self.fields['email'].widget.attrs.update({'class': 'w-full h-[25px] border-transparent rounded shadow-md ring ring-slate-300 hover:ring hover:ring-red-300 font-semibold',
                                                  'id': 'email'})
        self.fields['password'].widget.attrs.update({'class': 'w-full h-[25px] border-transparent rounded shadow-md ring ring-slate-300 hover:ring hover:ring-red-300 font-semibold',
                                                     'id': 'password'})

