
import sys
sys.stdout.reconfigure(encoding='utf-8')
import phonenumbers
from phonenumbers import geocoder
import folium
from UserPhoneNumber import num

phnumber = phonenumbers.parse(num)

location = geocoder.description_for_number(phnumber, "en")

print(location)

from phonenumbers import carrier

service_pro = phonenumbers.parse(num)
print(carrier.name_for_number(service_pro, "en"))

import opencage
from opencage.geocoder import OpenCageGeocode

API_key = "595466c10c6e480685fb732036f0a453"

geocoder = OpenCageGeocode(API_key)
query = str(location)
result = geocoder.geocode(query)

#print(result)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")