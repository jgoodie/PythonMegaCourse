# #!/usr/local/bin/python3

import folium, pandas

volcanos = pandas.read_csv("Volcanoes-USA.txt")

def elcolor(elev):
    elmin = int(min(volcanos['ELEV']))
    elincr = int(((max(volcanos['ELEV']) - min(volcanos['ELEV']))/4))
    if elev in range(elmin, elmin+elincr):
        col = 'green'
    elif elev in range(elmin+elincr,elmin+elincr*2):
        col = 'purple'
    elif elev in range(elmin+elincr*2,elmin+elincr*3):
        col = 'orange'
    else:
        col = 'red'
    return(col)

avglat = volcanos.LAT.mean() # or volcanos['LAT'].mean()
avglon = volcanos.LON.mean() # or volcanos['LON'].mean()

### NOTE YOU CAN USE DIFFERENT MAPPING SERVICES
# m = folium.Map(location=[avglat, avglon], zoom_start=5, tiles='Stamen Terrain')
m = folium.Map(location=[avglat, avglon], zoom_start=5, tiles='Mapbox bright')
#fg = feature group
fg=folium.FeatureGroup(name="Volcano Locations")
for name,lat,lon, elev in zip(volcanos['NAME'], volcanos['LAT'],volcanos['LON'], volcanos['ELEV']):
    icolor = elcolor(elev)
    #folium.Marker([lat, lon], popup=name + " " + "Elevation:" + " " + str(elev)+"m", icon = folium.Icon(color = icolor,icon_color='white')).add_to(m)
    fg.add_child(folium.Marker(location=[lat,lon],popup=name, icon=folium.Icon(color=icolor,icon_color='green')))

m.add_child(fg)
m.add_child(folium.GeoJson(data=open('WorldPop.json', encoding='utf-8'), 
                           name='World Population', 
                           style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000<x['properties']['POP2005']<20000000 else 'red'}))
m.add_child(folium.LayerControl())
m.save(outfile='volcanos.html')    
    
# print(volcanos)
# print(volcanos.loc[0:,"NAME":"LON"])
#help
# print(dir(folium))
# 3157 Dallas Ct
#mymap = folium.Map(location=[37.3551, -121.985], zoom_start=16)
#mymap.save('test.html')
#mymap2 = folium.Map(location=[37.3551, -121.985], zoom_start=10, tiles='Stamen Terrain')
#mymap2.save('stamen_map.html')

# Mt. Hood

# mthood = folium.Map(location=[45.372, -121.679], zoom_start=10, tiles='Stamen Terrain')
# # mthood.add_child(folium.Marker(location=[45.372, -121.679], popup='Mt. Hood', icon=folium.Icon(icon_color='white')))
# folium.Marker([45.3288, -121.6625], popup='Mt. Hood Meadows', icon = folium.Icon(icon = 'cloud')).add_to(mthood)
# folium.Marker([45.3311, -121.7113], popup='Timberline Lodge', icon = folium.Icon(color ='green')).add_to(mthood)
# folium.Marker([45.3300, -121.6823], popup='Some Other Location', icon = folium.Icon(color ='red')).add_to(mthood)
# mthood.save('mthood.html')




