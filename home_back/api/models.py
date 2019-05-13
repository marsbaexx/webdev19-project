from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    e_mail = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    phone_n = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Admin(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    e_mail = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    phone_n = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Database(models.Model):
    id = models.IntegerField
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    UserInfo = models.CharField(max_legnth=30)
    OrganizationInfo = models.CharField(max_legnth=30)

    def __str__(self):
        return '{}: {}'.format(self.id, self.username)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.username
        }