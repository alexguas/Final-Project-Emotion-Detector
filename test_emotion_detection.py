{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 """\
Unit tests for the emotion detector.\
"""\
\
import unittest\
from EmotionDetection import emotion_detector\
\
\
class TestEmotionDetector(unittest.TestCase):\
    """\
    Test cases for emotion_detector function.\
    """\
\
    def test_emotion_anger(self):\
        """\
        Test for anger detection.\
        """\
        result = emotion_detector("I am really mad about this")\
        self.assertEqual(result["dominant_emotion"], "anger")\
\
    def test_emotion_disgust(self):\
        """\
        Test for disgust detection.\
        """\
        result = emotion_detector("I feel disgusted just hearing about this")\
        self.assertEqual(result["dominant_emotion"], "disgust")\
\
    def test_emotion_fear(self):\
        """\
        Test for fear detection.\
        """\
        result = emotion_detector("I am really afraid that this will happen")\
        self.assertEqual(result["dominant_emotion"], "fear")\
\
    def test_emotion_joy(self):\
        """\
        Test for joy detection.\
        """\
        result = emotion_detector("I am glad this happened")\
        self.assertEqual(result["dominant_emotion"], "joy")\
\
    def test_emotion_sadness(self):\
        """\
        Test for sadness detection.\
        """\
        result = emotion_detector("I am so sad about this")\
        self.assertEqual(result["dominant_emotion"], "sadness")\
\
\
if __name__ == "__main__":\
    unittest.main()}