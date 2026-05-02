from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    ROLE_CHOICES = [('admin', 'Admin'), ('student', 'Student')]

    username = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_no = models.CharField(max_length=20)
    email_address = models.EmailField()
    account_status = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Payment(models.Model):
    PAYMENT_OPTION_CHOICES = [
        ('cash', 'Cash'),
        ('online', 'Online'),
        ('installment', 'Installment'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateField()
    payment_option = models.CharField(max_length=20, choices=PAYMENT_OPTION_CHOICES)

    def __str__(self):
        return f"Payment by {self.student} on {self.payment_date}"


class Waitlist(models.Model):
    waitlist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_date = models.DateField()
    position_number = models.IntegerField()

    def __str__(self):
        return f"Waitlist #{self.position_number} - {self.user}"