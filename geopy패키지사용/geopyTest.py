from geopy.geocoders import Nominatim # geopy패키지에서 geocoders로 들어가서 Nominatim를 가져와라

geolocator = Nominatim(user_agent="LeeJooHeon")
location = geolocator.geocode("Seoul, South Korea")
print(location)