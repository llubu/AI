class Question3_Solver:
    
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
    #    query: "qu--_--n";
    #    return "t";
    
    def solve(self, query):
        """
        This function solves the given querry and
        returns the letter which is most suitable.
        """
        
        query = '`' + query + '`'  # Adding string end delimiters
        uS = query.index('_')      # index of the underscore in the query string
        tmp = query.split('_')       
        #print tmp
        prevDash = tmp[0].count('-')  # Count of dashes before the underScore
        afterDash = tmp[1].count('-') # Count of dashes after the underScore
        #print prevDash, afterDash
        
        if  0 != (uS - prevDash):
            leftch = query[uS-prevDash -1]  # Index of valid character before leftmost dash
        else:
            leftch = query[uS-prevDash]
        
        if len(query) != (uS + afterDash):
            rtch = query[uS+afterDash +1]   # Index of valid character after rightmost dash
        else:
            rtch = query[uS+afterDash]
            
        #print leftch, rtch
        
        leftsum = 0     # Sum of probalities for left dashes
        rtsum = 0       # Sum of probabilities for right dashes
        maxSum = -1     # Max sum for a particular letter in the loop
        maxChar = '?'   # The character with maxSum
        
        for i in range(0, 26):
            if (0 == prevDash):
                leftsum = self.cpt.conditional_prob(chr(97+i) ,leftch)
            if (1 == prevDash):
                leftsum = self.skip1[chr(97+i), leftch]
            if (2 == prevDash):
                leftsum = self.skip2[chr(97+i), leftch]
                
            if (0 == afterDash):
                rtsum = self.cpt.conditional_prob(rtch, chr(97+i))
            if (1 == afterDash):
                rtsum = self.skip1[rtch, chr(97+i)]
            if (2 == afterDash):
                rtsum = self.skip2[rtch, chr(97+i)]
                
            fiSum = leftsum*rtsum
            if ( maxSum < fiSum ):
                maxSum = fiSum
                maxChar = chr(97+i) 
            
                
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
        
                
    

