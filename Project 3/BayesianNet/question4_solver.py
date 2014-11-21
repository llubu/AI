import math
import sys

class Question4_Solver:
    def __init__(self, cpt):
        self.cpt = cpt;
        self.skip1 = self.createTable1()
        self.skip2 = self.createTable2()


    #####################################
    # ADD YOUR CODE HERE
    # Pr(x|y) = self.cpt.conditional_prob(x, y);
    # A word begins with "`" and ends with "`".
    # For example, the probability of word "ab":
    # Pr("ab") = \
    #    self.cpt.conditional_prob("a", "`") * \
    #    self.cpt.conditional_prob("b", "a") * \
    #    self.cpt.conditional_prob("`", "b");
    # query example:
    #    query: ["que-_-on", "--_--icial",
    #            "in_elligence", "inter--_"];
    #    return "t";
    def solve(self, query):
        """
        Solves the given cross wors and returns the
        valid character found
        """
        
        uS = [0 for i in range(0, 4)]               # Index of the underscore in the query
        prevDash = [0 for i in range(0, 4)]         # Count of dashes before the underscore
        afterDash = [0 for i in range(0, 4)]        # Count of dashes after the underscore
        leftch = [0 for i in range(0, 4)]           # Index of valid char before the leftmost dash
        rtch = [0 for i in range(0, 4)]             # Index of valid char after the rightmost dash
        
        #print '\n'
        #print uS, prevDash, afterDash, leftch, rtch
        
        for i in range(0, 4):                       # get all the values for 4 words in the query
            tmp = '`' + query[i] + '`'
            uS[i] = tmp.index('_')
            tmp1 = tmp.split('_')
            #print tmp
            prevDash[i] = tmp1[0].count('-')
            afterDash[i] = tmp1[1].count('-')
            
        
            if  0 != (uS[i] - prevDash[i]):
                leftch[i] = tmp[uS[i]-prevDash[i] -1]
            else:
                leftch[i] = tmp[uS[i]-prevDash[i]]
                
            #print query[i]    
            #print "tmp len: ", len(tmp)
            #print uS[i]
            #print afterDash[i]
                
            if len(tmp) != (uS[i] + afterDash[i]):
                rtch[i] = tmp[uS[i]+afterDash[i] +1]
            else:
                rtch[i] = tmp[uS[i]+afterDash[i]]
                
        #print "pd: " , prevDash, ' ad :' , afterDash, ' lc :' , leftch, ' rc :', rtch
        
        leftsum = 0     # Sum of probabilities for the left dashes
        rtsum = 0       # Sum of probabilities for the right dashes
        maxSum = -1     # MAx sum found so far
        maxChar = '?'   # character corresponding to maxSum
        
        numZero = 0
        zeroList = []
        for i in range(4):
            if prevDash[i]*afterDash[i] == 0:
                numZero += 1
                zeroList.append(0)
            else:
                zeroList.append(1)
        
        #print numZero, zeroList
        
        for i in range(0, 26):
            ksum = 1
            
            for k in range(0, 4):   # Loop to consider all the 4 words in the query
            
                if (numZero > 1  and zeroList[k] == 0) or (numZero < 2):
                
                    if (0 == prevDash[k]):
                        leftsum = self.cpt.conditional_prob(chr(97+i) ,leftch[k])
                    if (1 == prevDash[k]):
                        leftsum = self.skip1[chr(97+i), leftch[k]]
                    if (2 == prevDash[k]):
                        leftsum = self.skip2[chr(97+i), leftch[k]]
                        
                    if (0 == afterDash[k]):
                        rtsum = self.cpt.conditional_prob(rtch[k], chr(97+i))
                    if (1 == afterDash[k]):
                        rtsum = self.skip1[rtch[k], chr(97+i)]
                    if (2 == afterDash):    
                        rtsum = self.skip2[rtch[k], chr(97+i)]
                        
                        
                    ksum *= leftsum*rtsum
                #if leftsum != 0 and rtsum != 0:
                #    ksum += math.log(leftsum) + math.log(rtsum)
                #else:
                #    ksum = -sys.maxint - 2
                
            #print query, chr(97+i), ksum 
                
            if ( maxSum < ksum ):
                maxSum = ksum
                maxChar = chr(97+i)
        
        #print maxChar, query
        return maxChar;
    
    
    def createTable1(self):
        """
        Creates the lookup table to help eliminate hidden var 1
        """
        table= dict()
        
        for i in range(0,27):
            prev = chr(96+i)
            for j in range(0, 27):
                sum = 0
                cur = chr(96+j)
                for k in range(0, 27):
                    sum += self.cpt.conditional_prob(chr(96+k), prev) * self.cpt.conditional_prob(cur, chr(96+k))
                    
                table[prev,cur] = sum
                
        return table
        
    def createTable2(self):
        """
        Creates the lookup table to help eliminate hidden var 2
        """
        table = dict()
        
        for i in range(0, 27):
            prev = chr(96+i)
            for j in range(0, 27):
                sum = 0
                cur = chr(96+j)
                for k in range(0, 27):
                    sum += self.skip1[chr(96+k), prev] * self.cpt.conditional_prob(cur, chr(96+k))
                
                table[prev, cur] = sum
        return table


