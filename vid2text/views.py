from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'vid2text/index.html')


def video(request):
    return render(request, 'vid2text/video.html')
