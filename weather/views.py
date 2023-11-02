from django.shortcuts import render
import json
import urllib.request


# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST["city"]
        res = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=7ae2f72dbbf6c93be7b4b74afb6e3004").read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data["sys"]["country"]),
            "coordinates": str(json_data["coord"]["lon"]) + ' ' + str(json_data["coord"]["lat"]),
            "temperature": str(round((json_data["main"]["temp"])-273.15)) + 'C',
            "temperature_feels_like": str(round(json_data["main"]["feels_like"]-273.15)) + 'C',
            "temperature_min": str(round(json_data["main"]["temp_min"] - 273.15)) + 'C',
            "temperature_max": str(round(json_data["main"]["temp_max"] - 273.15)) + 'C',
            "wind_speed": str(json_data["wind"]["speed"]) + ' m/s',
            "weather": str(json_data["weather"][0]["description"]),
            "humidity": str(json_data["main"]["humidity"]) + ' %',
        }
    else:
        city = ""
        data = {}
    return render(request, "index.html", {"city": city, "data": data})