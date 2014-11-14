import sys
from question1_solver import *
from question2_solver import *
from question3_solver import *
from question4_solver import *
from question5_solver import *
from cpt import *
from time import time

def question1(cpt, test):
    file_name = "question1.txt";
    if test:
        file_name = "question1_test.txt";
    solver = Question1_Solver(cpt);
    correct = 0.0;
    total = 0.0;
    with open(file_name, "r") as f:
        data = f.read().splitlines();
    for row in data:
        instance = row.split();
        predict = solver.solve(instance[0]);
        if (instance[1] == predict):
            correct = correct + 1;
        total = total + 1;
    print "Question 1 accuracy: %f" % (correct / total);

def question2(cpt, test):
    file_name = "question2.txt";
    if test:
        file_name = "question2_test.txt";
    solver = Question2_Solver(cpt);
    correct = 0.0;
    partial_correct = 0.0;
    total = 0.0;
    with open(file_name, "r") as f:
        data = f.read().splitlines();
    for row in data:
        instance = row.split();
        predict = solver.solve(instance[0]);
        if (instance[1] == predict[0] and instance[2] == predict[1]):
            correct = correct + 1;
        if (instance[1] == predict[0] or instance[2] == predict[1]):
            partial_correct = partial_correct + 1;
        total = total + 1;
    print "Question 2 accuracy: %f (two correct letters)" % (correct / total);
    print "Question 2 accuracy: %f (at least one correct letter)" % \
          (partial_correct / total);

def question3(cpt, test):
    file_name = "question3.txt";
    if test:
        file_name = "question3_test.txt";
    solver = Question3_Solver(cpt);
    correct = 0.0;
    total = 0.0;
    with open(file_name, "r") as f:
        data = f.read().splitlines();
    for row in data:
        instance = row.split();
        predict = solver.solve(instance[0]);
        if (instance[1] == predict):
            correct = correct + 1;
        total = total + 1;
    print "Question 3 accuracy: %f" % (correct / total);

def question4(cpt, test):
    file_name = "question4.txt";
    if test:
        file_name = "question4_test.txt";
    solver = Question4_Solver(cpt);
    correct = 0.0;
    total = 0.0;
    with open(file_name, "r") as f:
        data = f.read().splitlines();
    for row in data:
        instance = row.split();
        predict = solver.solve(\
            [instance[0], instance[1], instance[2], instance[3]]);
        if (instance[4] == predict):
            correct = correct + 1;
        total = total + 1;
    print "Question 4 accuracy: %f" % (correct / total);

def question5(cpt2, test):
    file_name = "question5.txt";
    if test:
        file_name = "question5_test.txt";
    solver = Question5_Solver(cpt2);
    correct = 0.0;
    total = 0.0;
    with open(file_name, "r") as f:
        data = f.read().splitlines();
    for row in data:
        instance = row.split();
        predict = solver.solve(instance[0]);
        if (instance[1] == predict):
            correct = correct + 1;
        total = total + 1;
    print "Question 5 accuracy: %f" % (correct / total);

def main(argv):
    cpt = CPT();
    cpt2 = CPT_2Order();
    test = 0;
    for arg in argv:
        if arg == "--print_cpt":
            cpt.print_cpt();
    for arg in argv:
        if arg == "--test":
            test = 1;
    for arg in argv:
        if arg == "-q1":
            t0 = time();
            question1(cpt, test);
            t1 = time();
            print "Q1 time used: %f" % (t1 - t0), "secs.\n";
    for arg in argv:
        if arg == "-q2":
            t0 = time();
            question2(cpt, test);
            t1 = time();
            print "Q2 time used: %f" % (t1 - t0), "secs.\n";
    for arg in argv:
        if arg == "-q3":
            t0 = time();
            question3(cpt, test);
            t1 = time();
            print "Q3 time used: %f" % (t1 - t0), "secs.\n";
    for arg in argv:
        if arg == "-q4":
            t0 = time();
            question4(cpt, test);
            t1 = time();
            print "Q4 time used: %f" % (t1 - t0), "secs.\n";
    for arg in argv:
        if arg == "-q5":
            t0 = time();
            question5(cpt2, test);
            t1 = time();
            print "Q5 time used: %f" % (t1 - t0), "secs.\n";

if __name__ == "__main__":
    main(sys.argv);

