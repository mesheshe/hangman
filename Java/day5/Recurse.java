// This file contains several simple examples of recursive definitions.

import java.io.*;
import java.util.*;

public class Recurse {
    public static void main(String[] args) {
        writeStars(8);
        writeStars2(6);
        Scanner input = new Scanner("this\nis\nfun\nno?\n");
        reverse(input);
        System.out.println(stutter(-348));
        System.out.print("Binary representation of -39 = ");
        writeBinary(-39);
        System.out.println();
        int[] data = {3, 9, 15, 7};
        for (int i = 0; i <= data.length; i++) {
            int[] test = Arrays.copyOf(data, i);
            System.out.println("sum of " + Arrays.toString(test) + " = "
                               + sum(test));
        }
    }

    // iterative method that produces an output line of exactly n stars
    public static void writeStars(int n) {
        for (int i = 0; i < n; i++) {
            System.out.print("*");
        }
        System.out.println();
    }

    // recursive method that produces an output line of exactly n stars
    public static void writeStars2(int n) {
        if (n <= 0) {
            System.out.println();
        } else {
            System.out.print("*");
            writeStars2(n - 1);
        }
    }
  
    // post: reads a file, writing the lines to System.out in reverse order
    public static void reverse(Scanner input) {
        if (input.hasNextLine()) {
            String line = input.nextLine();
            reverse(input);
            System.out.println(line);
        }
    }

    // returns the integer obtained by replacing every digit of n with two of
    // that digit.  For example, stutter(348) returns 334488.
    public static int stutter(int n) {
        if (n < 0) {
            return -stutter(-n);
        } else if (n < 10) {
            return n * 11;
        } else {
            return 100 * stutter(n / 10) + stutter(n % 10);
        }
    }

    // writes the binary representation of n to System.out
    public static void writeBinary(int n) {
        if (n < 0) {
            System.out.print("-");
            writeBinary(-n);
        } else if (n < 2) {
            System.out.print(n);
        } else {
            writeBinary(n/2);
            System.out.print(n % 2);
        }
    }

     // returns the sum of the numbers in the given array
     public static int sum(int[] list) {
        return sum(list, 0);
    }

    // computes the sum of the list starting at the given index
    private static int sum(int[] list, int index) {
        if (index == list.length) {
            return 0;
        } else {
            return list[index] + sum(list, index + 1);
        }
    }
}