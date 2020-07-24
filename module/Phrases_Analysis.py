import json
import requests
def getlocation(data):
    for idx, val in enumerate(data):
        if val["lemma"]=="에서":
            locationjson=data.pop(idx-1) # data에서 이마트는 빠져나감
            return locationjson["lemma"]

def knownmany(data):
    word=data['lemma']
    if word=="하나" or word == "한" or word == "1":
        return 1
    elif word=="둘" or word == "두" or word=="2":
        return 2
    elif word == "셋" or word == "세" or word=="3":
        return 3
    elif word == "넷" or word == "네" or word=="4":
        return 4
    elif word == "다섯" or word == "5":
        return 5
    elif word == "여섯" or word == "6":
        return 6
    elif word == "일곱" or word == "7":
        return 7
    elif word == "여덟" or word == "8":
        return 8
    elif word == "아홉" or word== "9":
        return 9
    elif word == "열" or word=="10":
        return 10

def getNNGNNP(data):
    NRfind=False
    # arraylist=[]
    NNPNNGlist={}
    product=""
    number=0
    for idx, val in enumerate(data):
        if NRfind==False:
            if val["type"] == "NNG" or val["type"] == "NNP":
                product = val ["lemma"]
                NRfind = True
                print(product)
        else:
            if val["type"] == "MM" or val["type"] == "NR" or val["type"]=="SN":
                number = knownmany(val)
                NRfind = False
                NNPNNGlist.update([("제품",product)])
                NNPNNGlist.update([("수량",number)])
                print(number)
                product = ""
                number = 0
                print(NNPNNGlist)
                return NNPNNGlist
                # arraylist.append(NNPNNGlist)
                # NNPNNGlist={}
            # else:
            #     number = 1
            #     NNPNNGlist.update([("제품", product)])
            #     NNPNNGlist.update([("수량", number)])
            #     product = ""
            #     number = 0
            #     arraylist.append(NNPNNGlist)
            #     NNPNNGlist={}
    # return arraylist

def getNNGNNPArray(data):
    NRfind=False
    arraylist=[]
    NNPNNGlist={}
    product=""
    number=0
    for idx, val in enumerate(data):
        if NRfind==False:
            if val["type"] == "NNG" or val["type"] == "NNP":
                product = val ["lemma"]
                NRfind = True
                print(product)
        else:
            if val["type"] == "MM" or val["type"] == "NR" or val["type"]=="SN":
                number = knownmany(val)
                NRfind = False
                NNPNNGlist.update([("제품",product)])
                NNPNNGlist.update([("수량",number)])
                print(number)
                product = ""
                number = 0
                print(NNPNNGlist)
                arraylist.append(NNPNNGlist)
                NNPNNGlist={}
            # else:
            #     number = 1
            #     NNPNNGlist.update([("제품", product)])
            #     NNPNNGlist.update([("수량", number)])
            #     product = ""
            #     number = 0
            #     arraylist.append(NNPNNGlist)
            #     NNPNNGlist={}
    return arraylist


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
