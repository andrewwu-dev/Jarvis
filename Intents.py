import Weather, PlayMusic

weather = Weather.Weather()
playMusic = PlayMusic.PlayMusic()

intentMap = {
    "weather": weather,
    "playMusic": playMusic
}

intentMap['weather']