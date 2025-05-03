import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

class IntentClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = MultinomialNB()

    def train(self, csv_path):
        df = pd.read_csv(csv_path)
        X = self.vectorizer.fit_transform(df['text'])
        y = df['intent']
        self.model.fit(X, y)
        with open("model.pkl", "wb") as f:
            pickle.dump((self.vectorizer, self.model), f)

    def predict(self, text):
        with open("model.pkl", "rb") as f:
            self.vectorizer, self.model = pickle.load(f)
        X = self.vectorizer.transform([text])
        return self.model.predict(X)[0]
