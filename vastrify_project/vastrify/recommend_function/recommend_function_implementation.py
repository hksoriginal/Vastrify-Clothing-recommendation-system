import json
import pickle
import re

from django.http import JsonResponse
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the CountVectorizer with a maximum of 5000 features and using English stop words
vec = CountVectorizer(max_features=5000, stop_words='english')


class RecommendFunction:
    @staticmethod
    def clean_text(text: str) -> str:
        # Initialize the WordNetLemmatizer for lemmatization
        lemmatizer = WordNetLemmatizer()

        # Remove non-alphabetic characters from the text
        cleaned_text = re.sub('[^a-zA-Z]', ' ', text)

        # Convert the text to lowercase
        cleaned_text = cleaned_text.lower()

        # Split the text into individual words
        cleaned_text = cleaned_text.split()

        # Lemmatize the words and remove stop words
        cleaned_text = [
            lemmatizer.lemmatize(word)
            for word in cleaned_text
            if not word in stopwords.words('english')
        ]

        # Join the cleaned words back into a string
        return ' '.join(cleaned_text)

    def recommend_clothes(self, text: str, top_num: int):
        # Load the clothing DataFrame from the pickled file
        clothing_df = pickle.load(open('vastrify/recommend_function/clothing_df.pkl', 'rb'))

        # Clean the input text using the clean_text() method
        cleaned_text = self.clean_text(text)

        # Convert the cleaned text into a Pandas Series
        cleaned_text_as_series = pd.Series([cleaned_text])

        # Get the descriptions column from the clothing DataFrame
        descriptions = clothing_df['cleaned_description']

        # Concatenate the descriptions column with the cleaned text as a new row
        description_with_new_text = pd.concat([descriptions, cleaned_text_as_series]).reset_index(drop=True)

        # Vectorize the descriptions using CountVectorizer and convert it to an array
        # vectors = cv.fit_transform(description_with_new_text).toarray()
        vectors = vec.fit_transform(description_with_new_text).toarray()

        # Calculate the cosine similarity scores between the vectors
        similarity_scores = cosine_similarity(vectors)

        # Get the index of the input description in the combined DataFrame
        input_description_index = description_with_new_text[description_with_new_text == cleaned_text].index[0]

        # Get the similarity scores for the input description
        distances = similarity_scores[input_description_index]

        # Sort the clothing items based on similarity scores and get the top N recommendations
        clothing_items_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:int(top_num) + 1]

        # Get the details of the recommended clothing items as dictionaries
        clothing_item_details = [(clothing_df.iloc[each[0]]).to_dict() for each in clothing_items_list]

        # Exclude the input description from the original descriptions
        descriptions = descriptions[descriptions != cleaned_text]

        # Return the details of the recommended clothing items
        return clothing_item_details
