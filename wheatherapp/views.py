import urllib.request 
import json 
from django.shortcuts import render # type: ignore
from urllib import *

# Create your views here.

from urllib import *

def index(request):
    if request.method=='POST':
        city=request.POST['city']
        
        source=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=f75e2eabaadd0a5800c6cfde4dfaae9a').read()
        list_of_data=json.loads(source)
        
        data= {
            "countrycode":str(list_of_data['sys']['country']),
            "coordinate":str(list_of_data['coord']['lon'])+', '
            +str(list_of_data['coord']['lat']),
            "temp":str(list_of_data['main']['temp']) + '°C',
            "pressure":(list_of_data['main']['pressure']),
            "humidity":(list_of_data['main']['humidity']),
            "main":str(list_of_data['weather'][0]['main']),
            "description":str(list_of_data['weather'][0]['description']),
            "icon":list_of_data['weather'][0]['icon'],
                
        }
        print(data)
    else:
        data={}
    return render(request,'main/index.html',data)
def hello(request,*args,**argv):
    return render(request,'main/hello.html',status=500)
def hai(request,exception):
    return render(request,'main/hai.html')