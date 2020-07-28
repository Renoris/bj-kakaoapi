# coding=utf8
import requests
import json
import uu
import wave
from pydub import AudioSegment
import koalanlp
import urllib3
import json

def convertkakaousevoice(file):
    sound = AudioSegment.from_wav(file)
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(16000)
    sound = sound.set_sample_width(2)
    return sound.raw_data

# def convertkakaousevoice2(file):
#     sound = AudioSegment.from_wav(file)
#     sound = sound.set_channels(1)
#     sound = sound.set_frame_rate(16000)
#     sound = sound.set_sample_width(2)
#     sound.export('middleresult',format="wav")

# url1='http://127.0.0.1:5000/kakaoRCG'
# # url2 = 'http://127.0.0.1:5000/kakaoSTS'
# file=open('audio2.wav','rb')
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
# asd=open('result2.txt','w')
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

# def test_adamsapi(url, params):
#     response = requests.get(url=url,params=params).content
#     response = json.loads(response)
#     response = json.dumps(response, ensure_ascii=False, indent=4)
#     asd=open("adamsapiresult6.json",'w')
#     asd.write(response)
#     return response
# # # 감자를 감(VV) 자(EC)로 때어버림
# # 새우를 동사로 받음
# # result1="물이랑 음료수랑 과자랑 피자랑 치토스 사가 줘요"
# result2="감자 다섯개 새우 여섯개 지갑 세개 물 여덟개 식사권 다섯개 사다줘"
# url2="http://api.adams.ai/datamixiApi/tms"
# params={
#     "key":"7493803880294659905",
#     "query" : result2,
#     "analysis" : "ne",
#     "lang":"kor"
# }
# url2="http://127.0.0.1:5000/PSA"
# params={
#     "say":result2,
# }

# response=test_adamsapi(url=url2,params=params)

def findroute():
    url="https://apis.openapi.sk.com/tmap/routes"


def findname(searchkeyword, centerLon, centerLat):
    url="http://127.0.0.1:5000/tmapfind"
    params={
        'searchKeyword' : searchkeyword,
        'centerLon' : centerLon,
        'centerLat' : centerLat,
    }
    response=requests.get(url=url,params=params).text
    return response

print(findname("편의점",'126.571664','33.442260'))