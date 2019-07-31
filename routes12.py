from search import search
import flask
from flask import jsonify
from flask import Flask, render_template, request
app = Flask(__name__)      


@app.route('/')
def home():
  return render_template('indexd.html')

@app.route('/enrolll1')
def enrolll1():
  resp = flask.Response('{"data": "' + str(search()) + '"}')
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp
@app.route('/')
def home1():
  return render_template('indexe.html')

@app.route('/enrolll2')
def enrolll2():
  resp = flask.Response('{"data": "' + str(search()) + '"}')
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp
@app.route('/enrolll3')
def enrolll3():
  resp = flask.Response('{"data": "' + str(search()) + '"}')
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp
if __name__ == '__main__':
  app.run(debug=True)
