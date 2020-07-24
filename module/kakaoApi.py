from flask import Flask, request, jsonify ,json ,Response ,send_file
import requests
from pydub import AudioSegment

def gokakaovoice_txt(file):
    result = file.read()  # open
    splitdata = result.splitlines()
    splitdata.reverse()
    finalresultjsontodict = json.loads(splitdata[1])
    myvoicestr = finalresultjsontodict['value']
    return myvoicestr

def convertkakaousevoice(file):
    sound = AudioSegment.from_file(file, format="wav")
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(16000)
    sound = sound.set_sample_width(2)
    return sound.raw_data

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
