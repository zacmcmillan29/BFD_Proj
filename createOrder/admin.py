from django.contrib import admin

# Register your models here.
# Register your models here.
# other models --> , , Trip_Category, Destination, Interests
from .models import Customer

# Register your models here
admin.site.register(Customer)
# admin.site.register(Trip_Category)
# admin.site.register(Destination)
# admin.site.register(Interests)
