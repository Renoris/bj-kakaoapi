# coding=utf8
import requests
import json
import uu
import wave
from pydub import AudioSegment
import time, datetime
import koalanlp
import urllib3
import json


def convertkakaousevoice(file):
    sound = AudioSegment.from_wav(file)
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(16000)
    sound = sound.set_sample_width(2)
    return sound.raw_data


timestamp = datetime.datetime.now().timestamp()

# def convertkakaousevoice2(file):
#     sound = AudioSegment.from_wav(file)
#     sound = sound.set_channels(1)
#     sound = sound.set_frame_rate(16000)
#     sound = sound.set_sample_width(2)
#     sound.export('middleresult',format="wav")

# url1='http://127.0.0.1:5000/kakaoRCG'
# url2 = 'http://127.0.0.1:5000/kakaoSTS'
# file=open('audio.wav','rb')
# file = {
#     'file' : file
# }
# KaKaoApikey="KakaoAK dc299f7081d23643fbb5122481b95b48"
# header = {
#     'Authorization':KaKaoApikey,
# }
#
# response = requests.post(url=url1,headers=header,files=file).text
# urldata=url2+"?say="+response
# urldata.encode('utf-8')
# response=requests.get(url=urldata,headers=header).content
#
# print(type(response))
#
# asd=open('result.wav','wb')
# asd.write(response)
# asd.close()

# -----------------------------------------------------

# openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU"
# accessKey = "2c54c9b9-fa34-4d57-8e20-e8b61fae4c4f"
# analysisCode = "ner"
# text = "근처 편의점에서 피자깡 하나랑 양파깡 두개랑 포테토칩 열개랑 코카콜라 이십병만 살거야"
#
# requestJson = {
# 	"access_key" : accessKey,
# 	"argument" : {
# 		"text" : text,
# 		"analysis_code" : analysisCode
# 	}
# }

# response = requests.post(url=openApiURL,json=requestJson).content
# response = json.loads(response)
# response = json.dumps(response, ensure_ascii=False, indent=4)
# response.encode('utf-8')

#----------------------------------
# #
# #---get방식2
# eviturl="https://evit-project-bj.du.r.appspot.com/kakaoSTS"
# homeurl='http://127.0.0.1:5000/kakao7?url=//s3.amazonaws.com/appforest_uf/f1594707934383x147632581708611600/audio.wav'
# r = requests.get(homeurl).content
# a = open('myvoice','wb')
# a.write(r)
# a.close()
# KaKaoApikey="KakaoAK dc299f7081d23643fbb5122481b95b48"
# header = {
#     'Authorization':KaKaoApikey,
# }
# asd=open('audio3.wav','rb')
# asd={
#     'file' : asd
# }
# eviturl="https://evit-project-bj.du.r.appspot.com/kakaoRCG"
# r = requests.post(url=eviturl, headers=header, files=asd).text
# print(r)

#https://evit-project-bj.du.r.appspot.com/PSA
jsoncall-array
def test_adamsapi(url, params):
    response = requests.get(url=url,params=params).content
    response = json.loads(response)
    response = json.dumps(response, ensure_ascii=False, indent=4)
    asd=open("adamsapiresult9.json",'w')
    asd.write(response)
    return response
# #
# url2="http://api.adams.ai/datamixiApi/tms"
# params={
#     "key":"7493803880294659905",
#     "query" : "이마트에서 물 두 개 음류수 세 개 과자 열 개",
#     "analysis" : "ne",
#     "lang":"kor"
# }
url2="http://127.0.0.1:5000/PS"
params={
    "say":"이마트에서 물 두 개 음류수 세 개 과자 열 개 사다줘",
}

response=test_adamsapi(url=url2,params=params)
