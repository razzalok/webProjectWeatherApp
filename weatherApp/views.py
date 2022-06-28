from email import message
from django.shortcuts import render
import requests
import datetime

city = 'Gharuan'

lon = 102
lat = 104


def index(request):
    if 'city' in request.POST:
        if request.POST['city'] == "":
            city = 'Gharuan'
        else:
            city = request.POST['city']

    else:
        city = 'Gharuan'
    appid = 'a14edc84ee129b22c119aaee2bc8d70a'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid': appid, 'units': 'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    pressure = res['main']['pressure']
    humidity = res['main']['humidity']
    clouds = res['clouds']['all']
    country = res['sys']['country']
    lon = res['coord']['lon']
    lat = res['coord']['lat']
    day = datetime.date.today()

    return render(request, 'weatherApp/index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city, 'pressure': pressure, 'humidity': humidity, 'clouds': clouds, 'country': country})


# def dayFive(request):
#     appid = 'a14edc84ee129b22c119aaee2bc8d70a'
#     URL = 'https://api.openweathermap.org/data/2.5/forecast/daily'
#     PARAMS = {'lat': lat, 'lon': lon, 'cnt': 5,
#               'appid': appid, 'units': 'metric'}
#     r = requests.get(url=URL, params=PARAMS)
#     res = r.json()
#     citys = res['city']['name']
#     temp = res['list'][0]['main']['temp']
#     return render(request, 'weatherApp/Day5.html', {'citys': citys, 'temp': temp})
