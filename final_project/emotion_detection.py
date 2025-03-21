# from final_project.emotion_detection import emotion_detector
# result = emotion_detector("I love this new technology")
# print(result)
import requests
def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data =  { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, headers=header, json=data)

    if response.status_code == 200:
        response_dict = response.json()
        emotions = response_dict['emotionPredictions'][0]['emotion']
        dominant_emotion =  max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion
        return emotions
    else:
        return {"error": f"Request failed with status code {response.status_code}"}