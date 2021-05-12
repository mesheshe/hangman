 
import java.util.*;

public class ListSetExample {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("four");
        list.add("score");
        list.add("seven");
        list.add("years");
        list.add("what was next?");
        list.add("ago");
        list.add(2, "and");
        list.remove(5);
        System.out.println("list = " + list);
        System.out.println(list.indexOf("seven"));
                
        for (int i = 0; i < list.size(); i++) {
            String next = list.get(i);
            System.out.println(next);
        }
        System.out.println();
                
        for (String s : list) {
            System.out.println(s);
        }
        System.out.println();
                
        Iterator<String> itr = list.iterator();
        while (itr.hasNext()) {
            String next = itr.next();
            System.out.println(next);
        }
        System.out.println();

        int[] data = {18, 4, 97, 3, 4, 18, 72, 4, 42, 42, -3};
        List<Integer> numbers1 = new ArrayList<>();
        Set<Integer> numbers2 = new TreeSet<>();
                
        for (int n : data) {
            numbers1.add(n);
            numbers2.add(n);
        }
        System.out.println("numbers1 = " + numbers1);
        System.out.println("numbers2 = " + numbers2);
                
        numbers2.remove(42);
        System.out.println("numbers2 = " + numbers2);
                
        Iterator<Integer> itr2 = numbers2.iterator();
        while (itr2.hasNext()) {
            int n = itr2.next();
            if (n % 3 == 0) {
                itr2.remove();
                // NOT numbers2.remove(n);
            }
        }
        System.out.println("numbers2 = " + numbers2);
    }
}
// This class includes sample client code for manipulating lists and sets.
//
// translation from array to ArrayList:
//    String[]          => ArrayList<String>
//    new String[10]    => new ArrayList<String>()
//    a.length          => list.size()
//    a[i]              => list.get(i)
//    a[i] = value;     => list.set(i, value);
// new list operations:
//     list.remove(i);     --remove the ith value
//     list.add(value);    --appends a value
//     list.add(i, value); --adds at an index
//     list.clear()        --remove all values
// set operations:
//     s.add(value);    --adds a value to the set (might already be there)
//     s.remove(value); --remove the given value from the set
//     s.contains()     --whether set contains the value
//     s.size()         --number of values in the set