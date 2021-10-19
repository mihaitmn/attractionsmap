import folium
import pandas

data = pandas.read_csv("Webmap-datasources\Atractii.txt", delimiter=';', skiprows=[0])

lat = list(data["LAT"])
lon = list(data["LON"])
type = list(data["TYPE"])
name = list(data["NAME"])

def color_producer(typeof):
    if typeof==1:
        return "red"
    elif typeof==2:
        return "orange"
    elif typeof==3:
        return "blue"
    elif typeof==4:
        return "green"
    elif typeof==5:
        return "black"
    elif typeof==6:
        return "purple"
    elif typeof==7:
        return "grey"
    elif typeof==8:
        return "yellow"

def return_type(num):
    if num == 1:
        return "Munte"
    elif num==2:
        return "Rezervatie"
    elif num==3:
        return "Apa"
    elif num==4:
        return "Vegetatie"
    elif num==5:
        return "Castel"
    elif num==6:
        return "Atractie istorica"
    elif num==7:
        return "Catedrala"
    elif num==8:
        return "Altele"

map = folium.Map(location=[45.9442858, 25.0094303], zoom_start = 7.5, tiles = "Stamen Terrain")
fgm = folium.FeatureGroup(name = "Munti")
fgr = folium.FeatureGroup(name = "Rezervatii")
fga = folium.FeatureGroup(name = "Ape")
fgv = folium.FeatureGroup(name = "Vegetatie")
fgc = folium.FeatureGroup(name = "Castele")
fgai = folium.FeatureGroup(name = "Atractii istorice")
fgctd = folium.FeatureGroup(name="Catedrale")
fgalt = folium.FeatureGroup(name = "Altele")


for lt, ln, tp, nam in zip(lat, lon, type, name):
    if tp==1:
        fgm.add_child(folium.CircleMarker(location = (lt, ln), radius = 10, popup= str(nam) + ", " + return_type(tp),
        fill_color = color_producer(tp), color="black", fill = True, fill_opacity=0.7))
    elif tp == 2:
        fgr.add_child(folium.CircleMarker(location=(lt, ln), radius=10, popup=str(nam) + ", " + return_type(tp),
                                          fill_color=color_producer(tp), color="black", fill=True, fill_opacity=0.7))
    elif tp == 3:
        fga.add_child(folium.CircleMarker(location=(lt, ln), radius=10, popup=str(nam) + ", " + return_type(tp),
                                          fill_color=color_producer(tp), color="black", fill=True, fill_opacity=0.7))
    elif tp == 4:
        fgv.add_child(folium.CircleMarker(location=(lt, ln), radius=10, popup=str(nam) + ", " + return_type(tp),
                                          fill_color=color_producer(tp), color="black", fill=True, fill_opacity=0.7))
    elif tp == 5:
        fgc.add_child(folium.CircleMarker(location=(lt, ln), radius=10, popup=str(nam) + ", " + return_type(tp),
                                          fill_color=color_producer(tp), color="black", fill=True, fill_opacity=0.7))
    elif tp == 6:
        fgai.add_child(folium.CircleMarker(location=(lt, ln), radius=10, popup=str(nam) + ", " + return_type(tp),
                                          fill_color=color_producer(tp), color="black", fill=True, fill_opacity=0.7))
    elif tp == 7:
        fgctd.add_child(folium.CircleMarker(location=(lt, ln), radius=10, popup=str(nam) + ", " + return_type(tp),
                                          fill_color=color_producer(tp), color="black", fill=True, fill_opacity=0.7))
    elif tp==8:
        fgalt.add_child(folium.CircleMarker(location=(lt, ln), radius=10, popup=str(nam) + ", " + return_type(tp),
                                          fill_color=color_producer(tp), color="black", fill=True, fill_opacity=0.7))

map.add_child(fgm)
map.add_child(fgr)
map.add_child(fga)
map.add_child(fgv)
map.add_child(fgc)
map.add_child(fgai)
map.add_child(fgctd)
map.add_child(fgalt)

map.add_child(folium.LayerControl())

map.save("map.html")