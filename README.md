# Facility Location

## GeoData

Geographical data of cities and towns in Lithuania and Spain, which can be used as demand points in a facility location model. First two columns of a file stands for the geographical coordinates of the point and the last column -- for the population (number of citizens).

## Class DCFLP

The class DCFLP (Discrete Competitive Facility Location Problem) is stored in the file `DCFLP.cpp` with the header file `DCFLP.h` and is designed to store and manage problem data.

#### Member variables

- `problemName` - problem name (`string`);
- `I` - vector of demand points (`vector < vector<double> > `); each element is a vector which stores two coordinates and the population;
- `DM` - distance matrix, which describes distances between all demand points (`vector < vector<double> >`);
    vector < vector <int> >    J;   // Preexisting facilities
    vector < vector <int> >    qJ;  // Qualities of preexisting facilities
    vector <int>               L;   // Location candidates
    vector <int>               qL;  // Qualities of location candidates

#### Member functions
