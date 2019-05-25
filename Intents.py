import Weather, PlayMusic, TextToSpeech

class Intents:
    def __init__(self): 
        self.weather = Weather.Weather()
        self.musicPlayer = PlayMusic.PlayMusic()
        self.speaker = TextToSpeech.TextToSpeech()   

    def performAction(self, data):
        intent = data["intent"]

        if intent == "PlayMusic":
            song = data["entities"].fields["song"].string_value
            self.speaker.say("Alright, here's " + song)
            self.musicPlayer.play(song)

        elif intent == "GetWeather":
            msg = self.weather.getWeather()
            self.speaker.say(msg)
            
        else:
            print (data["response"])
