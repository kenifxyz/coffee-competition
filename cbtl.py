from numpy.lib.shape_base import split
import requests as r
from bs4 import BeautifulSoup


def getCbtlLocations(excludeClosed=False):
    uri = "https://www.coffeebean.com.sg/stores"
    res = r.get(uri)
    soup = BeautifulSoup(res.text)

    storeDiv = soup.find(id="store-pickup-list-store")

    stores = storeDiv.find_all("div", {"class": "store-pickup-list-store-item"})


    storeList = []
    for store in stores:
        store = str(store)
        coords = store.split("calculateDistances(")[1].split(", '")[0]
        location = store.split(coords + ", '")[1].split("&lt;")[0]
        if location == "Hougang Mall": #the only exception
            coords = "1.3725894,103.8937225"
        elif ("0.000" in coords or (excludeClosed and "Temporarily Closed" in location)):
            continue
        else:
            coords = coords.replace(" ", "")
            location = location.replace("\\", "")
        splitCoords = coords.split(",")
        coords = (float(splitCoords[0]), float(splitCoords[1]))
        storeList.append([coords, location])

    return storeList
