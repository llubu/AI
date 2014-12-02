import math
import sys

def compEntropy(table):
    
    #print table
    
    if len(table) == 0:
        return 0
    
    numRep = table.count("republican")
    numDem = table.count("democrat")
    total = len(table)
    
    probRep = float(numRep) / total
    probDem = float(numDem) / total
    
    # print "probRep: " , probRep
    # print "probDem: " , probDem
    
    if probDem != 0 and probRep != 0:
        entropy = -(probRep * math.log(probRep, 2)) -(probDem * math.log(probDem,2))
    else:
        entropy = 0
    
    #print probRep, probDem
    
    return entropy
    
    
with open("train.data", "r") as f:
    data = f.read().splitlines();
    
print len(data), len(data[0])

sanData = list()

for item in data:

    resRow = list()
    params = list()
    
    row = item.split('\t')
    resRow.append(row[0])
    
    vals = row[1].split(',')
    
    i = 0
    for res in vals:
        if res == 'y':
            params.append('y')
        if res == 'n':
            params.append('n')
        if res == '?':
            params.append('?')        
    i += 1
    
    resRow.append(params)
    sanData.append(resRow)

curData = sanData
    


#Compute current entropy 
curEnt = compEntropy([ row[0] for row in curData ])
print curEnt

#Vars to store index of attribute which minimized entropy
minEnt = sys.maxint 
minInd = -1

#Lists to store y,n,? subsets for attribute which minimizes entropy
splitY = []
splitN = []
splitX = []

#Compute Entropy for all attributes and find the attribute that leads to max drop in entropy
for i in range(len(curData[0][1])):
    print i
    tabY = []
    tabN = []
    tabX = []

    #Split records on the basis of y,n,? into respective tables
    for j in range(len(curData)):
        if curData[j][1][i] == 'y':
            tabY.append(curData[j])
        elif curData[j][1][i] == 'n':
            tabN.append(curData[j])
        elif curData[j][1][i] == '?':
            tabX.append(curData[j])
    
    subY = [row[0] for row in tabY]
    subN = [row[0] for row in tabN]
    subX = [row[0] for row in tabX]
    
    #Compute Entropy for this attribute
    totRecords = len(subY) + len(subN) + len(subX)
    attrEnt = ((float(len(subY))/totRecords) *  compEntropy(subY)) + ((float(len(subN))/totRecords) *  compEntropy(subN)) + ((float(len(subX))/totRecords) *  compEntropy(subX))

    print "attrEnt: ", attrEnt
    print ""
    
    if attrEnt < minEnt:
        minEnt = attrEnt
        minInd = i
        
        splitY = tabY
        splitN = tabN
        splitX = tabX

        
print minInd

#We have to remove the attribute at minInd
for i in range(len(splitY)):
    del splitY[i][1][minInd]
for i in range(len(splitN)):
    del splitN[i][1][minInd]
for i in range(len(splitX)):
    del splitX[i][1][minInd]    




#We now have 3 subsets to recurse on    
    
# print "after: " , len(splitY[0][1])
# print splitY[0][1]
        



#Split on the basis of attribute at index minInd
    
    
    
# print tabY
# print ""
# print tabN
# print tabX

#for item in sanData:
    #print item

