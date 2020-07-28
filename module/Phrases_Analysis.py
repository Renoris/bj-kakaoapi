import json
import requests

def getlocation(data):
    for idx, val in enumerate(data):
        if val["lemma"] == "에서":
            locationjson=data.pop(idx-1) #data에서 이마트는 빠져나감
            return locationjson["lemma"]
    return "편의점"


def knownmany(data):
    word=data['lemma']
    if word=="하나" or word == "한" or word == "1":
        return "1"
    elif word=="둘" or word == "두" or word=="2":
        return "2"
    elif word == "셋" or word == "세" or word=="3":
        return "3"
    elif word == "넷" or word == "네" or word=="4":
        return "4"
    elif word == "다섯" or word == "5":
        return "5"
    elif word == "여섯" or word == "6":
        return "6"
    elif word == "일곱" or word == "7":
        return "7"
    elif word == "여덟" or word == "8":
        return "8"
    elif word == "아홉" or word== "9":
        return "9"
    elif word == "열" or word=="10":
        return "10"

def getNNGNNP(data):
    NRfind=False
    NNPNNGlist = {}
    product = ""
    number = 0
    for idx, val in enumerate(data):
        if NRfind==False:
            if val["type"] == "NNG" or val["type"] == "NNP":
                product = val["lemma"]
                NRfind = True
                print(product)
        else:
            if val["type"] == "MM" or val["type"] == "NR" or val["type"] == "SN":
                number = knownmany(val)
                NRfind = False
                NNPNNGlist.update([("제품", product)])
                NNPNNGlist.update([("수량", number)])
                print(number)
                product = ""
                number = 0
                print(NNPNNGlist)
                return NNPNNGlist

def getNNGNNPArray(data):
    NRfind=False
    arraylist=[]
    NNPNNGlist={}
    product=""
    number=0
    for idx, val in enumerate(data):
        if NRfind==False:
            if val["type"] == "NNG" or val["type"] == "NNP":
                product = val["lemma"]
                NRfind = True
        else:
            if val["type"] == "MM" or val["type"] == "NR" or val["type"] == "SN":
                number = knownmany(val)
                NRfind = False
                NNPNNGlist.update([("제품",product)])
                NNPNNGlist.update([("수량",number+"개")])
                product = ""
                number = 0
                print(NNPNNGlist)
                arraylist.append(NNPNNGlist)
                NNPNNGlist={}

            elif val["type"] == "NNG" or val["type"] == "NNP":
                number = "1"
                NRfind = False
                NNPNNGlist.update([("제품", product)])
                NNPNNGlist.update([("수량", number + "개")])
                print(number)
                product = ""
                number = 0
                print(NNPNNGlist)
                arraylist.append(NNPNNGlist)
                NNPNNGlist = {}
    return arraylist
#
# def testgetNNGNNPArray(data):
#     NRfind = False
#     arraylist = []
#     NNPNNGlist = {}
#     product = ""
#     number = 1
#     for idx, val in enumerate(data):
#         if NRfind == False:
#             if val["type"] == "NNG" or val["type"] == "NNP":
#                 NRfind = True
#                 product = val["lemma"]
#                 number = "1"
#                 NNPNNGlist.update([("제품", product)])
#                 NNPNNGlist.update([("수량", number + "개")])
#                 arraylist.append(NNPNNGlist)
#                 NNPNNGlist={}
#         else:
#             if val["type"] == "MM" or val["type"] == "NR" or val["type"] == "SN":
#                 NRfind = False
#                 NNPNNGlist=arraylist[-1]
#                 number = knownmany(val)
#                 NNPNNGlist.update([("수량", number + "개")])
#                 arraylist.remove(arraylist[-1])
#                 arraylist.append(NNPNNGlist)
#                 product = ""
#                 NNPNNGlist = {}
#             elif val["type"] == "NNG" or val["type"] == "NNP":
#                 NRfind = False
#                 product = val['lemma']
#                 number = "1"
#                 NNPNNGlist.update([("제품", product)])
#                 NNPNNGlist.update([("수량", number + "개")])
#                 arraylist.append(NNPNNGlist)
#                 NNPNNGlist = {}
#     return arraylist

# def testgetNNGNNPArrayelrang(data):
#     NRfind=False
#     arraylist=[]
#     NNPNNGlist={}
#     product=""
#     number=0
#     chainmmgp=False
#     for idx, val in enumerate(data):
#         if NRfind==False:
#             if val["type"] == "NNG" or val["type"] == "NNP":
#                 if chainmmgp == True:
#                     chainmmgp=False
#                     continue
#                 product = val["lemma"]
#                 number = "1"
#                 NNPNNGlist.update([("제품", product)])
#                 NNPNNGlist.update([("수량", number)])
#                 arraylist.append(NNPNNGlist)
#                 NRfind = True
#                 chainmmgp==True
#         else:
#             if val["type"] == "NNG" or val["type"] == "NNP":
#                 if chainmmgp==True:
#                     chainmmgp=False
#                     continue
#                 product = val["lemma"]
#                 number = "1"
#                 NNPNNGlist.update([("제품", product)])
#                 NNPNNGlist.update([("수량", number)])
#                 arraylist.append(NNPNNGlist)
#                 NNPNNGlist = {}
#                 chainmmgp = True
#             else:
#                 chainmmgp = False
#                 if val["type"] == "MM" or val["type"] == "NR" or val["type"] == "SN":
#                     number = knownmany(val)
#                     NNPNNGlist = arraylist[-1]
#                     arraylist.remove(arraylist[-1])
#                     NNPNNGlist.update([("수량", number)])
#                     arraylist.append(NNPNNGlist)
#                     NNPNNGlist = {}
#                     NRfind = False
#     return arraylist

def usesay(makedict):
    data = makedict
    saystring = ""
    location = data['location']
    productlist = data['product']
    saystring += location+"에서 "
    for i in productlist:
        saystring += i['제품']+" "
        saystring += i["수량"]+" "
    saystring += "구입"
    return saystring

def getpsdata(jsonfile):
    data=json.loads(jsonfile)
    data = data["return_object"]["sentence"]
    data = data[0]
    data = data["morp"]
    location = getlocation(data)
    productlist=getNNGNNP(data)
    result={}
    result.update([("location", location)])
    result.update([("product", productlist)])
    result=json.dumps(result, ensure_ascii=False)
    return result

def getpsdataArray(jsonfile):
    data=json.loads(jsonfile)
    data = data["return_object"]["sentence"]
    data = data[0]
    data = data["morp"]
    location = getlocation(data)
    productlist=getNNGNNPArray(data)
    result={}
    result.update([("location", location)])
    result.update([("product", productlist)])
    saystring=usesay(result)
    result.update([("say",saystring)])
    result=json.dumps(result, ensure_ascii=False)
    return result

def testgetpsdataArray(jsonfile):
    data=json.loads(jsonfile)
    data = data["return_object"]["sentence"]
    data = data[0]
    data = data["morp"]
    location = getlocation(data)
    productlist=testgetNNGNNPArray(data)
    result={}
    result.update([("location", location)])
    result.update([("product", productlist)])
    print(result)
    saystring=usesay(result)
    result.update([("say",saystring)])
    result=json.dumps(result, ensure_ascii=False)
    return result

def getdataadams(myvoicestrng):
    url = "http://api.adams.ai/datamixiApi/tms"
    params = {
        "key": "7493803880294659905",
        "query": myvoicestrng,
        "analysis": "ne",
        "lang": "kor"
    }
    return requests.get(url=url, params=params).content

