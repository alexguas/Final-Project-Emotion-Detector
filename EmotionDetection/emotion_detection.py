{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 """\
Emotion detection module.\
"""\
\
import requests\
\
\
def emotion_detector(text_to_analyse):\
    """\
    Analyze emotions in the provided text using Watson NLP API.\
    """\
    if text_to_analyse is None or text_to_analyse.strip() == "":\
        return \{\
            "anger": None,\
            "disgust": None,\
            "fear": None,\
            "joy": None,\
            "sadness": None,\
            "dominant_emotion": None\
        \}\
\
    url = (\
        "https://sn-watson-emotion.labs.skills.network/"\
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"\
    )\
\
    headers = \{\
        "grpc-metadata-mm-model-id":\
        "emotion_aggregated-workflow_lang_en_stock"\
    \}\
\
    input_json = \{\
        "raw_document": \{\
            "text": text_to_analyse\
        \}\
    \}\
\
    response = requests.post(url, json=input_json, headers=headers, timeout=10)\
\
    if response.status_code == 400:\
        return \{\
            "anger": None,\
            "disgust": None,\
            "fear": None,\
            "joy": None,\
            "sadness": None,\
            "dominant_emotion": None\
        \}\
\
    formatted_response = response.json()\
    emotions = formatted_response["emotionPredictions"][0]["emotion"]\
\
    anger = emotions["anger"]\
    disgust = emotions["disgust"]\
    fear = emotions["fear"]\
    joy = emotions["joy"]\
    sadness = emotions["sadness"]\
\
    dominant_emotion = max(emotions, key=emotions.get)\
\
    return \{\
        "anger": anger,\
        "disgust": disgust,\
        "fear": fear,\
        "joy": joy,\
        "sadness": sadness,\
        "dominant_emotion": dominant_emotion\
    \}}