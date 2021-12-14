import main
import os

from configparser import ConfigParser
from flask import Flask, request, Response
from sklearn.metrics.pairwise import cosine_similarity

#reading config to get get corpus documents
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
config_object = ConfigParser()
config_object.read(os.path.join(__location__, "config.ini"))
PATH = os.path.join(__location__,config_object["PROD"]["PATH"])

# creating a Flask app
application = app = Flask(__name__)

# Process and load objects in memory outside of API call for faster response time
try:
    df_catalogue, vectorizer, vectorized_catalauge = main.vectorize(PATH)
except Exception as e:
    print(f"Unexpected {e=}, {type(e)=}")
    raise 

@app.route('/', methods = ['GET'])
def home():
    return "OK", 200

@app.route('/search', methods = ['GET'])
def text_search(n=10):

    #get query parameters
    param = request.args.get('ntop-results')
    if param is not None:
        n = int(param)

    input_text = request.args.get('text')
    if input_text is None:
        return Response('Text to search not provided', 400)

    #get cosine similarity score and apped it to df
    query = vectorizer.transform([input_text])
    df_catalogue['score'] = cosine_similarity(vectorized_catalauge,query).reshape((-1,))

    return df_catalogue.iloc[df_catalogue['score'].argsort()[-1*(n):][::-1],:].to_json(orient='records')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)