# Vastrify Clothing Recommendation System
## App Link : https://vastrify-jpixwhuqja-el.a.run.app/home/
[![Vastrify: Clothing Recommendation System - Project Demo](https://img.youtube.com/vi/xD0EJ69NpiA/0.jpg)](https://www.youtube.com/watch?v=xD0EJ69NpiA)


![image](https://github.com/hksoriginal/Vastrify-Clothing-recommendation-system/assets/44989568/b4167e77-3558-46a2-bdfc-db1de738f1ae)
![image](https://github.com/hksoriginal/Vastrify-Clothing-recommendation-system/assets/44989568/1dcd913e-76e1-4125-a1aa-6999abe015f3)
![image](https://github.com/hksoriginal/Vastrify-Clothing-recommendation-system/assets/44989568/5ab541ab-603e-4ef4-be25-74e8e5341840)


Vastrify is a clothing recommendation system designed to provide personalized clothing suggestions based on user preferences and various other factors. This repository contains the source code and resources for the Vastrify Clothing Recommendation System.

# Dataset Preparation

To train the recommendation system, a dataset of various clothing items for men and women was prepared through web scraping from e-commerce websites like Flipkart and Amazon. The dataset includes textual descriptions of the clothing items.

## Data Preprocessing

Before training the recommendation system, the textual data from the dataset undergoes several preprocessing steps:

1. Convert the text to lowercase.
2. Remove stopwords to eliminate common words that do not carry much meaning.
3. Tokenize the text to split it into individual words.
4. Lemmatize the words to reduce them to their base form.
5. Remove special characters to clean the text further.

These preprocessing steps help to normalize the textual data and remove noise.

## Writing Recommendation Function

The recommendation function in the code performs the following steps:

1. Clean the text input given by the user and add it to the dataset.
2. Convert the textual descriptions in the dataset to vectors using the bag-of-words technique.
3. Calculate the similarity score between the user input vector and the vectors of clothing items using cosine similarity.
4. Recommend the top clothing items with the highest similarity scores to the user.

These steps ensure that the recommendation system provides relevant clothing suggestions based on the user's input.


## Features

- Personalized clothing recommendations
- User preference customization
- Machine learning algorithms for enhanced recommendations

## Installation

Clone the repository:

```bash
git clone https://github.com/hksoriginal/Vastrify-Clothing-recommendation-system.git
