#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from geopy.geocoders import Nominatim
locator = Nominatim(user_agent='myGeocoder')
location = locator.geocode('Пуровский район, Ямало-Ненецкий автономный округ, Уральский федеральный округ, Россия')
print('Latitude = {}, Longitude = {}'.format(location.latitude, location.longitude))


# In[ ]:


import csv
import pandas as pd
from geopy.geocoders import Nominatim
count = 0
with open(r'C:\Users\admin\Desktop\geo_data\in.csv', 'r', encoding="Windows-1251") as fr:
    with open(r'C:\Users\admin\Desktop\geo_data\out.txt', 'w', encoding="utf-8") as fw:
        for line in fr:
            print(line)
            locator = Nominatim(user_agent='myGeocoder')
            location = locator.reverse(line)
            if count < 5 :
                #fw.write(line[:-1].replace('"','')+'\r\n')
                #fw.write(line[:-1].replace('"','')+'\n')
                sep = '|'
                result = [location.address,sep,line]
                fw.writelines("%s\n" % result)
                count = count + 1
            else:
                print("The End")


# In[ ]:


from geopy.geocoders import Nominatim
locator = Nominatim(user_agent='myGeocoder')
location = locator.reverse('28.9792,41.1003')
country_new = location.raw['address']['country'].upper()
city = location.raw['address']
print(city)


# In[ ]:


from geopy.geocoders import Nominatim
import csv
import pandas as pd


def get_countries(lat,lon):
    coordinates = f'{lat} {lon}'
    locator = Nominatim(user_agent='myGeocoder', timeout=10)
    #location = locator.reverse(coordinates)
    location = locator.reverse(coordinates,language='ru')
    #country = location.raw['address']['country_code'].upper()
    country = location.address.upper()
    city = location.raw['address']['country'].upper()
    type_n = "y_x"
    #location = locator.reverse('41.3490;140.2598')
    return [city,type_n,lat,lon,country]

type_t = "y_x"
error = "address must not be None"
with open(r'C:\Users\admin\Desktop\geo_data\in.csv', 'r' , encoding="Windows-1251") as fr:
    with open(r'C:\Users\admin\Desktop\geo_data\out.txt', 'w', encoding="utf-8") as fw:
        for line in fr:
            lat = line.split(',')[:-1]
            lat = str(lat)
            lat = lat.replace('[','')
            lat = lat.replace(']','')
            lat = lat.replace("'",'')
            lon = line.replace('\n','').split(',')[1:]
            lon = str(lon)
            lon = lon.replace('[','')
            lon = lon.replace(']','')
            lon = lon.replace("'",'')
            try:
                result = get_countries(lat,lon)
                fw.writelines("%s\n" % result)
            except Exception:
                export_data = [error,type_t,lat,lon]
                export_data = str(export_data)
                fw.writelines("%s\n" % export_data)

