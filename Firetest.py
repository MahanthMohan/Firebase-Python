from firebase import firebase
import json

class Firetest:

    def geturl(self):
        f = open("url.txt", "r")
        url = f.read().replace("db_url: ","")
        return url

    def getInput(self):
        data = str("Message: ")
        return data

    def writeData(self, message):
        self.message = message
        with open("data.json") as file:
            msg_list = json.load(file)['Messages'][0]
            contents = msg_list['contents']
            contents.append(message)
        database.post('/MyMessages/', contents)

    def readData(self):
        data = database.get('/MyMessages', None)
        return data


Firetest = Firetest()

database = firebase.FirebaseApplication(Firetest.geturl(), None)
Firetest.writeData(Firetest.getInput())
print(Firetest.readData())