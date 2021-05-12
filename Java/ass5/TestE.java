// Short program to test whether the expressions generated using the file
// sentence2.txt are legal.  They can often be very long.  You should include
// the expression as indicated below and you should be able to compile the
// program.  It might throw an exception when run, but it should compile.

import static java.lang.Math.*;

public class TestE {
    public static void main(String[] args) {
        double x = 3;
        double y = 4;
        double z = 0 - 1; // placeholder
        
        System.out.println(z);
        /*
        0 - pow ( 92 , pow ( 1 % 92 % 42 / ( 92 ) % y , y / 1 ) )
        ( 42 + sin ( tan ( ( sqrt ( 42 ) ) + abs ( y ) % x / 1 - 0 ) ) * 1 - 1 - 1 % tan ( max ( 0 , 92 ) ) )
        ( 0 - y % 0 % sin ( cos ( x / 92 + 42 - min ( 1 , 1 ) + 0 ) ) + 0 / min ( 92 , - 92 ) / 1 )
        tan ( ( 92 % 42 ) ) % - ( 42 ) + 42
        0
        tan ( 1 ) + - pow ( pow ( x , 92 - x ) - 1 * - 42 * y , x * - - 42 * - sqrt ( 92 ) - - y - - 42 / cos ( pow ( ( 1 ) , sqrt ( abs ( 1 ) ) ) ) % x ) * ( x )
        min ( x + 1 , y )
        1
        y
        1 / 0
        y + 42
        1 + cos ( y + ( ( cos ( 42 / x ) ) ) + 92 ) + x - 42 % y / min ( y % min ( y , 92 ) * abs ( 1 - sqrt ( - sqrt ( 42 ) ) - pow ( x , pow ( 92 , y ) ) ) , sin ( ( 0 ) % y / - x ) ) * y / 92
        ( - max ( max ( 92 - - x , 92 ) , ( y % ( y ) - 1 ) % 0 / 0 + 42 + sin ( pow ( 92 , - sqrt ( 92 ) * 42 ) - - x ) ) ) * 92
        */
    }
}
