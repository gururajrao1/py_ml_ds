import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from textblob import TextBlob

# Read the data from a CSV file
file_path = r'C:\Users\gurur\OneDrive\Documents\python\code\Test.csv'
data = pd.read_csv(file_path)

# Check if the required columns exist in the DataFrame
if 'review' in data.columns and 'label' in data.columns:
    # Extract reviews and labels
    reviews = data['review'].tolist()
    labels = data['label'].tolist()
else: 
    raise ValueError("CSV file must contain 'review' and 'label' columns.")

# (Optional) Correct any spelling mistakes in the reviews using TextBlob
corrected_reviews = [str(TextBlob(review).correct()) for review in reviews]

# Convert the text data into numerical format using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corrected_reviews)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Create a Naive Bayes classifier
model = MultinomialNB()

# Train the model
model.fit(X_train, y_train)

# Use the trained model to make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy
print("Accuracy:", accuracy)

if accuracy > 0.5:
    print("The vibes are great, book the tickets!")
else:
    print("The vibes are iffy")