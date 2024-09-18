from django.db import models


class Sensor(models.Model):
    sensor_name = models.CharField(max_length=40, versobe_name='Нaзвание')
    description = models.CharField(max_length=200, versobe_name='Описание')


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
