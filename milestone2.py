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
searchObject = open(r"C:\Users\HP\Desktop\KLA hackathon\Milestone_Input\Milestone_Input\Milestone 2\Source.txt","r")
templateObject = open(r"C:\Users\HP\Desktop\KLA hackathon\Milestone_Input\Milestone_Input\Milestone 2\POI.txt","r")


writeObject=open(r"C:\Users\HP\Desktop\KLA hackathon\Milestone_Input\Milestone_Input\Milestone 2\output2.txt","w")


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




templatePolygons=partition1[2].split("endel")
templatePolygonCoorstr=templatePolygons[0].split()[6:]
templatePolygonCoor=[]
for i in range(0, len(templatePolygonCoorstr), 2):
    templatePolygonCoor.append([int(templatePolygonCoorstr[i]), int(templatePolygonCoorstr[i + 1])])
templateArea,templatePeri=find_area_perim(templatePolygonCoor)
templateArea=abs(templateArea)

writeText=""
writeText+=header
resInd=[]

for i in range(len(searchPolygonCoor)):
    searchArea,searchPeri=find_area_perim(searchPolygonCoor[i])
    if searchArea==templateArea and searchPeri==templatePeri:
        resInd.append(i)
#print(resInd)

for i in resInd:
    writeText+=searchPolygons[i]+'endel'

#writing the header
writeObject.write(writeText)

#closing the file objects
searchObject.close()
templateObject.close()
writeObject.close()