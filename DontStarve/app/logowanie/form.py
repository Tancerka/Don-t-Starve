from django import forms
from django.contrib.auth.forms import AuthenticationForm, authenticate

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa użytkownika'}),
        label="Nazwa użytkownika",
        required=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Hasło'}),
        label="Hasło",
        required=False
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'required': 'Nazwa użytkownika jest wymagana'}
        self.fields['password'].error_messages = {'required': 'Hasło jest wymagane'}

    def clean(self):
        #cleaned_data = super().clean()
         # Pobierz dane z formularza
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        # Sprawdź poprawność danych logowania
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Błędne dane. Sprawdź nazwę użytkownika i hasło.")
        else:
            raise forms.ValidationError("Błędne dane. Sprawdź nazwę użytkownika i hasło.")
        
        # Użyj domyślnego clean() dla reszty logiki
        return super().clean()