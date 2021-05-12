// client code to test the RemoveAll method, comparing results against the
// results for an ArrayList<Integer>.

import java.util.*;

public class TestRemoveAll {
    public static void main(String[] args) {
        int[] data1 = {1, 2, 3, 4, 5, 2, 2, 3, 4, 4, 4, 4, 5, 6};
        int[] data2 = {2, 4, 6, 8};
        ArrayIntList list1 = new ArrayIntList();
        ArrayIntList list2 = new ArrayIntList();
        List<Integer> list3 = new ArrayList<>();
        List<Integer> list4 = new ArrayList<>();
        for (int n1 : data1) {
            list1.add(n1);
            list3.add(n1);
        }
        for (int n2 : data2) {
            list2.add(n2);
            list4.add(n2);
        }
        System.out.println("original values:");
        System.out.println("    list1 = " + list1);
        System.out.println("    list2 = " + list2);
        list1.removeAll(list2);
        list3.removeAll(list4);
        System.out.println("after the call list1.removeAll(list2):");
        System.out.println("    list1 = " + list1);
        System.out.println("    list2 = " + list2);
        if (list1.toString().equals(list3.toString())) {
            System.out.println("passed");
        } else {
            System.out.println("list1 should be = " + list3);
        }
    }
}
