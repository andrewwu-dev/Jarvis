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

                norm = {
                        "entities": response.query_result.parameters,
                        "intent": response.query_result.intent.display_name,
                        "confidence": response.query_result.intent_detection_confidence,
                        "response": response.query_result.fulfillment_text
                }
                return norm
