import requests
from django.shortcuts import render

APPID = '8486ae527aa8c0b62ca90626dd1c24f7'

def index(request):
    city='Busan'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={APPID}'
    
    responce = requests.get(url).json()
    
    city_info = {
        'city': city,
        'temp': responce["main"]["temp"],
        'icon': responce["weather"][0]["icon"]
    }

    return render(request, 'weather/index.html', {'info': city_info})