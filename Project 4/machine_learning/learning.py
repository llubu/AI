import sys
from graphics import *
from question1_solver import *
from question2_solver import *
from question3_solver import *
from time import time

def question1():
    solver = Question1_Solver();
    correct = 0.0;
    total = 0.0;
    with open("validation.data", "r") as f:
        data = f.read().splitlines();
    for row in data:
        instance = row.split();
        predict = solver.solve(instance[1]);
        if (instance[0] == predict):
            correct = correct + 1;
        total = total + 1;
    print "Question 1 accuracy: %f" % (correct / total);

def question2():
    solver = Question2_Solver();
    correct = 0.0;
    total = 0.0;
    with open("validation.data", "r") as f:
        data = f.read().splitlines();
    for row in data:
        instance = row.split();
        predict = solver.solve(instance[1]);
        if (instance[0] == predict):
            correct = correct + 1;
        total = total + 1;
    print "Question 2 accuracy: %f" % (correct / total);

def question31():
    data = [(108, 22), (90, 30), (70, 10), (143, 40),
            (150, 13), (120, 38), (90, 5), (31, 80),
            (130, 18), (98, 11), (35, 119), (24, 93),
            (48, 80), (59, 83), (100, 30), (104, 33),
            (35, 96), (28, 73), (91, 43), (87, 29),
            (38, 57), (45, 103), (20, 87), (5, 48),
            (11, 101), (40, 79), (80, 82), (128, 20),
            (32, 90), (12, 126), (77, 98), (90, 90),
            (22, 75), (23, 83), (130, 130), (140, 140),
            (120, 15), (122, 132), (133, 123), (30, 95),
            (20, 50), (22, 65), (24, 71), (19, 55),
            (118, 113), (120, 118), (113, 143), (122, 113),
            (148, 121), (140, 120), (138, 128), (123, 144),
            (132, 128), (121, 129), (138, 133), (119, 128)];
    solver = Question3_Solver();
    centroids = solver.solve(data);
    win = GraphWin("K-means", 400, 400);
    line = Line(Point(20, 320), Point(360, 320));
    line.draw(win);
    line = Line(Point(360, 320), Point(350, 310));
    line.draw(win);
    line = Line(Point(360, 320), Point(350, 330));
    line.draw(win);

    line = Line(Point(20, 320), Point(20, 20));
    line.draw(win);
    line = Line(Point(20, 20), Point(30, 30));
    line.draw(win);
    line = Line(Point(20, 20), Point(10, 30));
    line.draw(win);

    text = Text(Point(30, 340), '(0,0)');
    text.draw(win);
    text = Text(Point(360, 340), 'x1');
    text.draw(win);
    text = Text(Point(40, 20), 'x2');
    text.draw(win);
    for point in data:
        pt = Point(20 + 2*point[0], 320 - 2*point[1]);
        pt.setFill('blue');
        pt.draw(win);
    for centroid in centroids:
        cir = Circle(Point(20 + 2*centroid[0], 320 - 2*centroid[1]), 30);
        cir.setOutline('red');
        text = Text(Point(20 + 2*centroid[0], 320 - 2*centroid[1]),
                "(" + str(centroid[0]) + "," + str(centroid[1]) + ")");
        print "Question 3.1 centroid: (" + str(centroid[0]) + "," + str(centroid[1]) + ")";
        text.draw(win);
        cir.draw(win);
    print "Press any key to continue.\n";
    win.getKey();
    win.close();
    return;

