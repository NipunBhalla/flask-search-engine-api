import main

from configparser import ConfigParser
from flask import Flask, request
from sklearn.metrics.pairwise import cosine_similarity

#reading config
config_object = ConfigParser()
config_object.read("config.ini")
PATH = config_object["PROD"]["PATH"]

# creating a Flask app
app = Flask(__name__)

# Process an load objects in memory outside of API call for faster response time
df_catalogue, vectorizer, vectorized_catalauge = main.vectorize(PATH)

@app.route('/search', methods = ['GET'])
def text_search(n=10):
    param = request.args.get('ntop-results')
    if param is not None:
        n = int(param)

    input_text = request.args.get('text')

    query = vectorizer.transform([input_text])
    df_catalogue['score'] = cosine_similarity(vectorized_catalauge,query).reshape((-1,))

    return df_catalogue.iloc[df_catalogue['score'].argsort()[-1*(n):][::-1],:].to_json(orient='records')

if __name__ == "__main__":
    app.run(host='0.0.0.0')