# coding=utf8
from flask import Flask, request, jsonify ,json ,Response ,send_file
import requests
from pydub import AudioSegment
import io

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'kakaoapi'

def write2file(file,content):
    asd=open(file,'w')
    asd.write(content)
    asd.close()

def write2voice(filename,content):
    file = content.read()
    file2 = open(filename, 'wb')
    file2.write(file)
    file2.close()

def write2voicefirst(filename,content): #맨처음 url에서 받아올때 쓰는 메소드
    file2 = open(filename, 'wb')
    file2.write(content)
    file2.close()

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

@app.route('/kakao1')
def process_voice1():
    message = request.args.get('url')
    response = requests.get(url=message).content
    write2voicefirst("middleresult.wav",response)
    file=io.BufferedReader(open(file='middleresult.wav' , mode='rb'))
    file = convertkakaousevoice(file)
    myvoicestr = gokakaovoice_realvoice(file)
    response = gokakaoxml(myvoicestr)
    return response

@app.route('/kakao2', methods=['POST'])
def process_voice2():
    # file = request.files['file']
    #--
    message = request.files['message']
    message=message.read()
    response=requests.get(url=message).content
    write2voicefirst("middleresult.wav",response)
    file=io.BufferedReader(open(file='middleresult.wav' , mode='rb'))
    # #--
    #---------------------------
    # write2voice("middleresult.wav",file)
    # file = io.BufferedReader(open(file='middleresult.wav' , mode='rb'))
    #-----------------------------------
    file = convertkakaousevoice(file)
    #버퍼로 만들어서 읽어야함 아니면 버퍼 객체로 만들거나 근데 객체로 만드는방법이한정적이여서 잘모르겟음
    myvoicestr = gokakaovoice_realvoice(file)
    response = gokakaoxml(myvoicestr)
    return response

@app.route('/kakao3', methods=['POST'])
def process_voice3():
    message = request.files['file']
    message = message.read()
    response = requests.get(url=message).content
    return response

@app.route('/kakao4')
def process_voice4():
    message = request.args.get('url')
    response = requests.get(url=message).content
    return response

@app.route('/kakao5')
def process_voice5():
    message = request.args.get('url')
    response = requests.get(url=message).content
    response = io.BytesIO(response)
    response = convertkakaousevoice(response)
    response = gokakaovoice_realvoice(response)
    response = gokakaoxml(response)
    return response

@app.route('/kakao6')
def process_voice6():
    message = request.args.get('url')
    message = "https:"+message
    try:
        response = requests.get(url=message).content
    except:
        return message
    try:
        response = io.BytesIO(response)
    except:
        return "io.byte problem"
    response = convertkakaousevoice(response)
    try:
        response = gokakaovoice_realvoice(response)
    except:
        return "realvoiceproblem"
    try:
        response = gokakaoxml(response)
    except:
        return "kakao syn problem"
    try:
        response = Response(response=response, mimetype="audio/mpeg")
    except:
        return "inner response problem"
    return response

@app.route('/kakao7')
def process_voice7():
    message = request.args.get('url')
    message = "https:"+message
    message.encode(encoding="utf-8")
    try:
        response = requests.get(url=message).content
    except:
        return message
    try:
        response = io.BytesIO(response)
    except:
        return "io.byte problem"
    try:
        response = convertkakaousevoice(response)
    except:
        return "conver error"
    try:
        response = gokakaovoice_realvoice(response)
    except:
        return "realvoiceproblem"
    try:
        response = gokakaoxml(response)
    except:
        return "kakao syn problem"
    try:
        response = Response(response=response, mimetype="audio/mpeg")
    except:
        return "inner response problem"
    return response

if __name__ == '__main__':
    app.run(debug=True)
