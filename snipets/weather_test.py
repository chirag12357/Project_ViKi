import pyowm

owm = pyowm.OWM('ed20b384594e2e2e2881ac85e38dca32')
observation = owm.weather_at_place("Cambridge,uk")
w = observation.get_weather()
wind = w.get_wind()
print(w)
print(wind)
