import Weather, PlayMusic, TextToSpeech, Help

class Intents:
    def __init__(self): 
        self.weather = Weather.Weather()
        self.musicPlayer = PlayMusic.PlayMusic()
        self.speaker = TextToSpeech.TextToSpeech()
        self.help = Help.Help()

    def performAction(self, data):
        intent = None
        
        if type(data) is not str:
            intent = data["intent"]
        else:
            intent = data

        if intent == "PlayMusic":
            song = data["entities"].fields["song"].string_value
            self.speaker.say("Alright, here's " + song)
            self.musicPlayer.play(song)

        elif intent == "GetWeather":
            msg = self.weather.getWeather()
            self.speaker.say(msg)
        
        elif intent == "ForecastWeather":
            msg = self.weather.getForecast(data["entities"].fields["number"].number_value)
            self.speaker.say(msg)

        elif intent == "StopMusic":
            self.musicPlayer.stop()

        elif intent == "PauseMusic":
            self.musicPlayer.pause(1)
        
        elif intent == "ResumeMusic":
            self.musicPlayer.pause(0)
        
        elif intent == "Help":
            commands = self.help.display()
            print(commands)

        else:
            self.speaker.say(data["response"])