from django.db import models

# Create your models here.


class Devices(models.Model):
    device_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.device_name}"


class Reads(models.Model):
    sensor_id = models.ForeignKey(Devices, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    temp = models.FloatField()
