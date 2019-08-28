#weather backend
import requests
import geocoder
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
            "q" : geocoder.ip('me')
        }

    def callAPI(self):
        req = requests.get(url=self.url, params=self.params)
        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(req.json())
        data = req.json()
        #print("-------------")

        weatherInfo = {
            "weather": data["current"]["condition"]["text"],
            "temp": round(data["current"]["temp_c"]),
            "windSpeed": data["current"]["wind_kph"],
            "windDir": data["current"]["wind_dir"]
        }

        #pp.pprint(weatherInfo)

        return weatherInfo
    
    def getWeather(self):
        info = self.callAPI()

        direction = {
            "W": "west",
            "N": "north",
            "S": "south",
            "E": "east",
            "NW": "north-west",
            "NE": "north-east",
            "SE": "south-east",
            "SW": "south-west",
            "NNW": "north north-west",
            "WNW": "west north-west",
            "WSW": "west south-west",
            "SSW": "south south-west",
            "SSE": "south south-east",
            "ESE": "east south-east",
            "ENE": "east north-east",
            "NNE": "north north-east"
        }
        msg = "Today is " + str(info["temp"]) + " degrees and the weather condition for today is " 
        msg += info["weather"] + ". The wind speed is " + str(info["windSpeed"]) + " kilometers per hour "
        msg += direction[info["windDir"]]
        return msg

if __name__ == "__main__":
    w = Weather()

    w.getWeather()

