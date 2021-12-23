# Document Search Engine

Flask API which takes a text input and returns the most relevant documents.

## Installation
To run the code locally, clone the repo and run the following commands.

```bash
cd flask-search-engine-api
python application.py --port 5000
```
By default, the API endpoint is "/search"

## Usage
The API accepts GET requests and requires 2 query parameters: 

| param |  Description |
| ------ | ------ |
| text | The text input by the user to be search in the corpus |
| ntop-results | The number of results to be returned. Default is 10 |

```
localhost:5000/search?text=Womens%20boots&ntop-results=5
```

## Response
API returns a JSON object with text, document id and similarity score. Similarity score ranges from 0-1, where 0 mean no match and 1 means exact match.

```json
[
  {
    "text": "Women's Classic Tall Boots Black 5M",
    "id": "13fe5c9fc92b75705a29533802d83f4d6f69aef7",
    "score": 0.4981161577
  }
]
```

## What could be done differently.
Right now the document corpus is part of the app directory but in real production scenarios, it should be stored either in Cloud Buckets or a Database. This way corpus could also be updated independenlty of the application.


## License
[MIT](https://choosealicense.com/licenses/mit/)
