from flask import Flask, render_template, request
from markupsafe import escape
import requests as req
app = Flask(__name__)

@app.route('/download/', methods=['GET', 'POST'])
def download():
    ytlink=request.args.get("ytlink", 0)
    if ytlink:
        return render_template('download.html.jinja', ytlink=ytlink)
    else:
        return render_template('download.html.jinja')
        
#https://www.youtube.com/watch?v=oBYbxw8f5OI