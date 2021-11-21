from django.contrib import admin

# Register your models here.
from .models import Employee, Employee_Position, Person, Customer, product_category, product, order_detail, job_order,  ticket


# Register your models here
admin.site.register(Person)
admin.site.register(Customer)
admin.site.register(Employee_Position)
admin.site.register(Employee)
admin.site.register(product_category)
admin.site.register(product)
admin.site.register(order_detail)
admin.site.register(job_order)
admin.site.register(ticket)
