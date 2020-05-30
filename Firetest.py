from firebase import firebase
import requests

class Firetest:

    def getWeatherData(self, location):
        self.location = location
        request_URL = "http://api.openweathermap.org/data/2.5/weather?appid=a82ce5d667628af3985ec52d8a1a91eb&q={}".format(location)
        return_content = requests.get(request_URL).json()
        temperature = float(return_content['main']['temp']) - 273
        return temperature
    

database = firebase.FirebaseApplication('https://python-realtime-database.firebaseio.com/', None)
Firetest = Firetest()

while True:

    temperature = Firetest.getWeatherData()

    data_to_upload = {
        'Temp' : temperature
    }

    result = database.post("/WeatherData/", data_to_upload)
