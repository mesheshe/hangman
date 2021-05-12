 import java.util.*;

public class ArrayIntListClient {
    public static void main(String[] args) {
        ArrayIntList list = new ArrayIntList(25);
        list.add(3);
        list.add(7);
        list.add(11);
        list.add(list.size(), 17);
        System.out.println("initial list = " + list);
        list.add(0, 2);
        list.add(2, 5);
        System.out.println("after some adds, list = " + list);
        System.out.println();

        for (int i = 1; i < 10; i += 2) {
            if (list.contains(i)) {
                System.out.println("index of " + i + " = " + list.indexOf(i));
            } else {
                System.out.println("list does not contain " + i);
            }
        }
        System.out.println();

        for (int i = 0; i < list.size(); i++) {
            System.out.println("get(" + i + ") returns " + list.get(i));
        }
        System.out.println();

        ArrayIntList list2 = new ArrayIntList();
        list2.add(42);
        System.out.println("after adding 42 to empty list, list2 = " + list2);
        list2.addAll(list);
        System.out.println("after addAll of list, list2 = " + list2);
        System.out.println("and list still = " + list);
        System.out.println();

        Random r = new Random();
        while (list.size() > 0) {
            int i = r.nextInt(list.size());
            list.remove(i);
            System.out.println("after removing at " + i + " list = " + list);
        }

        System.out.println();
        ArrayList<String> str = new ArrayList<String>();
        str.add("hi");
        str.add("how are");
        str.add("you?");
        System.out.println(str);
        stretch(str, 5);
        System.out.println(str);
        System.out.println();
        Stack<Integer> s = new Stack<>();
        s.push(2);
        s.push(2);
        s.push(2);
        s.push(2);
        s.push(2);
        s.push(-5);
        s.push(-5);
        s.push(3);
        s.push(3);
        s.push(3);
        s.push(3);
        s.push(4);
        s.push(4);
        s.push(1);
        s.push(0);
        s.push(17);
        s.push(17);
        System.out.println(s);
        compressDuplicates(s);
        System.out.println(s);
    }
    public static void stretch(ArrayList<String> list, int k){
        if (list.isEmpty() || k < 2){return;}
        for (int i = 0; i < list.size(); i+=k){
            int j = k - 1;
            while (j != 0){
                list.add(i, list.get(i));
                j--;
            }
        }        
    } 

    public static void s2q(Stack<Integer> s, Queue<Integer> q){
        while (!s.isEmpty()){
            q.add(s.pop());
        }
    }
    public static void q2s(Queue<Integer> q, Stack<Integer> s){
        while (!q.isEmpty()){
            s.push(q.remove());
        }
    }
    public static void compressDuplicates(Stack<Integer> s){
        Queue<Integer> q = new LinkedList<>();
        while(!s.isEmpty()){
            int count = 1;
            int value = s.pop();
            while (!s.isEmpty() && s.peek() == value){
                count++;
                s.pop();
            }
            q.add(value);
            q.add(count);
        }
        s2q(s,q);
        q2s(q,s);
        s2q(s,q);
        q2s(q,s);
    }

}
