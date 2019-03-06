# astar
Simple a* (a star) Algorithm in cpp for pathfinding with visualization in gnuplot

You have to install Gnuplot for visualization of the path, but it is not necessary. Gnuplot should be working in CMD.
Without Gnuplot, you have to rewrite the last part of the main function of astar.cpp .
The gnuplot.h header must be in the same folder as astar.cpp .
Type simply " g++ astar.cpp -o astar " for Compiling.
b.py is for generating of more rows.
A black cell means that this cell is blocked.
A gray cell is unblocked but is not chosen of the a* algorithm as a part of the path.
A white cell is part of the path.
