from django.db import models

# Crop model field
class Crop (models.Model):
    crop_name = models.CharField(max_length=50)
    price = models.BigIntegerField(default=0.0)
    location = models.CharField(max_length=75)
    state = models.CharField(max_length=75)
    date = models.DateField(auto_now=True)

# user data
class user_data(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    psw = models.CharField(max_length=75)
    location = models.CharField(max_length=75)
    state = models.CharField(max_length=75)

    def __str__(self):
        return self.name

# admin data
class admin_data(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    psw = models.CharField(max_length=75)
    location = models.CharField(max_length=75)
    state = models.CharField(max_length=75)

    def __str__(self):
        return self.name

# suggestion filler
class suggestion(models.Model):
    username = models.CharField(max_length=100)
    text = models.CharField(max_length=600)

    def __str__(self):
        return self.username

