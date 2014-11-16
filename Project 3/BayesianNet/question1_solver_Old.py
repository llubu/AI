class Question1_Solver:
    def __init__(self, cpt):
        self.cpt = cpt;
        print self.cpt.conditional_prob("`", "b")
        return;

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
    #    query: "ques_ion";
    #    return "t";     
    
    
    def solve(self, query):
        
        tmpWord = '`' + query + '`'
        prevChar = '`'
        prob = 1
        finList = []
        
        #print tmpWord
        index = -1
        
        for char in tmpWord:
            index += 1
            if char == "_":
                break
        
        #print index
        
        #=======================================================================
        # for char in tmpWord[1:index]:
        #     #print prevChar, char
        #     prob *= self.cpt.conditional_prob(char, prevChar)
        #     prevChar = char
        #=======================================================================
        
        #print "Break!!!"
        
        before = tmpWord[index-1]
        after = tmpWord[index+1]
        
        #print "Before, After : " , before, after
        
        
            
        #=======================================================================
        # prevChar = after
        # for char in tmpWord[index+2:]:
        #     #print prevChar, char
        #     prob *= self.cpt.conditional_prob(char, prevChar)
        #     prevChar = char
        #=======================================================================
            
        maxProb = -1
        maxChar = "a"
        
        for i in xrange(97,123): 
            #newProb = prob * self.cpt.conditional_prob(chr(i), before) * self.cpt.conditional_prob(after , chr(i))
            char = chr(i)
            currProb = self.cpt.conditional_prob(char, before) * self.cpt.conditional_prob(after , char)
            if currProb > maxProb:
                maxProb = currProb
                maxChar = char
                
                
            
            #finList.append([chr(i), newProb])
        
        #finList.sort(key=lambda x: x[1])
        #print finList
        #res =  finList[25][0]
        #print res
        #print "\n\n\n"
        
        

        
        
        return maxChar;


