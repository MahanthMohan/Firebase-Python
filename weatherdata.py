from firebase import firebase
import requests
import json

class weatherdata:

    def geturl(self):
        f = open("url.txt", "r")
        url = f.read().replace("db_url: ","")
        return url

    def getTempData(self, location):
        self.location = location
        request_url = 'http://api.openweathermap.org/data/2.5/weather?appid=a82ce5d667628af3985ec52d8a1a91eb&q={}'.format(location)
        data = requests.get(request_url).json()['main']
        temp = round(data['temp'], 2) - 273
        return temp


    def writeData(self, message):
        self.message = message
        with open("data.json") as file:
            weather_data = json.load(file)['weather'][0]
            temp = weather_data['temp']
            temp.append(temp)
        database.post('/SunnyvaleTempData/', temp)

    def readData(self):
        data = database.get('/SunnyvaleTempData/', None)
        return data


wt = weatherdata()

database = firebase.FirebaseApplication(wt.geturl(), None)
wt.writeData(wt.getTempData())
print(wt.readData())