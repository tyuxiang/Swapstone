from django.db import models

# Create your models here.
class Booth(models.Model):
    project_id = models.CharField(max_length=20)
    length =  models.DecimalField(decimal_places=2,max_digits=10,max_length=5)
    width =  models.DecimalField(decimal_places=2,max_digits=10,max_length=5)
    area =   models.DecimalField(decimal_places=2,max_digits=10,max_length=5)
    project_name =  models.CharField(max_length=100)
    industry =  models.CharField(max_length=100)
    length_pixel =  models.DecimalField(decimal_places=2,max_digits=10,max_length=5)
    width_pixel =  models.DecimalField(decimal_places=2,max_digits=10,max_length=5)
    rotation = models.DecimalField(decimal_places=2,max_digits=10,max_length=5,default = -1)
    position_x =models.DecimalField(decimal_places=2,max_digits=10,max_length=100,default = -1)
    position_y =models.DecimalField(decimal_places=2,max_digits=10,max_length=100,default =-1)
    in_campus_centre =models.BooleanField()
    
    # saved_map = models.ForeignKey(Map,on_delete=models.CASCADE)


# class Map(models.Model):
#     name = models.CharField(max_length = 100)

