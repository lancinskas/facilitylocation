# Facility Location

## GeoData

Geographical data of cities and towns in Lithuania and Spain, which can be used as demand points in a facility location model. First two columns of a file stands for the geographical coordinates of the point and the last column -- for the population (number of citizens).

## Class DCFLP

The class DCFLP (Discrete Competitive Facility Location Problem) is stored in the file `DCFLP.cpp` with the header file `DCFLP.h` and is designed to store and manage problem data.

#### Member variables

- `problemName` - problem name (`string`).
- `I` - list of demand points implemented as a vector of vectors (`vector < vector<double> >`). Each element (vector) stores three `double` values: two coordinates and the population.
- `DM` - distance matrix, which stores distances between all demand points (`vector < vector<double> >`);
- `J` - indices of locations of preexisting facilities implemented as a vector of vectors (`vector < vector <int> >`). Each row (vector) stores indices of facility locations which belongs to a single chain and the number of rows coincides with the number of chains.
- `qJ` - qualities of the corresponding preexisting facilities implemented as a vector of vectors (`vector < vector <int> >`). The size of `qJ` coincides with the size of `J`.
- `L` - indices of the location candidates.
- `qL` - qualities of the corresponding location candidates.

#### Member functions

To be completed
