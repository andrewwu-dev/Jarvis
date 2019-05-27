#weather backend
import requests
import pprint

class Weather:
    def __init__(self):
        keyFile = open('weatherKey.txt', 'r')
        if keyFile.mode == 'r':
            self.key = keyFile.read()
        assert self.key

        self.url = "https://api.apixu.com/v1/current.json?"
        
        self.params = {
            "key" : self.key,
            "q" : "auto:ip"
        }

    def callAPI(self):
        req = requests.get(url=self.url, params=self.params)
        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(req.json())
        data = req.json()
        #print("-------------")

        weatherInfo = {
            "weather": data["current"]["condition"]["text"],
            "temp": round(data["current"]["temp_c"])
        }

        #pp.pprint(weatherInfo)

        return weatherInfo
    
    def getWeather(self):
        info = self.callAPI()

        msg = "Today is " + str(info["temp"]) + " degrees and the weather condition for today is " 
        msg += info["weather"] 

        return msg

if __name__ == "__main__":
    w = Weather()

    w.getWeather()

