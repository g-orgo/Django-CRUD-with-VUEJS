from django.db import models

class Garage_place(models.Model):
    garage_id = models.AutoField(primary_key=True)
    garage_name = models.CharField(max_length=100)