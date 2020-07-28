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
#
# @app.route('/testPSA', methods=['POST'])
# def parsesentencetestRA():
#     psjson=request.files['file']
#     psjson=psjson.read()
#     result = PS.testgetpsdataArray(psjson)
#     return result

@app.route('/tmapfind')
def findname():
    searchkeyword = request.args.get('searchKeyword')
    # searchkeyword = str(searchkeyword)
    centerLon = request.args.get('centerLon')
    # centerLon = str(centerLon)
    print(searchkeyword)
    print(centerLon)
    centerLat = request.args.get('centerLat')
    # centerLat = str(centerLat)
    print(centerLat)
    url="https://apis.openapi.sk.com/tmap/pois"
    params={
        'page': 1,
        'count': 2,
        'version' : '1',
        'searchKeyword' : searchkeyword,
        'resCoordType' : 'WGS84GEO',
        'searchType' : 'all',
        'multiPoint' : 'N',
        'searchtypCd' : 'R',
        'radius': 15,
        'reqCoordType' : 'WGS84GEO',
        'centerLon' : centerLon,
        'centerLat' : centerLat,
        'appKey' : 'l7xxb88000c3454247eab158acc8a7094995'
    }
    response = requests.get(url=url,params=params).text
    print(response)
    return response

if __name__ == '__main__':
    app.run(debug=True)
