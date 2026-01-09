import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    """
    Extracts important keywords (skills/terms) from text.
    """
    doc = nlp(text.lower())
    keywords = set()

    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:
            keywords.add(token.text)

    return keywords
