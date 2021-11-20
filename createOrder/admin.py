from django.contrib import admin

# Register your models here.
from .models import Employee, Employee_Position, Person, Customer


# Register your models here
admin.site.register(Person)
admin.site.register(Customer)
admin.site.register(Employee_Position)
admin.site.register(Employee)
