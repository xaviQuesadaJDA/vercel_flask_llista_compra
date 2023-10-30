from flask import Flask, request, jsonify

app = Flask('llista_compra')

articles = []


@app.route('/article/<int:article_id>',
           methods=['GET', 'POST', 'PUT', 'DELETE'])
def article(article_id=0):
  global articles
  if request.method == 'GET':
    return jsonify(articles[article_id])
  elif request.method == 'POST':
    article = {
        'id': len(articles),
        'nom': request.json['nom'],
        'quantitat': request.json['quantitat']
    }
    articles.append(article)
    return jsonify(article), 201
  elif request.method == 'DELETE':
    if len(articles) > article_id:
      del articles[article_id]
    return jsonify({}), 204
  elif request.method == 'PUT':
    if len(articles) > article_id:
      articles[article_id] = request.json
    return jsonify(articles[article_id]), 200


@app.route('/articles', methods=['GET'])
def get_articles():
  global articles
  return jsonify(articles)


app.run(host='0.0.0.0', port=8080)
