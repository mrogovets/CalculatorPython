"""Doc."""


from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


# ---------- FREE API KEY examples ---------------------

owm = OWM('16fbeb8b0b596e1f5a5c629b77a45183')
mgr = owm.weather_manager()

place = input("What state/city: ")


# Search for current weather in London (Great Britain) and get details
# observation = mgr.weather_at_place('London,GB')
observation = mgr.weather_at_place(place)
w = observation.weather

print("In " + place + " now " + str(w.temperature('celsius')["temp"]) +
      " celsius degree and " + str(w.detailed_status))
if w.temperature('celsius')["temp"] < 10:
    print("Put on worm clothes")
elif w.temperature('celsius')["temp"] < 20:
    print("Now is cold")
else:
    print("Temperature is norm")
