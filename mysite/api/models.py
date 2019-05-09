from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length = 30)
    e_mail = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    phone_n = models.CharField(max_length = 30)
    country = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    street = models.CharField(max_length = 30)


    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    