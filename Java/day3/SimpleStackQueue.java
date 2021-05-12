
// short program to demonstrate basic use of a stack and queue

import java.util.*;

public class SimpleStackQueue {
    public static void main(String[] args) {
        String[] data = {"four", "score", "and", "seven", "years", "ago"};
        Queue<String> q = new LinkedList<>();
        Stack<String> s = new Stack<>();
        
        for (String str : data) {
            q.add(str);
            s.push(str);
        }
        
        System.out.println("initial queue = " + q);
        while (!q.isEmpty()) {
            String str = q.remove();
            System.out.println("removing " + str + ", now queue = " + q);
        }
        System.out.println();

        System.out.println("initial stack = " + s);
        while (!s.isEmpty()) {
            String str = s.pop();
            System.out.println("removing " + str + ", now stack = " + s);
        }
    }
}