#include <iostream>
using namespace std;
class Point{
    private:
        double x;
        double y;
    public:
        Point(){}
        Point(double x,double y):x(x),y(y){}
};
class Line{
    private:
        Point p1;
        Point p2;
    public:
        Line(Point p1, Point p2):p1(p2),p2(p2){}
};


int main(){
    Point p1(2,4);
    Point p2(2,5);
    Line l1(p1,p2);
    cout <<"all good";//\n";
    return 0;
}