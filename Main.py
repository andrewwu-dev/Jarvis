from SpeechRecognition import SpeechRecognition
import DialogFlow

speechRecognizer = SpeechRecognition()
while(True):
    input("Listening for 'ENTER' key press...")

    speechRecognizer.record()
    