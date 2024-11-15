from django.db import models

# Create your models here.
#models stores database tables,forms etc.,both frontend and backend
#models are classes

class Student(models.Model):
    image = models.ImageField(upload_to='student_images/', blank=True)
    name = models.CharField(max_length=50)
    admission_number = models.CharField(max_length=20, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    course = models.CharField(max_length=50)
    #for this form we will use whatever we have captured here to create a form

    def __str__(self):
        return self.name


    #now we create a file in the app called forms where we convert this model into form



