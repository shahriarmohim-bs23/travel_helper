from rest_framework import serializers


class CoolestDistrictSerializer(serializers.Serializer):
    name = serializers.CharField()
    temperature = serializers.FloatField()
