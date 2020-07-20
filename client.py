import requests
import json
import uu
import wave
from pydub import AudioSegment

def convertkakaousevoice(file):
    sound = AudioSegment.from_wav(file)
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(16000)
    sound = sound.set_sample_width(2)
    return sound.raw_data


def convertkakaousevoice2(file):
    sound = AudioSegment.from_wav(file)
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(16000)
    sound = sound.set_sample_width(2)
    sound.export('middleresult',format="wav")

url = 'http://127.0.0.1:5000/kakao9'
file=open('middleresult','rb')
content_type = "application/octet-stream"
file={
    'file':file
}
KaKaoApikey="KakaoAK dc299f7081d23643fbb5122481b95b48"
header = {
    'Authorization':KaKaoApikey,
}
response = requests.post(url=url,headers=header, files=file).content
#------------------------------------------------------------
asd=open('result.wav','wb')
asd.write(response)
asd.close()






#-----------------------------------------------------
# #
# #---get방식2
# eviturl="https://evit-project-bj.du.r.appspot.com/"
# homeurl='http://127.0.0.1:5000/kakao7?url=//s3.amazonaws.com/appforest_uf/f1594707934383x147632581708611600/audio.wav'
# r = requests.get(homeurl).content
# a = open('myvoice','wb')
# a.write(r)
# a.close()