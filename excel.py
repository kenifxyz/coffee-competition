import xlsxwriter
from Pair import Pair

def createExcel(pairList):
    workbook = xlsxwriter.Workbook('coffee-comp.xlsx')
    worksheet = workbook.add_worksheet()
    data = [["Pair0", "Pair1", "Distance (km)"]]
    for pair in pairList:
        data.append([pair.location0, pair.location1, pair.distance])
    row = 0
    col = 0
    for location0, location1, distance in (data):
        print("writing " + location0)
        worksheet.write(row, col,     location0)
        worksheet.write(row, col + 1, location1)
        worksheet.write(row, col + 2, distance)
        row += 1
    workbook.close()