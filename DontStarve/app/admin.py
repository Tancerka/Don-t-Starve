from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Reservation)
admin.site.register(Dish)
admin.site.register(Table)
admin.site.register(ReservationTime)
admin.site.register(Basket)
admin.site.register(BasketItem)
