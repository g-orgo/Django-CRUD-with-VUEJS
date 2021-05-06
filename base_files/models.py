from django.db import models

class Garage_place(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=100)