from django.db import models


class Program(models.Model):
    Program_ID = models.AutoField(primary_key=True)
    Program_Name = models.CharField(max_length=200)
    Program_Code = models.CharField(max_length=20, unique=True)
    Department_ID = models.IntegerField()
    Total_Units = models.IntegerField()
    Program_Duration = models.IntegerField(help_text="Duration in years")
    Associated_Courses = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.Program_Code} - {self.Program_Name}"

    class Meta:
        db_table = 'program'


class Semester(models.Model):
    TERM_CHOICES = [
        ('1st', '1st Semester'),
        ('2nd', '2nd Semester'),
        ('Summer', 'Summer'),
    ]

    Semester_ID = models.AutoField(primary_key=True)
    Academic_Year = models.CharField(max_length=20, help_text="e.g. 2024-2025")
    Term = models.CharField(max_length=10, choices=TERM_CHOICES)
    Start_Date = models.DateField()
    End_Date = models.DateField()
    Enrollment_Start = models.DateField()
    Enrollment_End = models.DateField()

    def __str__(self):
        return f"{self.Academic_Year} - {self.Term}"

    class Meta:
        db_table = 'semester'
