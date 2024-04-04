#==============================================================================
# Implementation of the binary model of customer behavior
#==============================================================================

import DCFLP

def utilityBinary(X):
    AttrJ = []          # attractiveness of all preexisting facilities
    AttrX = []          # attractiveness of all new facilities
    utility = 0         # utility of the new facilties
    totalDemand = 0     # total demand of the whole population
    
    for i in range(0,len(DCFLP.I)):
        totalDemand = totalDemand + DCFLP.I[i,2]
        
        # Calculate AttrP
        AttrJ.clear()
        for j in range(0,len(DCFLP.J)):
            AttrJ.append(DCFLP.attractiveness(i, DCFLP.J[j][0], DCFLP.J[j][1]))
            
        # Calculate AttrX
        AttrX.clear()
        for j in range(0,len(X)):
            AttrX.append(DCFLP.attractiveness(i, DCFLP.L[X[j]][0], DCFLP.L[X[j]][1]))
        
        # If the best of AttrX is better than the best of AttrJ
        if (max(AttrX) > max(AttrJ)):
            utility = utility + DCFLP.I[i,2]
        
        # If the best of Attr is equal to the best of AttrJ
        elif (max(AttrX) == max(AttrJ)):
            utility = utility + DCFLP.I[i,2] * 0.5
    
    return utility/totalDemand*100

#==============================================================================
# Test Case
#==============================================================================

# TestData.dat
# J =  [0, 1, 2, 3, 4]
# qJ = [1, 1, 1, 1, 1]
# X =  [5, 6, 7]
# qX = [1, 1, 1]
# Result: 15.7809

#==============================================================================
# Implementation of the proportional (Huff) model of customer behavior
#==============================================================================

def utilityProportional(X):    
    utility = 0
    totalDemand = 0
    
    for i in range(0,len(DCFLP.I)):
        
        totalDemand = totalDemand + DCFLP.I[i][2]
        
        # Sum attractiveness to all preexisting facilities
        sumAttrJ = 0;
        for j in range(0,len(DCFLP.J)):
            sumAttrJ = sumAttrJ + DCFLP.attractiveness(i, DCFLP.J[j][0], DCFLP.J[j][1])
        
        # Sum attractiveness to all new facilities
        sumAttrX = 0;        
        for j in range(0,len(X)):
            sumAttrX = sumAttrX + DCFLP.attractiveness(i, DCFLP.L[X[j]][0], DCFLP.L[X[j]][1])
        
        # Proportion of buying power ot the i-th demand point
        utility = utility + DCFLP.I[i][2] * sumAttrX / (sumAttrJ + sumAttrX) 
    
    return utility/totalDemand*100
    




