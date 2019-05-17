from SpeechRecognition import SpeechRecognition


speechRecognizer = SpeechRecognition()
while(True):
    input("Listening for 'ENTER' key press...")

    speechRecognizer.record()
