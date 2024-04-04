import numpy
import math

#==============================================================================
# Global variables
#==============================================================================

I  = []
J  = []
qJ = []
L =  []
qL = []

#==============================================================================
# Haversine distance between two points given by indices in the set I
#==============================================================================

def distance(p1, p2):    
    global I
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






