from django.db import models
from datetime import datetime
# Create your models here.


# Create your models here.
########################################## TABLE 1 ###################################################
class Person(models.Model):
    # don't need to make id, becuase python will do it= autogenerates!
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.Charfield(max_length=70)
    # user_name = models.CharField(max_length=20)
    # password = models.CharField(max_length=20)
    city = models.Charfield(max_length=30)
    state = models.Charfield(max_length=2)
    zip = models.IntegerField(max_length=5)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)

    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automailly does

    class Meta:
        db_table = "person"

    # ACCESS DATA--> if try to look at a single record, we are going to return the description
    # the description= the description field from the table
    # This is what is going to be displayed to the ADMIN!!
    def __str__(self):
        return self.first_name + " " + self.last_name


########################################### TABLE 2 ###############################################
class Customer(models.Model):
    # don't need to make id, becuase python will do it= autogenerates!
    first_name = models.CharField(max_length=30)
    business_name = models.CharField(max_length=30)
    # user_name = models.CharField(max_length=20)
    # password = models.CharField(max_length=20)
    # edit this later!
    customer_request_notes = models.CharField(max_length=260)

    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automailly does

    class Meta:
        db_table = "customer"

    # ACCESS DATA--> if try to look at a single record, we are going to return the description
    # the description= the description field from the table
    # This is what is going to be displayed to the ADMIN!!
    def __str__(self):
        return self.first_name + " " + self.last_name


##################################### Table 3 #######################################################


class Employee_Position(models.Model):
    # don't need to make id, becuase python will do it= autogenerates!
    emp_position = models.models.CharField(max_length=30)
    emp_position_description = models.CharField(max_length=260)

    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automailly does

    class Meta:
        db_table = "emp_position"

    # ACCESS DATA--> if try to look at a single record, we are going to return the description
    # the description= the description field from the table
    # This is what is going to be displayed to the ADMIN!!
    def __str__(self):
        return self.emp_position


####################################### TABLE 4 ###################################################


class Employee(models.Model):
    # don't need to make id, becuase python will do it= autogenerates!
    hire_date = models.DateField((""), auto_now=False, auto_now_add=False)
    # need to make this SINGULAR
    qualifications = models.CharField(max_length=30)
    # user_name = models.CharField(max_length=20)
    # password = models.CharField(max_length=20)
    # edit this later!
    position_id = models.ForeignKey(
        Employee_Position,

    )
    # edit this later! --> do we need this?
    person_id = models.ForeignKey(
        Person,

    )

    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automailly does

    class Meta:
        db_table = "employee"

    # ACCESS DATA--> if try to look at a single record, we are going to return the description
    # the description= the description field from the table
    # This is what is going to be displayed to the ADMIN!!
    def __str__(self):
        return self.first_name + " " + self.last_name

#####  Tables left to fill #####
# product_category
# product
# order_details
# order
# ticket
####################################### TABLE 5 ###################################################


####################################### TABLE 6 ###################################################


####################################### TABLE 7 ###################################################


####################################### TABLE 8 ###################################################


####################################### TABLE 9 ###################################################
