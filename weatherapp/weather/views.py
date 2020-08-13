import requests
from django.shortcuts import render
from .models import City

APPID = '8486ae527aa8c0b62ca90626dd1c24f7'

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + APPID
    
    cities = City.objects.all()
    
    all_cities = list()

    for city in cities:
        responce = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': responce["main"]["temp"],
            'icon': responce["weather"][0]["icon"]
        }
        all_cities.append(city_info)

    return render(request, 'weather/index.html', {'all_info': all_cities})