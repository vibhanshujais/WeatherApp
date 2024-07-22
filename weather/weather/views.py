from django.shortcuts import render, redirect
from django.http import HttpResponse
import urllib.request
import json

def weather(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        try:
            if city is not None:
                source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=ff11f6267007d54a213b35cfd38cb37b').read() 
                list_of_data =  json.loads(source)
                data = { 
                "country_code": str(list_of_data['sys']['country']), 
                "coordinate": str(list_of_data['coord']['lon']) + ' '
                            + str(list_of_data['coord']['lat']), 
                "temp": str(list_of_data['main']['temp']) + 'k', 
                "pressure": str(list_of_data['main']['pressure']), 
                "humidity": str(list_of_data['main']['humidity']), 
                } 
                return render(request, 'index.html', {'key':data})
        except Exception as e:
            return render(request, 'index.html', {'er':e})
    return render(request, 'index.html')