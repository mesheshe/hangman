// Simple client program that adds some values to the end of a LinkedIntList.

public class LinkedIntListClient {
    public static void main(String[] args) {
        LinkedIntList list = new LinkedIntList();
        list.add(0);
        list.add(-3);
        list.add(3);
        list.add(-5);
        list.add(7);
        list.add(-9);
        list.add(-10);
        list.add(10);
        list.add(-11);
        list.add(-11);
        list.add(-11);
        list.add(12);
        list.add(-15);
        
        list.reorder();
        System.out.println(list);
    }
}
