import asyncio

from open_meteo import OpenMeteo
from open_meteo.models import DailyParameters, HourlyParameters

# The latitude and longitude are the location of the greenhouse
async def main():
    async with OpenMeteo() as open_meteo:
        forecast = await open_meteo.forecast(
            latitude=60.63,
            longitude=26.31,
            current_weather=True,
            daily=[
                DailyParameters.SUNRISE,
                DailyParameters.SUNSET,
            ],
            hourly=[
                HourlyParameters.TEMPERATURE_2M,
                HourlyParameters.RELATIVE_HUMIDITY_2M,
            ],
        )
        print(forecast)


if __name__ == "__main__":
    asyncio.run(main())