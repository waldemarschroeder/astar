# a star
Simple a* (a star) Algorithm in cpp for pathfinding with visualization in Gnuplot. <br>
I took the a star implementation in cpp from https://github.com/thuva4/Algorithms .
I did the visualization with gnuplot. <br>

## Usage
For the visualization of the path you need Gnuplot, but it is not necessary. <br>
Without Gnuplot, you have to rewrite the last part of the main function of astar.cpp . <br>
The gnuplot.h header must be in the same folder as astar.cpp . <br>
Type simply " g++ astar.cpp -o astar " for Compiling. <br>
b.py is for generating of more rows. <br>
A black cell means that this cell is blocked. <br>
A gray cell is unblocked but is not chosen of the a* algorithm as a part of the path. <br>
A white cell is part of the path. <br>
