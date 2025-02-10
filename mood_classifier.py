# app/mood_classifier.py
from textblob import TextBlob

def classify_mood(text):
    """
    Classify the user's mood based on input text using sentiment analysis.
    """
    sentiment = TextBlob(text).sentiment.polarity
    mood = "neutral"
    
    if sentiment > 0.2:
        mood = "happy"
    elif sentiment < -0.2:
        mood = "sad"
    else:
        mood = "neutral"
    
    return mood