// Simple program that creates a linked list and writes it out.

public class ListExample {
    public static void main(String[] args) {
        ListNode list = new ListNode();
        list.data = 3;
        list.next = new ListNode();
        list.next.data = 7;
        list.next.next = new ListNode();
        list.next.next.data = 12;
        list.next.next.next = null;
        System.out.println(list.data + " " + list.next.data + " "
                           + list.next.next.data);

        // note that with the version of ListNode that includes multiple
        // constructors, the constructing can be written in one line:
        // ListNode list = new ListNode(3, new ListNode(7, new ListNode(12)));
    }
}