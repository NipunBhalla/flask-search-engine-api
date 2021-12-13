import json
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize(catalogue_path):
    catalogue = [json.loads(line) for line in open(catalogue_path, 'r')]
    df_catalogue = pd.DataFrame(catalogue)
    vectorizer = TfidfVectorizer()
    vectorized_catalauge = vectorizer.fit_transform(df_catalogue['text'])

    return df_catalogue, vectorizer, vectorized_catalauge
     

if __name__ == "__main__":
    vectorize('product_title.json')