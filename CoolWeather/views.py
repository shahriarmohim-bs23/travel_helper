import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CoolestDistrictSerializer
from .services import DistrictTemperature
import time

logger = logging.getLogger(__name__)

district_temperature = DistrictTemperature()


class CoolestDistricts(APIView):
    def get(self, request):
        try:
            start_time = time.time()
            district_temperatures = (district_temperature.
                                     get_district_temperature())
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
