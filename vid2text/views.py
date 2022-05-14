from django.shortcuts import redirect, render

from vid2text.models import videoUploader


# Create your views here.

def home(request):
    return render(request, 'vid2text/index.html')


def video(request):
    context = {}
    return render(request, 'vid2text/video.html', context)

def upload(request):
    videoUpload = request.FILES['video']
    videoUploader(video = videoUpload).save()
    print(videoUpload)
    print(videoUpload.url)

    # jsondata = videoUploader.objects.filter(video = videoUpload)[0]
    # print(jsondata)
    # print(jsondata.path)


    # filename = "/path/to/foo.wav"
    # def read_file(filename, chunk_size=5242880):
    #     with open(filename, 'rb') as _file:
    #         while True:
    #             data = _file.read(chunk_size)
    #             if not data:
    #                 break
    #             yield data

    # headers = {'authorization': "879ba2458d7c47debbc7189214746348"}
    # response = requests.post('https://api.assemblyai.com/v2/upload', headers=headers, data=read_file(filename))

    # print(response.json())
    print('uploaded')
    return redirect(video)
