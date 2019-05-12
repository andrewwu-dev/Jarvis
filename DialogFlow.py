import dialogflow_v2 as dialogflow

def detect_intent(text):
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
    
    normalizeResponse(response.query_result)

def normalizeResponse(res):
    norm = {
        "entities": res.parameters,
        "intent": res.intent.display_name,
        "confidence": res.intent_detection_confidence
    }
    print (norm)
    
detect_intent("Jarvis, play sparks fly")