# coding=utf8
from flask import Flask, request, jsonify ,json ,Response ,send_file
import requests
from pydub import AudioSegment
import io
import time


app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'kakaoapi'

def convertkakaousevoice(file):
    sound = AudioSegment.from_file(file, format="wav")
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(16000)
    sound = sound.set_sample_width(2)
    return sound.raw_data

def gokakaovoice_realvoice(file):
    myvoice = file
    #file=file.read()
    api_endpoint = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
    api_endpoint = api_endpoint.encode('utf-8')
    content_type = "application/octet-stream"
    autorization_key="KakaoAK dc299f7081d23643fbb5122481b95b48"
    header = {
        'Content-Type': content_type,
        'Authorization': autorization_key,
    }
    result = requests.post(url=api_endpoint, headers=header, data=myvoice).text
    splitdata=result.splitlines()
    splitdata.reverse()
    # finalresult = json.dumps(splitdata[1], ensure_ascii=False, encoding='utf-8')
    # finalresultjsontodict = json.loads(finalresult)
    finalresultjsontodict=json.loads(splitdata[1])
    myvoicestr = finalresultjsontodict['value']
    return myvoicestr

def MakeKaKaoRCGH(apikey):
    content_type = "application/octet-stream"
    header = {
        'Content-Type': content_type,
        'Authorization': apikey,
    }
    return header

def MakeKaKaoRCGR(url,headers,content):
    print(url)
    response = requests.post(url=url, headers=headers, data=content).text
    splitdata = response.splitlines()
    splitdata.reverse()
    result = json.loads(splitdata[1])
    return result['value']

# def gokakaovoice_txt(file):
#     result = file.read()  # open
#     splitdata = result.splitlines()
#     splitdata.reverse()
#     print(type(splitdata[1]))
#     finalresultjsontodict = json.loads(splitdata[1])
#     myvoicestr = finalresultjsontodict['value']
#     return myvoicestr

def MakeKaKaoSTSH(apikey):
    content_type = "application/xml"
    header = {'Content-Type': content_type,
              'Authorization': apikey,
    }
    return header

def MakeKaKaoSTSB(content):
    text_sppech_front = '요청하신 사항'
    text_speech = content
    text_sppech_back = '이 맞습니까?'
    xml_data = f'<speak>  \
                        <voice name="WOMAN_DIALOG_BRIGH" >{text_sppech_front}</voice> \
                        <voice name="WOMAN_DIALOG_BRIGH" >{text_speech}</voice> \
                        <voice name="WOMAN_DIALOG_BRIGH" >{text_sppech_back}</voice> \
                    </speak>'
    xml_data = xml_data.replace('\r', '').encode('utf-8')
    return xml_data

def MakeKaKaoSTSR(url,header,body):
    return requests.post(url=url, headers=header, data=body).content


def gokakaoxml(voice):
    api_endpoint = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
    content_type = "application/xml"
    autorization_key = "KakaoAK dc299f7081d23643fbb5122481b95b48"
    text_sppech_front='요청하신 사항'
    text_speech = voice
    text_sppech_back = '이 맞습니까?'
    xml_data = f'<speak>  \
                    <voice name="WOMAN_DIALOG_BRIGH" >{text_sppech_front}</voice> \
                    <voice name="WOMAN_DIALOG_BRIGH" >{text_speech}</voice> \
                    <voice name="WOMAN_DIALOG_BRIGH" >{text_sppech_back}</voice> \
                </speak>'

    api_endpoint = api_endpoint.encode('utf-8')
    xml_data = xml_data.replace('\r', '').encode('utf-8')
    header = {'Content-Type': content_type,
              'Authorization': autorization_key,
              }

    response = requests.post(api_endpoint, headers=header, data=xml_data).content
    return response

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
    response = convertkakaousevoice(response)
    header = MakeKaKaoRCGH(apikey=KaKaoApikey)
    response = MakeKaKaoRCGR(url=KaKaoRCGUrl, headers=header, content=response)
    #-- STS 시작
    header = MakeKaKaoSTSH(apikey=KaKaoApikey)
    body = MakeKaKaoSTSB(response)
    response = MakeKaKaoSTSR(url=KaKaoSTSUrl,header=header,body=body)
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
    response = convertkakaousevoice(response)
    header = MakeKaKaoRCGH(apikey=KaKaoApikey)
    response = MakeKaKaoRCGR(url=KaKaoRCGUrl, headers=header, content=response)
    return response

@app.route('/kakaoSTS')
def process_voiceSTS():
    KaKaoSTSUrl = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
    RCGVoice = request.args.get('say')
    KaKaoApikey = request.headers['Authorization']
    header = MakeKaKaoSTSH(apikey=KaKaoApikey)
    body = MakeKaKaoSTSB(RCGVoice)
    response = MakeKaKaoSTSR(url=KaKaoSTSUrl, header=header, body=body)
    response = Response(response=response, mimetype="audio/mpeg")
    return response

if __name__ == '__main__':
    app.run(debug=True)
