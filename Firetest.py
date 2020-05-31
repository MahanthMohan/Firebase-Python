from firebase import firebase
import json

class Firetest:

    def geturl(self):
        f = open("url.txt", "r")
        url = f.read().replace("db_url: ","")
        return url

    def getInput(self):
        while True:
            data = str("Message: ")
            return data


    def writeData(self, message):
        self.message = message
        with open("data.json") as file:
            data_list = json.load(file)['Messages'][0]
            datapoints = data_list['contents']
            datapoints.append(message)
        database.post('/WeatherData/', datapoints)

    def readData(self):
        data = database.get(Firetest.readData())
        return data


Firetest = Firetest()

database = firebase.FirebaseApplication(Firetest.geturl(), None)
Firetest.writeData(Firetest.getInput())