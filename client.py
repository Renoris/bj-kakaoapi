import requests
import json
import uu
import wave
from pydub import AudioSegment
import ffmpeg

def convertkakaousevoice(file):
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


url = 'http://127.0.0.1:5000/kakao2'
myfile=open('audio.wav','rb')
myfile=convertkakaousevoice(myfile)
my_img = {'file': myfile}
r = requests.post(url, files=my_img).content
a = open('myvoice.mp3','wb')
a.write(r)
a.close()

