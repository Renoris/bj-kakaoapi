# coding=utf8
from flask import Flask, request, jsonify ,json
from PIL import Image
import requests
import wave
from ast import literal_eval
from lxml import etree
from pydub import AudioSegment
import ffmpeg

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



def convertkakaousevoice(file):
    try :
        sound = AudioSegment.from_wav(file)
        sound = sound.set_channels(1)
        sound = sound.set_frame_rate(16000)
        sound = sound.set_sample_width(2)
    except Exception as e:
        print("error :" + e )
    return sound.raw_data


def gokakaovoice_realvoice(file):
    myvoice = file.read()
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



@app.route('/kakao2', methods=['POST'])
def process_voice2():
    try :
        file = request.files['file'].read()
        file = convertkakaousevoice(file)
        myvoicestr = gokakaovoice_realvoice(file)
        response = gokakaoxml(myvoicestr)
    except :
        print('error ')
    return response



@app.route('/kakao3', methods=['POST'])
def process_voice3():
    file = request.files['file']
    myvoicestr=gokakaovoice_realvoice(file)
    return myvoicestr


if __name__ == '__main__':
    app.run(debug=True)

