import flask
from flask import request, Flask, redirect, jsonify, render_template
from time import time
import os
import io
import lib
from lib import getMRZFromImg, mrzToText, getMRZData

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def file_ext(filename):
  return filename.split('.', 1)[-1].lower()
def allowed_file(filename):
  return file_ext(filename)  in ALLOWED_EXTENSIONS



@app.route('/mrzdata', methods=['POST'])
def mrzdata():
  if request.files.get("file"):
    file = request.files['file']
    if file and allowed_file(file.filename):  
      filename = str(time()).split(".")[0] + file_ext(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      imgpath = os.path.dirname(os.path.realpath(__file__))+"/uploads/"+filename
      img  = getMRZFromImg(imgpath=imgpath)
      text = mrzToText(img)
      data, t  = getMRZData(text)
      return jsonify( {
        "mrzdata": data,
    })


@app.route('/', methods=['POST'])
def upload_file():
  if request.files.get("file"):
    file = request.files['file']
    if file and allowed_file(file.filename):  
      filename = str(time()).split(".")[0] + file_ext(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      imgpath = os.path.dirname(os.path.realpath(__file__))+"/uploads/"+filename
      img  = getMRZFromImg(imgpath=imgpath)
      text = mrzToText(img)
      data, t  = getMRZData(text)

      return render_template('result.html', resultat=data)
  return render_template('index.html')
        

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html', resultat=None)


if __name__ == "__main__":
	app.run()