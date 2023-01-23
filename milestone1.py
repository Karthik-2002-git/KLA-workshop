#diff objects for reading n writing
readObject = open(r"C:\Users\HP\Desktop\KLA hackathon\Milestone_Input\Milestone_Input\Milestone 1\Format_Source.txt","r")
writeObject=open(r"C:\Users\HP\Desktop\KLA hackathon\Milestone_Input\Milestone_Input\Milestone 1\output1.txt","w")


readText=readObject.read()

#extracting the header from read file
partition=readText.partition('boundary')
header=partition[0]
#print(header)

writeText=""
writeText+=header+partition[1]

polygons=partition[2].split("endel", 2)
#print(polygons)
polygons[0]+='endel'
polygons[1]+='endel'
writeText+=polygons[0]+polygons[1]

#print(writeText)
#writing the header
writeObject.write(writeText)

#closing the file objects
readObject.close()
writeObject.close()