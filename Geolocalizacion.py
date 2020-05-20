from geopy.geocoders import Nominatim
import time
import math
from datetime import datetime
import csv
import folium
import branca

geo= Nominatim(user_agent="MyApp")

lugar = input("Dime un lugar: ")
loc = geo.geocode(lugar)
print (loc)
print ([loc.latitude], [loc.longitude])
naive_dt = datetime.now()
print ("Su hora y dia de consulta fue: ", naive_dt)

datos = [(loc)]
csvsalida = open('Coordenadas6.csv', 'w', newline='')
salida = csv.writer(csvsalida)
salida.writerow(['Ciudad', 'Latitud, Longitud'])
salida.writerows(datos)
csvsalida.close()

mi_mapa = folium.Map(location=(loc.latitude,loc.longitude), zoom_start=8)

marcador1 = folium.Marker(location=(loc.latitude,loc.longitude))


marcador1.add_to(mi_mapa)


mi_mapa.save("mapa3.html")





