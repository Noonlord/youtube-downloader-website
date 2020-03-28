from flask import Flask, render_template, request
from markupsafe import escape
import requests as req
import os
app = Flask(__name__)

@app.route('/download/', methods=['GET', 'POST'])
def download():
    ytlink=request.args.get("ytlink", 0)
    if ytlink:
        print("start")
        os.system("youtube-dl.exe -o static/%(id)s --format \"bestvideo[height<=480]+bestaudio[ext=m4a]/bestvideo+bestaudio/best\" --merge-output-format mp4 " + ytlink)
        print("stop")
        if "youtu.be" in ytlink:
            pass
        elif "youtube.com" in ytlink:
            id = ytlink.split("=")[1][:11]
            fileUrl = "http://127.0.0.1:5000/static/" + id + ".mp4"
            print(fileUrl)
        return render_template('download.html.jinja', downloadLink = fileUrl)
    else:
        return render_template('download.html.jinja')
        
#https://www.youtube.com/watch?v=oBYbxw8f5OI