from SpeechRecognition import SpeechRecognition
import Intents, DialogFlow

speechRecognizer = SpeechRecognition()
intents = Intents.Intents()
dialogFlow = DialogFlow.DialogFlow()

while(True):
    input("Listening for 'ENTER' key press...")
    intents.performAction("PauseMusic")
    speech = speechRecognizer.record()

    if speech != "":
        res = dialogFlow.detect_intent(speech)
        intents.performAction(res)
    
    intents.performAction("ResumeMusic")
