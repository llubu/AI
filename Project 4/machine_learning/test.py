import math
import sys
from collections import OrderedDict

choices = ['Y', 'N', '?']
    
def readData():
    with open("train.data", "r") as f:
        data = f.read().splitlines();
        
    #print len(data), len(data[0])
    sanData = list()
    
    for item in data:
        resRow = list()
        #params = list()
        params = OrderedDict()
        
        row = item.split('\t')
        resRow.append(row[0])
        
        vals = row[1].split(',')
        i = 0
        
        for res in vals:
            if res == 'y':
                params[i] = 'y'
            if res == 'n':
                params[i] = 'n'
            if res == '?':
                params[i] = '?'        
            i += 1
        
        resRow.append(params)
        sanData.append(resRow)
        
    return sanData

    
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



#Function to compute best attribute, given a subset of the training data 
#Return index of best attribute and subsets after split on that attribute   
def bestAttr(curData):

    #Compute current entropy 
    curEnt = compEntropy([ row[0] for row in curData ])
    #print curEnt

    #Vars to store index of attribute which minimized entropy
    minEnt = sys.maxint 
    minInd = -1

    #Lists to store y,n,? subsets for attribute which minimizes entropy
    splitY = []
    splitN = []
    splitX = []

    #Compute Entropy for all attributes and find the attribute that leads to max drop in entropy
    for attr in curData[0][1].items():
        #print attr
        tabY = []
        tabN = []
        tabX = []

        #Split records on the basis of y,n,? into respective tables
        for row in curData:
            if row[1][attr[0]] == 'y':
                tabY.append(row)
            elif row[1][attr[0]] == 'n':
                tabN.append(row)
            elif row[1][attr[0]] == '?':
                tabX.append(row)
        
        subY = [item[0] for item in tabY]
        subN = [item[0] for item in tabN]
        subX = [item[0] for item in tabX]
        
        #Compute Entropy for this attribute
        totRecords = len(subY) + len(subN) + len(subX)
        attrEnt = ((float(len(subY))/totRecords) *  compEntropy(subY)) + ((float(len(subN))/totRecords) *  compEntropy(subN)) + ((float(len(subX))/totRecords) *  compEntropy(subX))

        #print "attrEnt: ", attrEnt
        #print ""
        
        if attrEnt < minEnt:
            minEnt = attrEnt
            minInd = attr[0]
            
            splitY = tabY
            splitN = tabN
            splitX = tabX
            
    #print minInd

    #print "Before: " , len(splitY[0][1])
    #We have to remove the attribute at minInd
    
    for i in range(len(splitY)):
        del splitY[i][1][minInd]
        
    for i in range(len(splitN)):
        del splitN[i][1][minInd]
        
    for i in range(len(splitX)):
        del splitX[i][1][minInd]
               
        
    #print "After: " , len(splitY[0][1])
    
    return minInd, [splitY, splitN, splitX]



#Function to create decision tree
def createDecisionTree(data):
    
    #print "Len data: " , len(data)
    #print data
    #print "\n\n\n"
    
    #If no attributes or no records are left, return majority class
    if len(data) == 0 or len(data[0][1]) == 0:
       return ""
       
    #If all records have the same class, return that class   
    if len(data) == [row[0] for row in data].count("republican"):
        # print "Rep! : " , [row[0] for row in data].count("republican")
        # print data
        # print "\n\n\n"
        return "republican"
    elif len(data) == [row[0] for row in data].count("democrat"):
        # print "Dem! : " , [row[0] for row in data].count("democrat"), ""
        # print data
        # print "\n\n\n"
        return "democrat"
        
         
    bAttr, subSet = bestAttr(data)
    decTree = {bAttr:{}}
    
    #print bAttr
    #print subSet[0]
    #print len(subSet[0][0][1])
    
    for i in range(len(choices)):
        subTree = createDecisionTree(subSet[i])
        decTree[bAttr][choices[i]] = subTree
    
    return decTree
    
sanData = readData()
#print sanData , "\n\n\n"  
print createDecisionTree(sanData)

