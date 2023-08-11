from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    print(f"Searching for name: {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    print(f"Finding wikipedia summary for name: {name}")
    return wikipedia.summary(name)


def get_textBlob(text):
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Find Wikipedia name and return back key phrases"""
    text = summarize_wikipedia(name)
    blob = get_textBlob(text)
    phrases = blob.noun_phrases
    return phrases
