import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import City
from .forms import CityForm

APPID = '8486ae527aa8c0b62ca90626dd1c24f7'
URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + APPID

def index(request):
    cities = City.objects.all()
    all_cities = list()

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm() # clears the form object

    for city in cities:
        responce = requests.get(URL.format(city.name)).json()
        city_info = {
            'city': city.name,
            'id': city.id,
            'temp': responce["main"]["temp"],
            'icon': responce["weather"][0]["icon"]
        }
        all_cities.append(city_info) 

    return render(request, 'weather/index.html', {'all_info': all_cities, 'form': form})

def delete_city(request, pk):
    city = get_object_or_404(City, pk=pk)
    city.delete()
    return redirect('/')