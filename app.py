import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif elevation < 1800:
        return "red"
    elif elevation < 2500:
        return "orange"
    else:
        return "blue"

map = folium.Map(location = [29.860394, 77.888817], zoom_start = 6)

fgv = folium.FeatureGroup(name = "Volcanoes")

for lt ,ln, el in zip(lat , lon, elev):
    fgv.add_child(folium.CircleMarker(location = [lt, ln],radius = 6, popup = "Elevation: " + str(el) + "m",
    fill_color = color_producer(el), color = "grey", fill_opacity = 0.7))

fgp = folium.FeatureGroup("Population")

fgp.add_child(folium.GeoJson(data = open("world.json", "r", encoding= "utf-8-sig").read(),
style_function = lambda x : {"fillColor" : "green" if x["properties"]["POP2005"] < 10000000
else "orange" if 10000000 <= x["properties"]["POP2005"] <= 20000000 else "red"}))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl()) #For the laye control

map.save("Map1.html")