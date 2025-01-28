from django import forms

class AddDishForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa dania'}),
        label="Nazwa dania"
    )
    description = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Opis'}),
        label="Opis"
    )
    price = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cena'}),
        label="Cena"
    )
    image_url = forms.URLField(
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Zdjęcie URL'}),
        label="Zdjęcie URL"
    )