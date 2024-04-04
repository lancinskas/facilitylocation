#==============================================================================
# Implementation of the binary model of customer behavior
#==============================================================================

import numpy
import DCFLP
from CustomerBehaviorModels import utilityBinary
from CustomerBehaviorModels import utilityProportional


#==============================================================================
# Driver code
#==============================================================================

DCFLP.I  = numpy.loadtxt('TestData.dat')
DCFLP.J  = [[0,1], [1,1], [2,1], [3,1], [4,1]]           
DCFLP.L  = [[5,1], [6,1], [7,1], [8,2], [21, 55]]

X =  [0, 1, 2]

utility = utilityBinary(X)
print(round(utility,4))

utility = utilityProportional(X)
print(round(utility,4))

# Result: 15.7809
    




