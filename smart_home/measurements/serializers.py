from rest_framework import serializers
from .models import Sensor, Measurement


# TODO: опишите необходимые сериализаторы
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['sensor_name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor_id', 'temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'sensor_name', 'description', 'measurements']
