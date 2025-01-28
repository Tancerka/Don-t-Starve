from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# Model dla stolików w restauracji
class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)  # Numer stolika
    seats = models.PositiveIntegerField()  # Liczba miejsc przy stoliku

    def __str__(self):
        return f"Stolik {self.number} ({self.seats} miejsc)"

# Model dla dostępnych godzin rezerwacji
#wywalic
class ReservationTime(models.Model):
    time = models.TimeField(unique=True)  # Godzina dostępna dla rezerwacji

    def __str__(self):
        return self.time.strftime("%H:%M")

# Model dla rezerwacji
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Klient rezerwujący (powiązanie z użytkownikiem)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)  # Powiązanie ze stolikiem
    date = models.DateField()  # Data rezerwacji
    time = models.ForeignKey(ReservationTime, on_delete=models.CASCADE)  # Godzina rezerwacji
    created_at = models.DateTimeField(auto_now_add=True)  # Data utworzenia rezerwacji

    def __str__(self):
        return f"Rezerwacja na {self.date} o {self.time} ({self.user.username})"

# Model dla menu dań
class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(default='https://example.com/placeholder.jpg')

    def __str__(self):
        return self.name

# Model dla koszyka
class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Powiązanie koszyka z użytkownikiem
    items = models.ManyToManyField(Dish, through='BasketItem')  # Powiązanie z daniami

    def __str__(self):
        return f"Koszyk użytkownika {self.user.username}"

# Element koszyka
class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)  # Powiązanie z koszykiem
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)  # Powiązanie z daniem
    quantity = models.PositiveIntegerField(default=1)  # Ilość zamówionych dań

    def __str__(self):
        return f"{self.quantity} x {self.dish.name} ({self.basket.user.username})"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username
