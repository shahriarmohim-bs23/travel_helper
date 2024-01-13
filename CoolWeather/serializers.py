from rest_framework import serializers
from .services import DistrictTemperature

temperature = DistrictTemperature()


class CoolestDistrictSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    temperature = serializers.DecimalField(read_only=True,
                                           max_digits=5,
                                           decimal_places=2)


class TravelRecommendationSerializer(serializers.Serializer):
    location = serializers.CharField(write_only=True)
    destination = serializers.CharField(write_only=True)
    date = serializers.DateField(write_only=True, format='%Y-%m-%d')
    recommendation = serializers.CharField(read_only=True)

    def create(self, validated_data):
        location = validated_data['location']
        destination = validated_data['destination']
        date = validated_data['date']
        location_temperature = temperature.get_district_temperature_by_name(
            name=location,
            date=date,
        )

        destination_temperature = temperature.get_district_temperature_by_name(
            name=destination,
            date=date
        )

        recommendation = None

        if location_temperature > destination_temperature:
            recommendation = f"Travel to {destination}!"
        elif location_temperature <= destination_temperature:
            recommendation = f"Don't Travel to {destination}!"

        return {'recommendation': recommendation}
