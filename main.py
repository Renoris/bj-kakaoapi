# coding=utf8
from flask import Flask, request, jsonify ,json
from PIL import Image
import requests
import wave
import uu
from ast import literal_eval
from lxml import etree

app = Flask(__name__)

def write2file(file,content):
    asd=open(file,'w')
    asd.write(content)
    asd.close()

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'kakaoapi'


# @app.route('/kakao', methods=['POST'])
# def process_image():
#     file = request.files['image']
#     # Read the image via file.stream
#     img = Image.open(file.stream)
#     return jsonify({'msg': 'success', 'size': [img.width, img.height]})


def gokakaovoice_realvoice(file):
    myvoice = file.read()  # open
    api_endpoint = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
    api_endpoint = api_endpoint.encode('utf-8')
    content_type = "application/octet-stream"
    autorization_key="KakaoAK dc299f7081d23643fbb5122481b95b48"
    header = {'Content-Type': content_type,
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

def gokakaovoice_txt(file):
    result = file.read()  # open
    splitdata = result.splitlines()
    splitdata.reverse()
    print(type(splitdata[1]))
    finalresultjsontodict = json.loads(splitdata[1])
    myvoicestr = finalresultjsontodict['value']
    return myvoicestr

def gokakaoxml(voice):
    api_endpoint = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
    content_type = "application/xml"
    autorization_key = "KakaoAK dc299f7081d23643fbb5122481b95b48"
    text_sppech_front='요청하신 사항'
    text_speech = voice
    text_sppech_back='이 맞습니까?'
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


@app.route('/kakao2', methods=['POST'])
def process_voice2():
    file = request.files['file']
    myvoicestr=gokakaovoice_txt(file)
    response=gokakaoxml(myvoicestr)
    return response


    # url2="https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
    # headers2={
    #     "charset":"UTF-8",
    #     "Content-Type":"application/xml" ,
    #     "Authorization":"KakaoAK dc299f7081d23643fbb5122481b95b48"
    # }
    # --xml파트
    # rootxml = etree.Element("speak")
    # voicexml = etree.Element("voice")
    # voicexml.text = myvoicestr
    # voicexml.set("name","WOMAN_DIALOG_BRIGHT")
    # rootxml.append(voicexml)
    # xmloutput=etree.tostring(rootxml, encoding='UTF8')
    # xmlheader='<?xml version="1.0" encoding="UTF-8"?>\n'
    # print(xmlheader + xmloutput.decode('utf-8'))
    # result2 = requests.post(url=url2, headers=headers2, data=xmloutput).text
    # ------xml파트끝
    # -----xml 안되서 직접 값
    # imsi23="<speak><voice name=\"WOMAN_DIALOG_BRIGHT\">편의점에서 물 한 병만 사다 줘</voice></speak>"
    # imsi23=imsi23.encode('utf-8')
    # result2 = requests.post(url=url2, headers=headers2, data=imsi23).text
    # ----xml 안되서 직접 값 끝
    # asd=open('kakaoresult2.mp3', 'w', encoding='UTF8')
    # se23=open('testing.txt','w',encoding='UTF8')
    # se23.write("Sadasdasd")
    # se23.close()
    # asd.write(result2)
    # asd.close()
    # print(type(result2))
    return myvoicestr





if __name__ == '__main__':
    app.run(debug=True)

