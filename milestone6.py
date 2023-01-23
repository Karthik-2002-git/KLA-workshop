import math
def find_area_perim(array):
    a = 0
    p = 0
    ox,oy = array[0]
    for x,y in array[1:]:
        a += (x*oy-y*ox)
        p += abs((x-ox)+(y-oy)*1j)
        ox,oy = x,y
    return a/2,p
#diff objects for reading n writing
searchObject = open(r"C:\Users\HP\Desktop\KLA hackathon\Milestone_Input\Milestone_Input\Milestone 6\Source.txt","r")
templateObject = open(r"C:\Users\HP\Desktop\KLA hackathon\Milestone_Input\Milestone_Input\Milestone 6\POI.txt","r")


writeObject=open(r"C:\Users\HP\Desktop\KLA hackathon\Milestone_Input\Milestone_Input\Milestone 6\output6.txt","w")


readSearch=searchObject.read()
readTemplate=templateObject.read()

#extracting the header from read file
#Search polygon
partition=readSearch.partition('boundary')
header=partition[0]



#template polygon
partition1=readTemplate.partition('boundary')
header1=partition1[0]



searchPolygons=partition[2].split("endel")
#print(searchPolygons)
searchPolygons[0]='\nboundary'+searchPolygons[0]

#print(searchPolygons)
searchPolygonCoorstr=[searchPolygons[i].split()[7:] for i in range(len(searchPolygons))]

searchPolygonCoorstr=searchPolygonCoorstr[:-1]
searchPolygonCoor=[]

for poly in searchPolygonCoorstr:
    temp=[]
    for i in range (0,len(poly),2):
        temp.append([int(poly[i]),int(poly[i+1])])
    searchPolygonCoor.append(temp)

searchPolygonDist=[[math.dist(searchPolygonCoor[j][i],searchPolygonCoor[j][i+1]) for i in range (len(searchPolygonCoor[j])-1)] for j in range(len(searchPolygonCoor))]


templatePolygons=partition1[2].split("endel")
templatePolygons[0]='\nboundary'+templatePolygons[0]
templatePolygonCoorstr=[templatePolygons[i].split()[7:] for i in range(len(templatePolygons))]
templatePolygonCoor=[]



searchPolygonVertices=[int(searchPolygons[i].split()[6]) for i in range(len(searchPolygons)-1)]
templatedPolygonVertices=[int(templatePolygons[i].split()[6]) for i in range(len(templatePolygons)-1)]

searchPolygonLayer=[int(searchPolygons[i].split()[2]) for i in range(len(searchPolygons)-1)]
templatePolygonLayer=[int(templatePolygons[i].split()[2]) for i in range(len(templatePolygons)-1)]


#print(templatedPolygonVertices)
for poly in templatePolygonCoorstr:
    temp=[]
    for i in range (0,len(poly),2):
        temp.append([int(poly[i]),int(poly[i+1])])
    templatePolygonCoor.append(temp)
templatePolygonCoor=templatePolygonCoor[:-1]

templatedist=[[math.dist(templatePolygonCoor[j][i],templatePolygonCoor[j][i+1]) for i in range (len(templatePolygonCoor[j])-1)] for j in range(len(templatePolygonCoor))]
ratio=[]

for i in range(len(templatedist)):
   for j in range(len(searchPolygonDist)):
       if len(templatedist[i])==len(searchPolygonDist[j]):
           ratio.append([templatedist[i][k]/searchPolygonDist[j][k] for k in range(len(templatedist[i]))])
       else:
           ratio.append(0)
perfectRatioInd=[]

for i in range(len(ratio)):
    ini=ratio[i][0]
    flag=1
    for j in range(1,len(ratio[i])):
        if ratio[i][j]!=ini:
            flag=0
    if flag:
        perfectRatioInd.append(i)
print(len(perfectRatioInd))



expected=[]
for i in templatePolygonCoor:
    templateArea,templatePeri=find_area_perim(i)
    templateArea=abs(templateArea)
    expected.append([templateArea,templatePeri])

writeText=""
writeText+=header

'''
resInd=[]

for i in range(len(searchPolygonCoor)):
    searchArea,searchPeri=find_area_perim(searchPolygonCoor[i])

    if [searchArea,searchPeri] in expected:
        ind=expected.index([searchArea,searchPeri])
        if templatedPolygonVertices[ind]==searchPolygonVertices[i] and templatePolygonLayer[ind]==searchPolygonLayer[i]:

            resInd.append(i)
'''


#print(resInd)

for i in perfectRatioInd:
    writeText+=searchPolygons[i]+'endel'

#writing the header
writeObject.write(writeText)

#closing the file objects
searchObject.close()
templateObject.close()
writeObject.close()