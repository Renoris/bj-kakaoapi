# coding=utf8
from flask import Flask, request, jsonify ,json ,Response ,send_file
import requests
from pydub import AudioSegment
import io
import time
import module.kakaoApi as usekakaoapi
import module.Phrases_Analysis as PS
app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'kakaoapi'

@app.route('/kakao9', methods=['POST'])
def process_voice9():
    KaKaoRCGUrl = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
    KaKaoSTSUrl = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
    voicefile = request.files['file']
    KaKaoApikey = request.headers['Authorization']
    # -wav 파일 변환
    response = voicefile.read()
    response = io.BytesIO(response)
    # -- KaKaoRCG
    response = usekakaoapi.convertkakaousevoice(response)
    header = usekakaoapi.MakeKaKaoRCGH(apikey=KaKaoApikey)
    response = usekakaoapi.MakeKaKaoRCGR(url=KaKaoRCGUrl, headers=header, content=response)
    #-- STS 시작
    header = usekakaoapi.MakeKaKaoSTSH(apikey=KaKaoApikey)
    body = usekakaoapi.MakeKaKaoSTSB(response)
    response = usekakaoapi.MakeKaKaoSTSR(url=KaKaoSTSUrl,header=header,body=body)
    #-- STS 가공
    response = Response(response=response, mimetype="audio/mpeg")
    return response


@app.route('/kakaoRCG', methods=['POST'])
def process_voiceRCG():
    KaKaoRCGUrl = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
    voicefile = request.files['file']
    KaKaoApikey = request.headers['Authorization']
    response = voicefile.read()
    response = io.BytesIO(response)
    # -- KaKaoRCG
    response = usekakaoapi.convertkakaousevoice(response)
    header = usekakaoapi.MakeKaKaoRCGH(apikey=KaKaoApikey)
    response = usekakaoapi.MakeKaKaoRCGR(url=KaKaoRCGUrl, headers=header, content=response)
    return response

@app.route('/kakaoSTS')
def process_voiceSTS():
    KaKaoSTSUrl = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
    RCGVoice = request.args.get('say')
    KaKaoApikey = request.headers['Authorization']
    header = usekakaoapi.MakeKaKaoSTSH(apikey=KaKaoApikey)
    body = usekakaoapi.MakeKaKaoSTSB(RCGVoice)
    response = usekakaoapi.MakeKaKaoSTSR(url=KaKaoSTSUrl, header=header, body=body)
    response = Response(response=response, mimetype="audio/mpeg")
    return response


@app.route('/PS')
def parsesentence():
    voicestring = request.args.get('say')
    psjson = PS.getdataadams(voicestring)
    result = PS.getpsdata(psjson)
    return result

@app.route('/PSA')
def parsesentenceRA():
    voicestring = request.args.get('say')
    psjson = PS.getdataadams(voicestring)
    result = PS.getpsdataArray(psjson)
    return result
if __name__ == '__main__':
    app.run(debug=True)
