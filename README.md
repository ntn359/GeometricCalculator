# GeometricCalculator

- Shapes implemented
  - Point
  - Line
  - Circle
  - Rectangle
  - Cuboid

- Mainly focused on quality of the code
- Unit tests are done for each and every function
- Static code analysis is done
- No dead code or unused variables in the code
- Docstring added for better understanding of func
- Uniform naming conventions are used

##To run

You need to import contents of main.py file

`from main import *`

Above line will import all.
Sample execution

```
from main import *
p1 = Point(1,2)
p2 = Point(2,3)
distance_between_points(p1, p2)
p1.distance(3,4)

```

##Assumptions

- All points are in cartesian coordinate system
- Distance between 2 similar shapes are done from center points of respective shape
- All values are either int or float

##Known issues
- Area of Intersection of 2 rectangles is not working. Unable to get the logic right

##Challenges and/or learnings
- Initially started off with writing code in C++. But, the concept of Read-Eval-Print-Loop is bit difficult in C++. Had to spend much effort on that rather than spending on actual logic. So, pivoted to Python.
- Thought process behind choosing C++ was to showcase and utilize many concepts of C++ such as overriding functions and constructors and use move semantics. 
- Had opportunity to learn unit tests in python.



-