class Question5_Solver:
    def __init__(self, cpt2):
        self.cpt2 = cpt2;
        return;

    #####################################
    # ADD YOUR CODE HERE
    #         _________
    #        |         v
    # Given  z -> y -> x
    # Pr(x|z,y) = self.cpt2.conditional_prob(x, z, y);
    #
    # A word begins with "``" and ends with "``".
    # For example, the probability of word "ab":
    # Pr("ab") = \
    #    self.cpt2.conditional_prob("a", "`", "`") * \
    #    self.cpt2.conditional_prob("b", "`", "a") * \
    #    self.cpt2.conditional_prob("`", "a", "b") * \
    #    self.cpt2.conditional_prob("`", "b", "`");
    # query example:
    #    query: "ques_ion";
    #    return "t"
	
	
    def solve(self, query):
        
        #Adding ` to beginning and end of word to simplify logic
        tmpWord = '``' + query + '``'

        index = -1
        
        #Search for index of _ in word
        for char in tmpWord:
            index += 1
            if char == "_":
                break
        
        #print "Break!!!"
        
        
        #Characters before and after _
        before1 = tmpWord[index-2]
        before2 = tmpWord[index-1]
        after1 = tmpWord[index+1]
        after2 = tmpWord[index+2]
        
        #print "Before, After : " , before, after
         
        #Variables to keep track of maximum probability and the characters     
        maxProb = -1
        maxChar = "a"
        
        #Loop over all alphabets and find the character that results in highest probability
        for i in xrange(97,123): 
            char = chr(i)
            currProb = self.cpt2.conditional_prob(char, before1, before2) * self.cpt2.conditional_prob(after1 , before2, char) * self.cpt2.conditional_prob(after2 , char, after1) 
            if currProb > maxProb:
                maxProb = currProb
                maxChar = char
                

        return maxChar;

