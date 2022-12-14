import nltk

import nltk.tag

import nltk.tokenize

from flask import Flask, request, jsonify
from functions.NewHifenizei import hifenizei
from functions.answerComplet import answer

nltk.download('punkt')



app = Flask(__name__)

@app.route('/')
def view0 ():
    return 'hifeniz.ei - backend'

@app.route('/dt')
def view8 ():
    return 'hello2'

@app.route('/data')
def view ():
    word = request.args.get('word')
    word2 = word.lower()
    x = hifenizei(word2)
    response = jsonify({'word': x})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/datas')
def view2 ():
    word2 = request.args.get('word2')
    x = answer(word2)
    response = jsonify({'word2': x})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    



if __name__ == '__main__':
    app.run(debug=True)

