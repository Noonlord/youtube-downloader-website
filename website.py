from flask import Flask, render_template, request
from markupsafe import escape
import requests as req
app = Flask(__name__)

@app.route('/download/', methods=['POST', 'GET'])
def download():
    if request.method == "POST":
        return render_template('download.html.jinja', ytlink=request.form["ytlink"])
    else:
        return render_template('download.html.jinja')
        
#https://www.youtube.com/watch?v=oBYbxw8f5OI