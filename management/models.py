from django.db import models

# Create your models here.
# Admission students database 
class Student_database(models.Model):
    id=models.AutoField(primary_key=True)
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Father_name=models.CharField(max_length=100)
    Student_cnic=models.CharField(max_length=15 ,unique=True)
    Father_cnic=models.CharField(max_length=15 )
    Address=models.TextField()  # main address
    Previous_Qualification=models.CharField(max_length=100)
    Total_marks=models.IntegerField()
    Obtained_marks=models.IntegerField()
    Percentage=models.CharField(max_length=15)
    previous_institute=models.CharField(max_length=100)
    selected_program=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.First_name + " " + self.Last_name
class UserAuth(models.Model):
    user_id = models.CharField(max_length=50, unique=True , null=True , blank=True)  # same as Roll No
    password = models.CharField(max_length=100 , null=True , blank=True)
class Engineering(models.Model):
    child=models.OneToOneField(
        Student_database,
        on_delete=models.CASCADE,
        related_name="Eng"
        )
class Medical(models.Model):
    child=models.OneToOneField(
        Student_database,
        on_delete=models.CASCADE,
        related_name="Med"
        )
class ICS(models.Model):
    child=models.OneToOneField(
        Student_database,
        on_delete=models.CASCADE,
        related_name="ICS"
        )
    
    auth = models.OneToOneField(UserAuth, on_delete=models.CASCADE , null=True , blank=True)
    image = models.ImageField(upload_to='students/', null=True, blank=True)      
    def __str__(self):
        return f"{self.child.First_name} {self.child.Last_name}"  # optional for admin readability
class subjects(models.Model):
    ics=models.ForeignKey(ICS,on_delete=models.CASCADE)
    subject=models.CharField(max_length=100)
    

class ICom(models.Model):
    child=models.OneToOneField(
        Student_database,
        on_delete=models.CASCADE,
        related_name="ICom"
        )
class Arts(models.Model):
    child=models.OneToOneField(
        Student_database,
        on_delete=models.CASCADE,
        related_name="Arts"
        )
class Seience(models.Model):
    child=models.OneToOneField(
        Student_database,
        on_delete=models.CASCADE,
        related_name="Seience"
        )

    