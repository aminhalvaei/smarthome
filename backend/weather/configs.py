from datetime import timedelta

# Its the duration that a weather condition is valid
# so it does not need to make an new api call to get weather
WEATHER_VALID_DURATION = timedelta(milliseconds=5000)

UNITS_OF_MEASUREMENT = "metric"

SETABLE_PARAMETERS = ["temp", "humidity",]

CONSTANT_URL = "https://api.openweathermap.org/data/2.5/weather"

# Here is a list of available api keys from
# openweathermap.org
WEATHER_API_KEYS = [
    "46eb760d100fb6baef9ac0517c1123d8",
]
