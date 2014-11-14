class CPT:
    def __init__(self):
        self.create_cpt();

    def add_cpt_count(self, word):
        pre_i = 0;
        for cur_c in word:
            cur_i = ord(cur_c) - 96;
            self.cpt[pre_i][cur_i] = self.cpt[pre_i][cur_i] + 1;
            pre_i = cur_i;
        self.cpt[pre_i][0] = self.cpt[pre_i][0] + 1;

    def create_cpt(self):
        self.cpt = [[0.0] * 27 for i in range(27)];
        #####################################
        # Read dictionSample.txt and build the Conditional Probability Table (CPT).
        with open("dictionSample.txt", "r") as f:
            data = f.read().splitlines();
        for row in data:
            self.add_cpt_count(row);
        for i in range(0, 27):
            s = sum(self.cpt[i]);
            for j in range(0, 27):
                self.cpt[i][j] = self.cpt[i][j] / s;

    def print_cpt(self):
        print "%     `    a    b    c    d    e    f    " \
              "g    h    i    j    k    l    m    n    " \
              "o    p    q    r    s    t    u    v    w    x    y    z";
        print "===========================================" \
              "===========================================" \
              "====================================================";
        print "`", "|", "|".join(str("%.1f" % (p*100)).rjust(4, ' ') for p in self.cpt[0])
        for i in range(1, 27):
            print chr(i + 96), "|", \
                  "|".join(str("%.1f" % (p*100)).rjust(4, ' ') for p in self.cpt[i])
        for i in range(0, 27):
            s = sum(self.cpt[i]);
            if abs(s - 1.0) > 0.01:
                print "[ERROR] The conditional probability of Pr(*|%s) " \
                      "does not add up to 1 (actual: %f)." % (chr(i + 96), s);

    def conditional_prob(self, v, given):
        return self.cpt[ord(given) - 96][ord(v) - 96];


class CPT_2Order:
    def __init__(self):
        self.create_cpt();

    def add_cpt_count(self, word):
        ppp_i = 0;
        pre_i = 0;
        for cur_c in word:
            cur_i = ord(cur_c) - 96;
            self.cpt[ppp_i*27+pre_i][cur_i] = self.cpt[ppp_i*27+pre_i][cur_i] + 1;
            ppp_i = pre_i;
            pre_i = cur_i;
        self.cpt[ppp_i*27+pre_i][0] = self.cpt[ppp_i*27+pre_i][0] + 1;
        self.cpt[pre_i*27+0][0] = self.cpt[pre_i*27+0][0] + 1;

    def create_cpt(self):
        self.cpt = [[0.1] * 27 for i in range(27*27)];
        #####################################
        # Read dictionSample.txt and build the Conditional Probability Table (CPT).
        with open("dictionSample.txt", "r") as f:
            data = f.read().splitlines();
        for row in data:
            self.add_cpt_count(row);
        for i in range(0, 27*27):
            s = sum(self.cpt[i]);
            for j in range(0, 27):
                self.cpt[i][j] = self.cpt[i][j] / s;

    def conditional_prob(self, v, given1, given2):
        return self.cpt[(ord(given1) - 96) * 27 + ord(given2) - 96][ord(v) - 96];


