import azure.cognitiveservices.speech as speechsdk

class SpeechRecognition:
    def __init__(self):
        # Creates an instance of a speech config with specified subscription key and service region.
        # Replace with your own subscription key and service region (e.g., "westus").
        speech_key, service_region = "a4d34c6569384d7da15dc9133fe8cfe3", "canadacentral"
        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
        # Creates a recognizer with the given settings
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    def record(self):
        result = self.speech_recognizer.recognize_once()
        
        # Checks result.
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(result.text))
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(result.no_match_details))
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))

