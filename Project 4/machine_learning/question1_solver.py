import math
import sys  
from collections import OrderedDict
choices = ['y', 'n', '?']

class Question1_Solver:

    def __init__(self):
        self.learn('train.data');
        return;

    # Add your code here.
    # Read training data and build yo   ur decision tree
    # Store the decision tree in this class
    # This function runs only once when initializing
    # Please read and only read train_data: 'train.data'
    def learn(self, train_data):
        
        #Read training data file
        def readData():
            with open("train.data", "r") as f:
                data = f.read().splitlines();
        
            sanData = list()
            
            for item in data:
                resRow = list()
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

        #Given data, find majority class
        def majority(data):

            dem = [row[0] for row in data].count("democrat")  
            rep = [row[0] for row in data].count("republican") 
            
            if dem > rep : 
                return "democrat"
            else:
                return "republican"
            
        #Compute entropy given data     
        def compEntropy(table):
 
            if len(table) == 0:
                return 0
            
            numRep = table.count("republican")
            numDem = table.count("democrat")
            total = len(table)
            
            probRep = float(numRep) / total
            probDem = float(numDem) / total
            
            if probDem != 0 and probRep != 0:
                entropy = -(probRep * math.log(probRep, 2)) -(probDem * math.log(probDem,2))
            else:
                entropy = 0
            
            return entropy

            
        #Function to compute best attribute, given a subset of the training data 
        #Return index of best attribute and subsets after split on that attribute   
        def bestAttr(curData):

            #Compute current entropy 
            curEnt = compEntropy([ row[0] for row in curData ])

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

                #Keep track of attribute with minimum entropy
                if attrEnt < minEnt:
                    minEnt = attrEnt
                    minInd = attr[0]
                    
                    splitY = tabY
                    splitN = tabN
                    splitX = tabX
             
            #Delete minimum entropy attribute    
            for i in range(len(splitY)):
                del splitY[i][1][minInd]
                
            for i in range(len(splitN)):
                del splitN[i][1][minInd]
                
            for i in range(len(splitX)):
                del splitX[i][1][minInd]
                       
            
            return minInd, [splitY, splitN, splitX]


        #Recursive function to create decision tree
        def createDecisionTree(data, maj):
            
            #If no attributes or no records are left, return majority class
            if len(data) == 0 or len(data[0][1]) == 0:
               return maj
               
            #If all records have the same class, return that class   
            if len(data) == [row[0] for row in data].count("republican"):
                return "republican"         
            elif len(data) == [row[0] for row in data].count("democrat"):
                return "democrat"
                
            #Pruning : If only 1 democrat/republican and total records > 5, return the majority class    
            if [row[0] for row in data].count("republican") == 1 and len(data) > 5:
                return 'democrat'
            elif [row[0] for row in data].count("democrat") == 1 and len(data) > 5:
                return 'republican'
            
            #Get best attribute and subsets
            bAttr, subSet = bestAttr(data)
            decTree = {bAttr:{}}
            
            #Iterate over y,n,? and generate subtrees
            for i in range(len(choices)):
                subMaj = majority(subSet[i])
                subTree = createDecisionTree(subSet[i], subMaj)
                decTree[bAttr][choices[i]] = subTree
                
            return decTree

        #Create Decision Tree    
        sanData = readData()
        maj = majority(sanData)
        self.decTree = createDecisionTree(sanData, maj)
    
        return;

        
    # Add your code here.
    # Use the learned decision tree to predict
    # query example: 'n,y,n,y,y,y,n,n,n,y,?,y,y,y,n,y'
    # return 'republican' or 'republican'
    def solve(self, query):
        
        attr = query.split(',')
        tree = self.decTree
        
        while (tree != "democrat" or tree != "republican"):
            key = tree.keys()
            tree = tree[key[0]][attr[key[0]]] #Get SubTree

            if tree == 'republican':
                return 'republican'
            elif tree == 'democrat':
                return 'democrat'
    
        return tree;

