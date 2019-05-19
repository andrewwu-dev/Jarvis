from SpeechRecognition import SpeechRecognition
import Intents, DialogFlow

speechRecognizer = SpeechRecognition()
while(True):
    input("Listening for 'ENTER' key press...")

    speech = speechRecognizer.record()
    if (speech != ''):
        res = DialogFlow.DialogFlow().detect_intent(speech)
        song = res['entities'].fields['song'].string_value
        Intents.intentMap[res['intent']].play(song)