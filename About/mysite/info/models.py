from django.db import models


# Create your models here.

class Fund(models.Model):
    name = models.CharField(max_length=30)
    foundation_date = models.CharField(max_length=30)
    assets = models.IntegerField()


    def __str__(self):
        return self.name



class about(models.Model):
    Contacts = models.IntegerField()
    E_mail = models.CharField(max_length = 30)

    def __str__(self):
        return self.E_mail

class typeOfFund(models.Model):
    type = models.CharField(max_length = 30)


    def __str__(self):
        return self.type
