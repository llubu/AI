from collections import OrderedDict

class Question2_Solver:
    def __init__(self):
        self.learn('train.data');
        self.classes = ['democrat' , 'republican']
        self.resp = ['y' , 'n' , '?']
        
        return;
    
        
    # Add your code here.
    # Read training data and build your naive bayes classifier
    # Store the classifier in this class
    # This function runs only once when initializing
    # Please read and only read train_data: 'train.data'
    def learn(self, train_data):
        sanData = self.readData()
        print len(sanData)
        
        classList = [row[0] for row in sanData]
        self.numDem = classList.count('democrat')
        self.numRep = classList.count('republican')
        
        self.demProb = float(self.numDem)/len(sanData)
        self.repProb = float(self.numRep)/len(sanData)
        
        #self.numDem += 3
        #self.numRep += 3
        
        print self.demProb, self.repProb
        
        #Dicts to store probabilities
        self.demDict = dict() # Dict has a dict for each attr
        self.repDict = dict()

        for attr in range(16):
            
            #i = float(1)
            i = 0
            
            numY = i
            numN = i
            numX = i
            numYr = i
            numNr = i
            numXr = i
            
            for row in sanData:
                if row[0] == 'democrat':
                    if row[1][attr] == 'y':
                        numY += 1
                    elif row[1][attr] == 'n':
                        numN += 1
                    elif row[1][attr] == '?':
                        numX += 1
                        
                elif row[0] == 'republican':
                    if row[1][attr] == 'y':
                        numYr += 1
                    elif row[1][attr] == 'n':
                        numNr += 1
                    elif row[1][attr] == '?':
                        numXr += 1
                        
            self.demDict[attr] = {'y':(float(numY))/self.numDem, 'n':(float(numN))/self.numDem, '?':(float(numX))/self.numDem}
            self.repDict[attr] = {'y':(float(numYr))/self.numRep, 'n':(float(numNr))/self.numRep, '?':(float(numXr))/self.numRep}

            
        #print self.repDict
        
        
        return;

    # Add your code here.
    # Use the learned naive bayes classifier to predict
    # query example: 'n,y,n,y,y,y,n,n,n,y,?,y,y,y,n,y'
    # return 'republican' or 'republican'
    def solve(self, query):
    
        attrList =  query.split(',')
        
        dem = self.demProb
        rep = self.repProb
        
        for i in range(len(attrList)):
            dem *= self.demDict[i][attrList[i]]
            rep *= self.repDict[i][attrList[i]]
        
        if dem >= rep:
            return 'democrat'
        else:
            return 'republican'


        
    
    def readData(self):
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