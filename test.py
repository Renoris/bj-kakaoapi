
#-*- coding:utf-8 -*-
import unittest #기본적인 라이브러리
import requests
import xml
import pytest

class locationsearch(unittest.TestCase):
    # def testAdd(self):
    #     result = FAO.add(10, 20)
    #     if result == 20:
    #         print('test clear')
    #
    #     else:
    #         print('test fail')
    #
    #
    # def testsubstact(self):
    #     result = FAO.substact(20,40)
    #     if result == -20:
    #         print('test ok')
    #
    #     else:
    #         print('test fail')

    # def testsplitingsay(self): # 맨앞글자에 test를 붙여야함
    #     location = sayanalysis.splitingsay("가까운 편의점에서 생수1병만 사다줘")
    #     if location == "편의점":
    #         print("테스트 성공")
    #
    #
    # def testsplitingsay2(self): # 맨앞글자에 test를 붙여야함
    #     location = sayanalysis.splitingsay("근처 슈퍼마켓이 어디야?")
    #     if location == "슈퍼마켓":
    #         print("테스트 성공")
    #     else :
    #         print("테스트 실패")

    def testassert(self):
        url = 'http://127.0.0.1:5000/im_size'
        myfile=open(file='kakaoresult.txt')
        r = requests.post(url, files=myfile)

        # convert server response into JSON format.
        print(r.json())




