#==============================================================================
# Implementation of the binary model of customer behavior
#==============================================================================

import numpy
import math

#==============================================================================
# Haversine distance between two points given by indices in the set I
#==============================================================================

def distance(p1, p2):
    
    # Get coordinates by indices in the set I
    lat1 = I[p1,0]; lon1 = I[p1,1]
    lat2 = I[p2,0]; lon2 = I[p2,1]
    
    # distance between latitudes and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0
 
    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
 
    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c

#==============================================================================
# Attractiveness that customer i feels to the facility j in I
#==============================================================================

def attractiveness(i, j, q_j):
    return q_j / (distance(i, j) + 1)

#==============================================================================
# Utility of the new locations given by X
#==============================================================================

def utilityBinary(I, J, X, theta):
    
    AttrJ = []          # attractiveness of all preexisting facilities
    AttrX = []          # attractiveness of all new facilities
    utility = 0         # utility of the new facilties
    totalDemand = 0     # total demand of the whole population
    
    for i in range(0,len(I)):
        totalDemand = totalDemand + I[i,2]
        
        # Calculate AttrP
        AttrJ.clear()
        for j in range(0,len(J)):
            #AttrJ.append(distance(i,J[j]))
            AttrJ.append(attractiveness(i, J[j], 1))
            
        # Calculate AttrX
        AttrX.clear()
        for j in range(0,len(X)):
            #AttrX.append(distance(i,X[j]))
            AttrX.append(attractiveness(i, X[j], 1))
        
        # If the best of AttrX is better than the best of AttrJ
        if (max(AttrX) > max(AttrJ)):
            utility = utility + I[i,2]
        
        # If the best of Attr is equal to the best of AttrJ
        elif (max(AttrX) == max(AttrJ)):
            utility = utility + I[i,2] * theta
    
    return utility/totalDemand*100

#==============================================================================
# Driver code
#==============================================================================

I = numpy.loadtxt('TestData.dat')
J = [0, 1, 2, 3, 4]
X = [5, 6, 7]
utility = utilityBinary(I, J, X, 1/3)
print(round(utility,4))

# Result: 15.7809
    




