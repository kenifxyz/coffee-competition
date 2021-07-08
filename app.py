from cbtl import getCbtlLocations
from sbux import getSbuxLocations
from scipy import spatial
from math import sin, cos, sqrt, atan2, radians
from excel import createExcel
from Pair import Pair

c = getCbtlLocations()
s = getSbuxLocations()

def calcDistance(c, s):
    lat1 = radians(c[0][0])
    lon1 = radians(c[0][1])
    lat2 = radians(s[0][0])
    lon2 = radians(s[0][1])
    R = 6373.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    return distance
    
def getNeighbour(input, reverse=False): # takes in cbtl object and searches for nearest sbux neighbour
    if reverse:
        global c
        compare = c
    else:
        global s
        compare = s
    coordList = []
    for x in compare:
        coordList.append(x[0])
    tree = spatial.KDTree(coordList)
    nearestIndex = tree.query(input[0])[1]
    pair0 = "SBUX" if reverse else "CBTL"
    pair1 = "CBTL" if reverse else "SBUX"
    distance = calcDistance(input, compare[nearestIndex])
    print(pair0 + ": " + input[1] + " - " + pair1 + ": " + compare[nearestIndex][1])
    print("Distance: " + str(distance) + "km\n")
    return Pair(pair0, pair1, input[1], compare[nearestIndex][1], distance)


getNeighbour([(1.3969115322405228, 103.74695872789806), "Yew Tee Point (New)"])
print(str(len(c)) + " CBTL locations")
print(str(len(s)) + " SBUX locations")

# pairList = []
# for store in c:
#     pair = getNeighbour(store)
#     pairList.append(pair)

# createExcel(pairList)