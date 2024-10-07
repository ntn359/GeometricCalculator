#include<iostream>
#include <math.h>
#include<vector>
using namespace std;

# define PI           3.14159265358979323846  /* pi */


class Point;
class Shape
{

virtual float findArea()=0;
virtual float findDistance(Point p)=0;

};



class Point: public Shape
{
    public:
float x, y;

Point(float a=0, float b=0)
{
x=a;y=b;
cout<<"Point created\n";
}
Point(Point& other)
{
x=other.x;
y=other.y;
cout<<"Point created\n";
}
Point& operator=(Point& other)
{
x=other.x;
y=other.y;
cout<<"Point created\n";
return *this;
}
Point(Point && other)
{
   x=other.x;
y=other.y;
other.x=0;
other.y=0; 
}
float findArea()
{
cout<<"Cant find area of point";
return 0;
}
float findDistance(Point p)
{
return std::sqrt(std::pow((p.x - x), 2) + std::pow((p.y - y), 2));
}

};

class Line : public Shape
{
Point p1,p2;
public:
Line()
{
cout<<"Line created\n";
}
Line(Point a, Point b):p1(move(a)), p2(move(b)){cout<<"Line created\n";}
float findArea()
{
cout<<"Cant find area of line";
return 0;
}
float findDistance(Point p)
{
    float x=(p1.x+p2.x)/2;
    float y=(p1.y+p2.y)/2;
return std::sqrt(std::pow((p.x - x), 2) + std::pow((p.y - y), 2));
}

};


class Circle : public Shape
{
Point center;
float radius;
public:
Circle(Point p, float r):center(std::move(p)), radius(r)
{
cout<<"Circle created\n";
}
float findArea()
{
return PI*radius*radius;
}
float findCircumference()
{
return 2*PI*radius;
};
float findDistance(Point p)
{
return std::sqrt(std::pow((p.x - center.x), 2) + std::pow((p.y - center.y), 2));
}


};

class Rectangle:public Shape
{
Point topLeft, botRight;
public:
Rectangle(Point p1, Point p2):topLeft(p1), botRight(p2)
{
}
Rectangle(Rectangle& other )
{
topLeft =other.topLeft;
botRight=other.botRight;
}
float findArea()
{
return (topLeft.x-botRight.x) * (topLeft.y - botRight.y);
}
float findDistance(Point p)
{
    float x= (topLeft.x+botRight.x) /2;
    float y= (topLeft.y+botRight.y) /2;
return std::sqrt(std::pow((p.x - x), 2) + std::pow((p.y - y), 2));
}
};

class ShapeFactory
{
public:
Point* createPoint(float x, float y)
{
    return new Point(x,y);
}
Line* createLine(float x1, float y1, float x2, float y2)
{
    return new Line(Point(x1,y1), Point(x2,y2));
}
Circle* createCircle(float x, float y, float rad)
{
    return new Circle(Point(x,y), rad);
}
Rectangle* createRectangle(float x1, float y1, float x2, float y2)
{
    return new Rectangle(Point(x1,y1), Point(x2,y2));
}

Shape* create()
{
    int i;
    cout<<"1. Create Point\n"
"2. Create Line\n"
"3. Create Circle\n"
"4. Create Rectangle\n"
"5. Exit"<<endl;
cin>>i;
switch(i)
{
case 1:
{
float x,y;
cout<<"Enter x and y\n";
cin>>x>>y;
return createPoint(x,y);
}
break;

case 2:
{
float x1,y1,x2,y2;
cout<<"Enter x1, y1 and x2, y2";
cin>>x1>>y1>>x2>>y2;
return createLine(x1,y1,x2,y2);
}
break;

case 3:
{
float x,y;
cout<<"Enter x and y";
cin>>x>>y;
return createPoint(x,y);
}
break;


case 4:
{
float x,y;
cout<<"Enter x and y";
cin>>x>>y;
return createPoint(x,y);
}
break;
default:cout<<"Invalid shape"<<endl;
}

};


int main()
{
ShapeFactory *fact=new ShapeFactory();
vector<Shape*> shapes;
int in;
for(int i=0;i<2;i++)
{

cout<<"1. Create\n"
"2. "




}


}

return 1;
}