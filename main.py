# coding=utf8
from flask import Flask, request, jsonify ,json
from PIL import Image
import requests
import wave
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
    myvoice = file.read()  #3 인자 값으로 들어온 파일을 읽어서 myvoice 변수에 저장한다
    api_endpoint = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize" #4 url값을 엔드포인트라는 변수에저장
    api_endpoint = api_endpoint.encode('utf-8') #5 url값을 utf-8로 인코딩
    content_type = "application/octet-stream" #6 헤더값에 들어갈 컨텐츠 타입을 변수에 저장
    autorization_key="KakaoAK dc299f7081d23643fbb5122481b95b48" #7 헤더값에 들어갈 카카오개인키를 저장
    header = {'Content-Type': content_type,         #8헤더 작성, 컨텐츠타입 키에 컨텐츠 타입변수 저장,작성자 키에 카카오 개인키를 저장
              'Authorization': autorization_key,
              }
    result = requests.post(url=api_endpoint, headers=header, data=myvoice).text #9 카카오 api를 요청하기 위해 리퀘스트메소드를
    #이용해서 url(카카오음성인식url), header, 그리고 아까 인자값으로 받은 파일을 보내서 그 결과의 텍스트를 result 변수에 저장
    splitdata=result.splitlines() #10 result 변수를 줄단위로 나눠서 배열로 저장
    splitdata.reverse() #11 배열의 순서를 서로 뒤집음
    # finalresult = json.dumps(splitdata[1], ensure_ascii=False, encoding='utf-8')
    # finalresultjsontodict = json.loads(finalresult)
    finalresultjsontodict=json.loads(splitdata[1])#12 마지막줄에서 2번째(배열은 0부터시작하니까 1)를 가져와서 json타입을 디렉토리타입으로 변환
    myvoicestr = finalresultjsontodict['value']#13 디렉토리 타입에서 value 값을 꺼내서 myvoice str을 저장
    return myvoicestr #14 myvoicestr을 리턴




def gokakaovoice_txt(file):
    result = file.read()  # open
    splitdata = result.splitlines()
    splitdata.reverse()
    print(type(splitdata[1]))
    finalresultjsontodict = json.loads(splitdata[1])
    myvoicestr = finalresultjsontodict['value']
    return myvoicestr

def gokakaoxml(voice):
    api_endpoint = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize" #17 url저장
    content_type = "application/xml" #18 헤더에 넣을 컨텐츠 타입변수를 저장
    autorization_key = "KakaoAK dc299f7081d23643fbb5122481b95b48" #19 헤더에넣을 카카오 키 저장
    text_sppech_front='요청하신 사항' #20 바디에 넣을 우리가 말한 음성의 앞쪽에 저장할 말을 변수에 저장
    text_speech = voice #21 인자값으로 받은 보이스를 변수에 저장
    text_sppech_back='이 맞습니까?' #22 바디에 넣을 우리가말한 음성의 뒤쪽에 저장할 말을 변수에 저장
    xml_data = f'<speak>  \
                    <voice name="WOMAN_DIALOG_BRIGH" >{text_sppech_front}</voice> \
                    <voice name="WOMAN_DIALOG_BRIGH" >{text_speech}</voice> \
                    <voice name="WOMAN_DIALOG_BRIGH" >{text_sppech_back}</voice> \
                </speak>'
    #23 위처럼 xml_data 라는 변수에 xml형식처럼 위에서 저장한 변수를 활용해서 xml 데이터를 생성
    api_endpoint = api_endpoint.encode('utf-8') #24 url을 utf-8로 변환
    xml_data = xml_data.replace('\r', '').encode('utf-8') #25 위에서 데이터로 가공하기위해 쓴 \를 전송할 최종적으로 전송할 데이터로
    #만들기위해 \r을 제거하고 utf-8로 변환
    header = {'Content-Type': content_type,
              'Authorization': autorization_key,
              }
    #26 헤더를 변수를 이용해서 작성
    response = requests.post(api_endpoint, headers=header, data=xml_data).content #27이제 저장된 데이터를 이용해서 카카오
    #음성합성 api에게 요청하고 내용이 mp3형식일거니까 text가 아닌 content를 받아 변수에 저장
    return response #27변수를 반


@app.route('/kakao2', methods=['POST'])
def process_voice2():
    file = request.files['file'] #1 리퀘스트(요청으로 들어온 파일을 받는다)
    myvoicestr=gokakaovoice_realvoice(file)#2 위에 만들어둔 gokakaovice_realvoice메소드를 file을 인자값으로 호출한다.
    #15 myvoicestr을 받앗으니 그걸 이제 변수에 저장하고 이제 음성 합성 api로 넘길 차례
    response=gokakaoxml(myvoicestr) #16 myvoicestr을 위에 음성합성 api로 넘기는 메소드를 실행환
    #28 메소드에서 받은 변수를 response 라는 변수에 저장
    return response # 29 우리가만든 api에서 클라이언트(bubble이나 우리가 만든 클라이언트)에 반환


if __name__ == '__main__':
    app.run(debug=True)

