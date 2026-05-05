from django.db import models

class Room(models.Model):
    Room_ID = models.AutoField(primary_key=True)
    Room_Code = models.CharField(max_length=50)
    Building_Name = models.CharField(max_length=100)
    Floor = models.IntegerField()
    Room_Type = models.CharField(max_length=50)
    Capacity = models.IntegerField()

class Department(models.Model):
    Dept_ID = models.AutoField(primary_key=True)
    Dept_Name = models.CharField(max_length=100)
    Dept_Head = models.CharField(max_length=100)
    Contact_No = models.CharField(max_length=20)
    Office_Location = models.CharField(max_length=100)
    Contact_Email = models.EmailField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

class Faculty(models.Model):
    Faculty_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Date_Hired = models.DateField()
    Expertise = models.CharField(max_length=100)
    Position = models.CharField(max_length=50)
    Schedule = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class CourseOffering(models.Model):
    Section_ID = models.AutoField(primary_key=True)
    Course_Code = models.CharField(max_length=50)
    Instructor_Name = models.CharField(max_length=100)
    Students = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
