import Weather, PlayMusic

class Intents:
    def __init__(self): 
        self.weather = Weather.Weather()
        self.musicPlayer = PlayMusic.PlayMusic()   

    def performAction(self, data):
        intent = data["intent"]

        if intent == "PlayMusic":

            song = data["entities"].fields["song"].string_value
            self.musicPlayer.play(song)

        elif intent == "GetWeather":
            msg = self.weather.getWeather()
            print(msg)
