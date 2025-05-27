import requests

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        }
    data = { 
        "raw_document": {
             "text": text_to_analyse 
             } 
        }

    response = requests.post(URL, headers = Headers, json = data)

    if response.status_code == 200 :
        return response.text
    else:
        return {"error":response.status_code, "message":response.text}
