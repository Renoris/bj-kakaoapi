import requests
import json
import uu
import wave
from pydub import AudioSegment
import ffmpeg

def convertkakaousevoice(file):
    print(type(file))
    sound = AudioSegment.from_wav(file)
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(16000)
    sound = sound.set_sample_width(2)
    return sound.raw_data

# url2 ='https://evit-project-bj.du.r.appspot.com/kakao2'
# myfile=open('audio.wav','rb')
# convertvoice=convertkakaousevoice(myfile)
# my_img = {'file': convertvoice}
# my_img = {'file': open('asd', 'rb')}


# url = 'http://127.0.0.1:5000/kakao2'
# myfile=open('audio.wav','rb')
# print(type(myfile))
# # myfile=convertkakaousevoice(myfile)
# print(type(myfile))
# my_img = {'file': myfile}
# r = requests.post(url, files=my_img).content
# a = open('myvoice.mp3','wb')
# a.write(r)
# a.close()

# #------
# url = 'http://127.0.0.1:5000/kakao2'
# message = "https://s3.amazonaws.com/appforest_uf/f1594707934383x147632581708611600/audio.wav"
# my_img = {'message': message}
# r = requests.post(url, files=my_img).content
# a = open('myvoice.mp3','wb')
# a.write(r)
# a.close()

# #---get방식
# eviturl="https://evit-project-bj.du.r.appspot.com/"
# url = 'https://evit-project-bj.du.r.appspot.com/kakao1?url=https://s3.amazonaws.com/appforest_uf/f1594707934383x147632581708611600/audio.wav'
# r = requests.get(url).content
# a = open('myvoice.mp3','wb')
# a.write(r)
# a.close()

#---get방식2
eviturl="https://evit-project-bj.du.r.appspot.com/"
homeurl='https://evit-project-bj.du.r.appspot.com/kakao7?url=//s3.amazonaws.com/appforest_uf/f1594707934383x147632581708611600/audio.wav'
r = requests.get(homeurl).content
a = open('myvoice','wb')
a.write(r)
a.close()