#weather backend
import geocoder
import requests
import pprint

class Weather:
    def __init__(self):
        keyFile = open('weatherKey.txt', 'r')
        if keyFile.mode == 'r':
            self.key = keyFile.read()
        assert self.key

        self.url = "http://api.openweathermap.org/data/2.5/weather"
        self.ip = geocoder.ip('me')
        
        self.params = {
            "lat": self.ip.lat,
            "lon": self.ip.lng,
            "units": "metric",
            "APPID": self.key
        }
        
        print('initialized Weather')

    def getWeather(self):
        req = requests.get(url=self.url, params=self.params)
        pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(req.json())
        data = req.json()
        #print("-------------")

        weatherInfo = {
            "weather": data["weather"][0]["description"],
            "temperature": round(data["main"]["temp"])
        }

        #pp.pprint(weatherInfo)

        return weatherInfo

if __name__ == "__main__":
    w = Weather()

    w.getWeather()

