from flask import Flask, render_template, request
from markupsafe import escape
import requests as req
import os
import urllib
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/download/', methods=['GET', 'POST'])
def download():
    ytlink=request.args.get("ytlink", 0)
    if ytlink:
        print(request.args)
        format = request.args["format"]
        print(format)
        print("start")
        #youtube-dl -x --audio-format mp3
        if format == "mp4":
            os.system("youtube-dl -o \"static/%(id)s\" --format \"bestvideo[height<=480]+bestaudio[ext=m4a]/bestvideo+bestaudio/best\" --merge-output-format mp4 " + ytlink)
        elif format == "mp3":
            os.system("youtube-dl -o \"static/%(id)s.%(ext)s\" -x --audio-format mp3 " + ytlink)
        print("stop")
        if "youtu.be" in ytlink:
            id = ytlink.split("/")[1]
        elif "youtube.com" in ytlink:
            id = ytlink.split("=")[1][:11]
        if format == "mp4":
            vidExt = ".mp4"
        elif format == "mp3":
            vidExt = ".mp3"
        fileUrl = "http://127.0.0.1:5000/static/" + id + vidExt
        print(fileUrl)
        soup = BeautifulSoup(urllib.request.urlopen(ytlink))
        videoName = soup.title.string + vidExt
        videoThumb = "https://img.youtube.com/vi/" + id + "/mqdefault.jpg"
        return render_template('download.html', downloadLink = fileUrl, videoName = videoName, videoThumb = videoThumb)
    else:
        return render_template('download.html')
        
#https://www.youtube.com/watch?v=oBYbxw8f5OI