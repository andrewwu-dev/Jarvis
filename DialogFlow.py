import dialogflow_v2 as dialogflow
import Intents

class DialogFlow:
        def detect_intent(self, text):
                session_client = dialogflow.SessionsClient()

                session = session_client.session_path("newagent-3a903", "1")
                print ('Session path: {}\n'.format(session))
                        
                text_input = dialogflow.types.TextInput(text=text, language_code="en")

                query_input = dialogflow.types.QueryInput(text=text_input)

                response = session_client.detect_intent(
                        session=session, query_input=query_input)

                print('=' * 20)
                print('Query text: {}'.format(response.query_result.query_text))
                print('Detected intent: {} (confidence: {})\n'.format(
                        response.query_result.intent.display_name,
                        response.query_result.intent_detection_confidence))
                print('Fulfillment text: {}\n'.format(
                        response.query_result.fulfillment_text))
                norm = {
                        "entities": response.query_result.parameters,
                        "intent": response.query_result.intent.display_name,
                        "confidence": response.query_result.intent_detection_confidence
                }
                return norm

#res = DialogFlow().detect_intent("play sparks fly")
#song = res['entities'].fields['song'].string_value
#Intents.intentMap[res['intent']].play(song)
