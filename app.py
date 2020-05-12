from flask import Flask, render_template, request

import re
import bz2
import _pickle as cPickle


model = cPickle.load(bz2.BZ2File('svmModel.pbz2', 'rb')) 
vectorizer = cPickle.load(bz2.BZ2File('vectorizer.pbz2', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/predict', methods = ['POST', 'GET'])
def predict():
  originalComment = request.form['comment']
  originalComment = originalComment.strip()

  words = re.split(r'\W+', originalComment)
  for i in range(len(words)):
      words[i] = ''.join([c for c in words[i] if not c.isdigit() ])
  comment = ' '.join(map(str, words)).lower()
  v_comment = vectorizer.transform([comment])
  rating = model.predict(v_comment)[0]
  #rating  = 0
  return render_template('index.html', comment=comment, rating= rating)


if __name__ == "__main__":
  app.run(debug = True)