class Question2_Solver:
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
    #    query: "que__ion";
    #    return ["s", "t"];
    
    
    def solve(self, query): 
        
        #Adding ` to beginning and end of word to simplify logic
        tmpWord = '`' + query + '`'

        index = -1
        
        #Search for index of _ in word
        for char in tmpWord:
            index += 1
            if char == "_":
                break
        
        #print "Break!!!"

        #Character before and after _
        before = tmpWord[index-1]
        after = tmpWord[index+2]
        
        #print "Before, After : " , before, after
        
        #Variables to keep track of maximum probability and the characters    
        maxProb = -1
        maxChar1 = "a"
        maxChar2 = "b"
        
        #Loop over all combinations of two alphabets and find the characters that result in highest probability
        for i in xrange(97,123):
            for j in xrange(97,123):  
                char1 = chr(i)
                char2 = chr(j)
                
                currProb = self.cpt.conditional_prob(char1, before) * self.cpt.conditional_prob(char2, char1) * self.cpt.conditional_prob(after , char2)
                
                if currProb > maxProb:
                    maxProb = currProb
                    maxChar1 = char1
                    maxChar2 = char2
                
        
        
        return [maxChar1, maxChar2];


