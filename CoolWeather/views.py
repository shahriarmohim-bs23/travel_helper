import logging
import time
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CoolestDistrictSerializer, \
    TravelRecommendationSerializer
from .services import DistrictTemperature

logger = logging.getLogger(__name__)
User = get_user_model()

district_temperature = DistrictTemperature()


class CoolestDistricts(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            start_time = time.time()
            district_temperatures = (district_temperature.
                                     get_districts_temperature())
            response_time = time.time() - start_time

            if response_time > 0.5:
                return (Response(
                    {"message": "Time exceed 500ms"},
                    status=status.HTTP_204_NO_CONTENT)
                )

            serializer = CoolestDistrictSerializer(
                district_temperatures,
                many=True
            )
            return Response(serializer.data)

        except Exception as ex:
            logger.error(str(ex), exc_info=True)

        return Response(
            {"message": "Server error!"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class TravelRecommendationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = TravelRecommendationSerializer(data=request.data)
            if serializer.is_valid():
                result = serializer.save()
                return Response(result)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        except Exception as ex:
            logger.error(str(ex), exc_info=True)

        return Response(
            {"message": "Server error!"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
