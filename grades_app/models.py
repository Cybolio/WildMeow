from django.db import models


class Grade(models.Model):
    report_id = models.AutoField(primary_key=True)
    courses_offered = models.CharField(max_length=100)
    grades = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    total_enrolled = models.IntegerField()
    total_waitlist = models.IntegerField()
    demand_level = models.CharField(max_length=50)
    generated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.courses_offered} - {self.semester}"


class DemandReport(models.Model):
    report = models.OneToOneField(Grade, on_delete=models.CASCADE)
    semester_id = models.CharField(max_length=20)
    report_type = models.CharField(max_length=50)
    year = models.IntegerField()
    total_waitlist = models.IntegerField()
    demand_data = models.TextField()

    def __str__(self):
        return f"Report {self.report_type} - {self.year}"


class Prerequisite(models.Model):
    prerequisite_id = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=50)
    required_gr = models.CharField(max_length=20)

    def __str__(self):
        return self.course_code