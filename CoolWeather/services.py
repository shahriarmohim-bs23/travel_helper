import requests
import openmeteo_requests
import requests_cache
from retry_requests import retry

district_url = (
    "https://raw.githubusercontent.com/strativ-dev/technical-screening-test"
    "/main/bd-districts.json"
)

weather_url = "https://api.open-meteo.com/v1/forecast"

cache_session = requests_cache.CachedSession(
    '.cache',
    expire_after=3600
)
retry_session = retry(
    cache_session,
    retries=5,
    backoff_factor=0.2
)
openmeteo = openmeteo_requests.Client(
    session=retry_session
)


class DistrictTemperature:
    @staticmethod
    def get_temperature(district):
        params = {
            "latitude": district.get('lat'),
            "longitude": district.get('long'),
            "hourly": "temperature_2m",
            "timezone": "auto",
            "forecast_days": 7
        }

        responses = openmeteo.weather_api(
            weather_url,
            params=params
        )

        hourly = responses[0].Hourly()
        temperatures_at_2pm = hourly.Variables(0).ValuesAsNumpy()[
                              14::24]
        average_temperature = (sum(temperatures_at_2pm) /
                               len(temperatures_at_2pm))

        return average_temperature

    def get_district_temperature(self):
        district_temperatures = []
        response = requests.get(district_url)
        if response.status_code == 200:
            json_data = response.json()
            districts_info = json_data.get('districts', [])
            for district in districts_info:
                average_temperature = self.get_temperature(district)
                district_temperatures.append(
                    {
                        "name": district.get('name'),
                        "temperature": average_temperature
                    }
                )

            sorted_district_temperatures = sorted(
                district_temperatures,
                key=lambda item: item['temperature']
            )
            top_10_district_temperatures = sorted_district_temperatures[
                                           :10]

            return top_10_district_temperatures

        else:
            return None
