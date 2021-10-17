from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

# class Musician(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     instrument = models.CharField(max_length=100)
#
# class Album(models.Model):
#     artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     release_date = models.DateField()
#     num_stars = models.IntegerField()
#
# class Owner(models.Model):
#     name = models.CharField(max_length=50)
#     surename = models.CharField(max_length=50)
#
#
# class Dog(models.Model):
#     name = models.CharField(max_length=50, null=False)
#     owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
#     breed = models.CharField(max_length=100)
#     age = models.IntegerField(max_length=100, default=1)

