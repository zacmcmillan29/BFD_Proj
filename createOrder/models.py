from django.db import models
from datetime import datetime
# Create your models here.


# Create your models here.
# TABLE 1
class Customer(models.Model):
    # don't need to make id, becuase python will do it= autogenerates!
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automailly does

    class Meta:
        db_table = "customer"

    # ACCESS DATA--> if try to look at a single record, we are going to return the description
    # the description= the description field from the table
    # This is what is going to be displayed to the ADMIN!!
    def __str__(self):
        return self.first_name + " " + self.last_name

