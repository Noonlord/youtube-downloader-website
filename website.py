from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/download/<vidID>')
def download(vidID):
    return escape(vidID)