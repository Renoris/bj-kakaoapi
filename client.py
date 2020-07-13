import requests
import json
import uu
url = 'http://127.0.0.1:5000/kakao2'
my_img = {'file': open('kakaoresult.txt', 'rb')}
r = requests.post(url, files=my_img).content

