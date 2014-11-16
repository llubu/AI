class Question1_Solver:
    def __init__(self, cpt):
        self.cpt = cpt;
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

        index = -1
        
        for char in tmpWord:
            index += 1
            if char == "_":
                break
        
        #print "Break!!!"
        
        before = tmpWord[index-1]
        after = tmpWord[index+1]
        
        #print "Before, After : " , before, after
            
        maxProb = -1
        maxChar = "a"
        
        for i in xrange(97,123): 
            char = chr(i)
            currProb = self.cpt.conditional_prob(char, before) * self.cpt.conditional_prob(after , char)
            if currProb > maxProb:
                maxProb = currProb
                maxChar = char
                

        return maxChar;


