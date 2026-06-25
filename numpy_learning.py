from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pandas as pd
df = pd.read_csv('spam.csv')
X = df['Message']
Y = df['Category']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
vectorizer.fit(X_train)
X_train = vectorizer.transform(X_train)
X_test = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train, Y_train)

predictions = model.predict(X_test)
print(predictions)
accuracy = accuracy_score(Y_test, predictions)
print(f"Accuracy: {accuracy}")