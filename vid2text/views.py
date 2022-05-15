from django.shortcuts import redirect, render
from vid2text.models import videoUploader
import requests
import time

from moviepy.editor import VideoFileClip

# Create your views here.

def home(request):
    return render(request, 'vid2text/index.html')

def video(request):
    context = {}
    return render(request, 'vid2text/video.html', context)

def upload(request):
    videoUpload = request.FILES['video']
    file_obj = videoUploader.objects.create(video=videoUpload)
    file_path = '/media/'+ str(file_obj.video)
    file_path = './' + file_path

    filename = file_path
    videoD = VideoFileClip(filename)
    # print(videoD.duration)  # this will return the length of the video in seconds
    sleepTime = videoD.duration * 0.4
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    headers = {'authorization': "879ba2458d7c47debbc7189214746348"}
    response = requests.post('https://api.assemblyai.com/v2/upload', headers=headers, data=read_file(filename))

    url = response.json()['upload_url']

    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = { "audio_url": url }
    headers = {
        "authorization": "879ba2458d7c47debbc7189214746348",
        "content-type": "application/json"
    }
    response = requests.post(endpoint, json=json, headers=headers)
    # print(response.json())
    print(response.json()['id'])
    time.sleep(sleepTime)

    id = str(response.json()['id'])
    endpoint = "https://api.assemblyai.com/v2/transcript/"+id
    headers = {
        "authorization": "879ba2458d7c47debbc7189214746348",
    }
    response = requests.get(endpoint, headers=headers)
    print()
    print(response.json()['text'])
    text = response.json()['text']
    request.session['text'] = text
    # return redirect(video)
    context = {'text': text}
    return render(request, 'vid2text/video.html', context)
