import math 

class Question3_Solver:
    def __init__(self):
        return;

    # Add your code here.
    # Return the centroids of clusters.
    # You must use [(30, 30), (150, 30), (90, 130)] as initial centroids
    #[(30, 60), (150, 60), (90, 130)]
    def solve(self, points):
        centroids = [(30, 30), (150, 30), (90, 130)]
        #centroids = [(30, 60), (150, 60), (90, 130)]
        
        while(1):
            final = [[],[],[]]
            centroid1 = [(), (), ()]
            minIndex = -1
            
            #Get distance from each current centroid
            for point in points:
                d1 = self.getDistance(centroids[0], point)
                d2 = self.getDistance(centroids[1], point)
                d3 = self.getDistance(centroids[2], point)
                
                #Find closest centroid
                if d1 < d2:
                    minIndex = 0
                    if d3 < d1:
                        minIndex = 2
                elif d3 < d2:
                    minIndex = 2
                else:
                    minIndex = 1

                final[minIndex].append(point)
            
            #Compute new centroid
            for i in range(0,3):
                xsum = 0
                ysum = 0
                for item in final[i]:
                    xsum += item[0]
                    ysum += item[1]
                    
                centroid1[i] = (xsum/len(final[i]), ysum/len(final[i]))
            
            #If centroids don't change, terminate
            if ( centroid1[0] == centroids[0] and centroid1[1] == centroids[1] and centroid1[2] == centroids[2]):
                break
            else:
                centroids = centroid1
                centroid1 = [(), (), ()]

        return centroids;
    
    def getDistance(self, p1, p2):
        """
        Helper function to get the distance between two points p1 and p2
        """
        dis = math.pow( math.pow (( p2[0] - p1[0]), 2) + math.pow (( p2[1] - p1[1]), 2),  0.5)
        return dis
