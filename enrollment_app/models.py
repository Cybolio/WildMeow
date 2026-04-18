from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=50)
    fullName = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Role = models.CharField(max_length=50)
    Phone_No = models.CharField(max_length=12)
    EmailAddress = models.EmailField()
    AccountStatus = models.CharField(max_length=50)
    Admin = models.CharField(max_length=50)
    Permission_Level = models.CharField(max_length=50)

    def __str__(self):
        return self.Username


class Payment(models.Model):
    Payment_ID = models.AutoField(primary_key=True)
    Student = models.CharField(max_length=50)
    Payment_Date = models.DateField()
    Payment_Status = models.CharField(max_length=50)
    Payment_Option = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment {self.Payment_ID}"


class Waitlist(models.Model):
    Waitlist_ID = models.AutoField(primary_key=True)
    Request_Date = models.DateField()
    Position_Number = models.IntegerField()

    def __str__(self):
        return f"Waitlist {self.Waitlist_ID}"