def question32():
    data = [(47,20),(47,22),(53,24),(46,26),
            (50,28),(46,30),(53,32),(46,34),
            (49,36),(46,38),(48,40),(49,42),
            (54,44),(47,46),(53,48),(47,50),
            (51,52),(50,54),(48,56),(46,58),
            (50,60),(50,62),(53,64),(45,66),
            (46,68),(51,70),(45,72),(52,74),
            (46,76),(49,78),(47,80),(51,82),
            (53,84),(52,86),(52,88),(54,90),
            (54,92),(48,94),(53,96),(52,98),
            (48,100),(46,102),(54,104),(46,106),
            (52,108),(50,110),(54,112),(52,114),
            (46,116),(47,118),(50,120),(52,122),
            (45,124),(50,126),(46,128),(47,130),
            (51,132),(49,134),(45,136),(49,138),
            (45,140),(125,10),(126,12),(128,14),
            (131,16),(130,18),(131,20),(127,22),
            (129,24),(127,26),(129,28),(134,30),
            (125,32),(129,34),(134,36),(133,38),
            (126,40),(125,42),(127,44),(133,46),
            (129,48),(132,50),(133,52),(128,54),
            (134,56),(132,58),(133,60),(134,62),
            (130,64),(130,66),(128,68),(129,70),
            (134,72),(126,74),(133,76),(132,78),
            (129,80),(127,82),(126,84),(125,86),
            (129,88),(128,90),(126,92),(129,94),
            (131,96),(131,98),(132,100),(129,102),
            (134,104),(134,106),(131,108),(132,110),
            (134,112),(130,114),(127,116),(127,118),
            (133,120),(125,122),(127,124),(134,126),
            (128,128),(129,130),(5,103),(7,104),
            (9,104),(11,96),(13,100),(15,97),
            (17,102),(19,99),(21,102),(23,96),
            (25,99),(27,104),(29,103),(31,104),
            (33,98),(35,98),(37,97),(39,98),
            (41,98),(43,100),(45,99),(47,103),
            (49,101),(51,100),(53,103),(55,103),
            (57,101),(59,99),(61,99),(63,95),
            (65,101),(67,104),(69,98),(71,97),
            (73,99),(75,97),(77,104),(79,99),
            (81,101),(83,103),(85,103),(87,97),
            (89,101),(91,102),(93,96),(95,102),
            (97,98),(99,96),(101,101),(103,101),
            (105,100),(107,97),(109,104),(111,104),
            (113,99),(115,101),(117,104),(119,102),
            (121,102),(123,95),(125,104),(127,98),
            (129,102),(131,101),(133,100),(135,100),
            (137,102),(139,97),(141,99),(143,97),
            (145,102),(147,99),(149,101),(151,96),
            (153,95),(155,104),(157,103),(159,97)];
    solver = Question3_Solver();
    centroids = solver.solve(data);
    win = GraphWin("K-means", 400, 400);
    line = Line(Point(20, 320), Point(360, 320));
    line.draw(win);
    line = Line(Point(360, 320), Point(350, 310));
    line.draw(win);
    line = Line(Point(360, 320), Point(350, 330));
    line.draw(win);

    line = Line(Point(20, 320), Point(20, 20));
    line.draw(win);
    line = Line(Point(20, 20), Point(30, 30));
    line.draw(win);
    line = Line(Point(20, 20), Point(10, 30));
    line.draw(win);

    text = Text(Point(30, 340), '(0,0)');
    text.draw(win);
    text = Text(Point(360, 340), 'x1');
    text.draw(win);
    text = Text(Point(40, 20), 'x2');
    text.draw(win);
    for point in data:
        pt = Point(20 + 2*point[0], 320 - 2*point[1]);
        pt.setFill('blue');
        pt.draw(win);
    for centroid in centroids:
        cir = Circle(Point(20 + 2*centroid[0], 320 - 2*centroid[1]), 30);
        cir.setOutline('red');
        text = Text(Point(20 + 2*centroid[0], 320 - 2*centroid[1]),
                "(" + str(centroid[0]) + "," + str(centroid[1]) + ")");
        print "Question 3.2 centroid: (" + str(centroid[0]) + "," + str(centroid[1]) + ")";
        text.draw(win);
        cir.draw(win);
    print "Press any key to continue.\n";
    win.getKey();
    win.close();
    return;

def main(argv):
    for arg in argv:
        if arg == "-q1":
            question1();
    for arg in argv:
        if arg == "-q2":
            question2();
    for arg in argv:
        if arg == "-q3.1":
            question31();
    for arg in argv:
        if arg == "-q3.2":
            question32();

if __name__ == "__main__":
    main(sys.argv);

