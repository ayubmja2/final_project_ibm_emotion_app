import requests
import json

def emotion_detector(text_to_analyse):
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header ={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_data = { "raw_document": { "text": text_to_analyse } }

    res = requests.post(URL, json = json_data, headers= header)
    format_res = json.loads(res.text)
    
   
    #for testing to force a fail. check the response code for the elif and if statments to print out the formt_res NONE values: 
  
    if res.status_code == 200:
        return format_res
    elif res.status_code == 400:
        format_res = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None           
        }
        return format_res

def emotion_predictor(detected_text):
    if all(value is None for value in detected_text.values()):
        return detected_text
    if(detected_text['emotionPredictions'] is not None):
        emotions = detected_text['emotionPredictions'][0]['emotion']
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        max_emotion = max(emotions, key=emotions.get)

        format_emotion_dictionary = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': max_emotion
        }
        return format_emotion_dictionary
