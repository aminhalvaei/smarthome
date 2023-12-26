from datetime import timedelta

# Its the duration that a weather condition is valid
# so it does not need to make an new api call to get weather
WEATHER_VALID_DURATION = timedelta(milliseconds=5000)
