import requests as r
import json

def getSbuxLocations():
    uri = "https://www.starbucks.com.sg/api/graphql?query=query%20MyQuery%20{%20store(orderBy:%20{displayText:%20ASC})%20{%20storeAmenities%20{%20termContentItems%20{%20displayText%20}%20}%20address%20coordinate%20{%20lat%20long%20}%20image%20{%20paths(first:%2010)%20}%20openingHours%20{%20contentItems%20{%20...%20on%20DataRow%20{%20key%20value%20}%20}%20}%20phone%20displayText%20contentItemId%20expiryDate%20publishDate%20}%20}"
    res = r.get(uri)
    data = json.loads(res.text)
    storeList = []
    for store in data['data']['store']:
        coords = store['coordinate']['lat'] + "," + store['coordinate']['long']
        location = store['displayText']
        splitCoords = coords.split(",")
        coords = (float(splitCoords[0]), float(splitCoords[1]))
        storeList.append([coords, location])
        
    return storeList