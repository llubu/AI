import math 

class Question3_Solver:
    def __init__(self):
        return;

    # Add your code here.
    # Return the centroids of clusters.
    # You must use [(30, 30), (150, 30), (90, 130)] as initial centroids
    def solve(self, points):
        centroids = [(30, 60), (150, 30), (90, 130)];
        centroid1 = [(), (), ()]
        
        while(1):
            final = [[],[],[]]
            minIndex = -1
            
            for point in points:
                d1 = self.getDistance(centroids[0], point)
                d2 = self.getDistance(centroids[1], point)
                d3 = self.getDistance(centroids[2], point)
                
                if d1 < d2:
                    minIndex = 0
                    if d3 < d1:
                        minIndex = 2
                elif d3 < d2:
                    minIndex = 2
                else:
                    minIndex = 1
                
                final[minIndex].append(point)
            #print len(final[0]), len(final[1]), len(final[2]) 
                
            for i in range(0,3):
                xsum = 0
                ysum = 0
                for item in final[i]:
                    xsum += item[0]
                    ysum += item[1]
                        
                centroid1[i] =(xsum/len(final[i]), ysum/len(final[i]))
            print centroid1, 'CEN'
            cd1 = self.getDistance(centroids[0], centroid1[0])
            cd2 = self.getDistance(centroids[1], centroid1[1])
            cd3 = self.getDistance(centroids[2], centroid1[2])
                
            if ( cd1 < 0.0001 and cd2 < 0.0001 and cd3 < 0.0001):
                break
            else:
                centroids = centroid1
                
        return centroids;
    
    def getDistance(self, p1, p2):
        """
        Helper function to get the distance between two points p1 and p2
        """
        #print 'points' , p1, p2
        dis = math.pow( math.pow (( p2[0] - p1[0]), 2) + math.pow (( p2[1] - p1[1]), 2),  0.5)
        
        return dis
