from django.db import models

# Create your models here.
class Booth(models.Model):
    length =  models.DecimalField(max_length=5)
    width =  models.DecimalField(max_length=5)
    area =   length*width
    project_name =  models.CharField(max_length=100)
    position_x =models.DecimalField(max_length=100)
    position_y =models.DecimalField(max_length=100)
    in_campus_centre =models.BooleanField()
    saved_map = models.ForeignKey(Map,on_delete=models.CASCADE)


class Map(models.Model):
    name = models.CharField(max_length = 100)

