from django.db import models

class Diabetes_data(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    pregnancy = models.IntegerField()
    glucose = models.IntegerField()
    blood_Pressure = models.IntegerField()
    insulin = models.IntegerField()
    bmi = models.FloatField()
    age = models.IntegerField()
    time = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.name
    
class FeedBack(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    feedback = models.TextField()


    def __str__(self):
        return self.name