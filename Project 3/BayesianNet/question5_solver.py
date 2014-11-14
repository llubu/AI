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
    #    return "t";
    def solve(self, query):
        return "t";

