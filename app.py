from cbtl import getCbtlLocations
from sbux import getSbuxLocations
from scipy import spatial


c = getCbtlLocations()
s = getSbuxLocations()
def getNeighbour(c): # takes in cbtl object and searches for nearest sbux neighbour
    global s
    coordList = []
    for x in s:
        coordList.append(x[0])
    tree = spatial.KDTree(coordList)
    nearestIndex = tree.query(c[0])[1]
    print("CBTL: " + c[1] + " - SBUX: " + s[nearestIndex][1])




print(str(len(c)) + " CBTL locations")
print(str(len(s)) + " SBUX locations")

for store in c:
    getNeighbour(store)