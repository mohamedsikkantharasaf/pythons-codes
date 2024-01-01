import phonenumbers
import folium

from phonenumbers import geocoder

key = '7b2aeb0cd6aa44b69e9baec8c625791e'

myNumber = input("enter the phone number : ")

phnumbers = phonenumbers.parse(myNumber)

yourLocation = geocoder.description_for_number(phnumbers, "en")
print(yourLocation)

# get service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(myNumber)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourLocation)

result = geocoder.geocode(query)
# print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print("latitude--longitude")
print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

# save map in html file
myMap.save("myLocation.html")
