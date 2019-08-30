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

    def getForecast(self, days):
        if (int(days) > 10):
            return "Sorry, forecast has a maximum range of 10 days"
        
        req = requests.get(url="http://api-cdn.apixu.com/v1/forecast.json?", params={"key" : self.key, "q": geocoder.ip('me'), "days": int(days)})
        data = req.json()

        forecastInfo = {
            "date": data["forecast"]["forecastday"][int(days) - 1]["date"],
            "high": data["forecast"]["forecastday"][int(days) - 1]["day"]["maxtemp_c"],
            "low": data["forecast"]["forecastday"][int(days) - 1]["day"]["mintemp_c"],
            "avg": data["forecast"]["forecastday"][int(days) - 1]["day"]["avgtemp_c"],
            "wind": data["forecast"]["forecastday"][int(days) - 1]["day"]["maxwind_kph"],
            "precip": data["forecast"]["forecastday"][int(days) - 1]["day"]["totalprecip_mm"],
            "condition": data["forecast"]["forecastday"][int(days) - 1]["day"]["condition"]["text"]
        }
        print (forecastInfo)
        msg = "The weather condition for " + str(forecastInfo["date"]) + " is " + str(forecastInfo["condition"])
        msg += " The average temperature is " + str(forecastInfo["avg"]) + " degrees celsius. "
        msg += " With a high of " + str(forecastInfo["high"]) + " and low of " + str(forecastInfo["low"]) + " degrees celsius. "
        msg += " Wind speed reaches a high of " + str(forecastInfo["wind"]) + " kilometers per hour"
        msg += " and total precipitation is expected to be " + str(forecastInfo["precip"]) + " millimeters."
        return msg

if __name__ == "__main__":
    w = Weather()

    w.getWeather()

