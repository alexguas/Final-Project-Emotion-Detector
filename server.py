{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 """\
Flask server for the Emotion Detection application.\
"""\
\
from flask import Flask, render_template, request\
from EmotionDetection import emotion_detector\
\
app = Flask("Emotion Detector")\
\
\
@app.route("/")\
def render_index_page():\
    """\
    Render the main application page.\
    """\
    return render_template("index.html")\
\
\
@app.route("/emotionDetector")\
def sent_detector():\
    """\
    Detect emotion for the provided text and return formatted output.\
    """\
    text_to_analyze = request.args.get("textToAnalyze")\
\
    response = emotion_detector(text_to_analyze)\
\
    if response["dominant_emotion"] is None:\
        return "Invalid text! Please try again!"\
\
    return (\
        "For the given statement, the system response is "\
        f"'anger': \{response['anger']\}, "\
        f"'disgust': \{response['disgust']\}, "\
        f"'fear': \{response['fear']\}, "\
        f"'joy': \{response['joy']\} and "\
        f"'sadness': \{response['sadness']\}. "\
        f"The dominant emotion is \{response['dominant_emotion']\}."\
    )\
\
\
if __name__ == "__main__":\
    app.run(host="0.0.0.0", port=5000)}