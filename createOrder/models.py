from django.db import models
from datetime import datetime, timedelta
# Create your models here.

# --> for null/not null constraints --> https://newbedev.com/not-null-constraint-failed-after-adding-to-models-py


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
    zip = models.IntegerField(null=True)
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
    customer_request_notes = models.CharField(max_length=60, null=True)
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
        to_field="id",
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
    # position_id = models.ForeignKey(
    #     Employee_Position,

    # )
    # # edit this later! --> do we need this?
    # person_id = models.ForeignKey(
    #     Person,

    # )

    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automatically does

    class Meta:
        db_table = "employee"

    # ACCESS DATA--> if try to look at a single record, we are going to return the description
    # the description= the description field from the table
    # This is what is going to be displayed to the ADMIN!!
    def __str__(self):
        return self.first_name + " " + self.last_name


####################################### TABLE 5 ################################################### product_category

class product_category(models.Model):
    # don't need to make id, becuase python will do it= autogenerates!
    product_category_name = models.CharField(max_length=50)
    product_category_description = models.CharField(max_length=30)

    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automatically does

    class Meta:
        db_table = "product_cateogory"

    # ACCESS DATA--> if try to look at a single record, we are going to return the description
    # the description= the description field from the table
    # This is what is going to be displayed to the ADMIN!!
    def __str__(self):
        return self.product_category_description

####################################### TABLE 6 ################################################### product

class product(models.Model):
    # don't need to make id, becuase python will do it= autogenerates!
    product_name = models.CharField(max_length=25)
    product_category_id = models.ForeignKey(
        product_category,
        default="",
        verbose_name="Product Category ID",
        on_delete=models.DO_NOTHING,
        to_field="id",
    )

    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automatically does

    class Meta:
        db_table = "product"

    # ACCESS DATA--> if try to look at a single record, we are going to return the description
    # the description= the description field from the table
    # This is what is going to be displayed to the ADMIN!!
    def __str__(self):
        return self.product_name


####################################### TABLE 7 ################################################### order_detail

class order_detail(models.Model):
    # don't need to make id, becuase python will do it= autogenerates!
    product_id = models.ForeignKey(
        product,
        default="",
        verbose_name="Product ID",
        on_delete=models.DO_NOTHING,
        to_field="id",
    )
    quantity = models.IntegerField(null=True)
    quoted_price = models.DecimalField( max_digits=6, decimal_places=2)
    order_notes = models.CharField(max_length = 500)

    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automatically does

    class Meta:
        db_table = "order_detail"

    # ACCESS DATA--> if try to look at a single record, we are going to return the description
    # the description= the description field from the table
    # This is what is going to be displayed to the ADMIN!!
    def __str__(self):
        return self.product_id + " " + self.order_notes


####################################### TABLE 8 ################################################### job order

class job_order(models.Model):
    # don't need to make id, becuase python will do it= autogenerates!
    order_date = models.DateTimeField(default=datetime.today, blank = True)
    customer_id = models.ForeignKey(
        Customer,
        default="",
        verbose_name="Customer ID",
        on_delete=models.DO_NOTHING,
        to_field="id",
    )
    employee_id = models.ForeignKey(
        Employee,
        default="",
        verbose_name="Employee ID",
        on_delete=models.DO_NOTHING,
        to_field="id",
    )


    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automatically does

    class Meta:
        db_table = "job_order"

    # ACCESS DATA--> if try to look at a single record, we are going to return the description
    # the description= the description field from the table
    # This is what is going to be displayed to the ADMIN!!
    def __str__(self):
        return self.order_date + " " + self.employee_id


####################################### TABLE 9 ################################################### ticket


class ticket(models.Model):
    # don't need to make id, becuase python will do it= autogenerates!
    order_id = models.ForeignKey(
        job_order,
        default="",
        verbose_name="Order ID",
        on_delete=models.DO_NOTHING,
        to_field="id",
    )
    product_id = models.ForeignKey(
        product,
        default="",
        verbose_name="Product ID",
        on_delete=models.DO_NOTHING,
        to_field="id",
    )
    employee_id = models.ForeignKey(
        Employee,
        default="",
        verbose_name="Employee ID",
        on_delete=models.DO_NOTHING,
        to_field="id",
    )
    confirmed_date = models.DateTimeField(default=datetime.today, blank = True)
    status = models.CharField( max_length=15)
    status_change_date = models.DateTimeField(default=datetime.today, blank = True)
    filing_cabinet = models.CharField( max_length=10)
    file_name = models.CharField( max_length=25)
    notes = models.CharField( max_length=500)


    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automatically does

    class Meta:
        db_table = "ticket"

    # ACCESS DATA--> if try to look at a single record, we are going to return the description
    # the description= the description field from the table
    # This is what is going to be displayed to the ADMIN!!
    def __str__(self):
        return self.order_id + " " + self.status + " " + self.notes