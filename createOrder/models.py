from django.db import models
from datetime import datetime
# Create your models here.

# --> for null/not null contraints --> https://newbedev.com/not-null-constraint-failed-after-adding-to-models-py


# Create your models here.
########################################## TABLE 1 ###################################################
class Person(models.Model):
    # don't need to make id, becuase python will do it= autogenerates!
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=40, null=True)
    # user_name = models.CharField(max_length=20)
    # password = models.CharField(max_length=20)
    city = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    zip = models.IntegerField(max_length=5, null=True)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=30)

    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automatically does

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

    #
    #
    #first_name = models.CharField(max_length=30)
    business_name = models.CharField(max_length=30)
    # user_name = models.CharField(max_length=20)
    # password = models.CharField(max_length=20)
    # edit this later!
    customer_request_notes = models.CharField(max_length=60)
    # edit this later! --> do we need this?
    #
    #
    # HOW do we make sure this inherits from the person class??
    # How do we see the person class table??
    person_id = models.ForeignKey(
        Person,
        default="",
        verbose_name="Person ID",
        on_delete=models.DO_NOTHING,
        to_field="person_id",
    )

    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automatically does

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
    position = models.CharField(max_length=20)
    position_description = models.CharField(max_length=50)

    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automatically does

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
    hire_date = models.DateField(verbose_name="When Hired")
    # need to make this SINGULAR
    qualifications = models.CharField(max_length=15)
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
    # python will automatically do this, but this just makes SURE and will override what python automatically does

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
