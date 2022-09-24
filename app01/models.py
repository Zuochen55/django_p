from django.db import models

# Create your models here.

class Admin(models.Model):
    name = models.CharField(verbose_name="Name", max_length=32)
    password = models.CharField(verbose_name="Password", max_length=64)

class Department(models.Model):
    title = models.CharField(verbose_name="depatment_title", max_length=32)

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    name = models.CharField(verbose_name="User", max_length=32)
    password = models.CharField(verbose_name="Password", max_length=64)
    age = models.IntegerField(verbose_name="Age")

    account = models.DecimalField(verbose_name="Account", max_digits=10, decimal_places=2,default=0)

    create_time = models.DateField(verbose_name="Create time")
    depart_id = models.ForeignKey(verbose_name="Department",to='Department', to_field='id', on_delete=models.CASCADE)

    gender_choices=(
        (1,"male"),
        (2, "female"),
        (3, "divers")
    )
    gender=models.SmallIntegerField(verbose_name="Gender",choices=gender_choices)

class VipNumber(models.Model):
    mobile = models.CharField(verbose_name="VIP number", max_length=11)
    price = models.IntegerField(verbose_name="price",default=0)
    level_choices=(
        (1,"level 1"),
        (2,"level 2"),
        (3,"level 3"),
        (4,"level 4")
    )
    level = models.SmallIntegerField(verbose_name="level",choices=level_choices,default=1)

    status_choices = (
        (1,"for sale"),
        (2,"sold")
    )
    status = models.SmallIntegerField(verbose_name="status", choices=status_choices,default=1)


