// This class contains the example from lecture.
// Drag the "dummy" variable out to view p and q.

public class ListTest {
    public static void main(String[] args) {
        ListNode dummy = new ListNode(1);               //dummy = data = 1   next = null 
        ListNode p = new ListNode(2, new ListNode(4));  //p     = data = 2   next = (data = 4   next = null)
        ListNode q = new ListNode(3, new ListNode(9));  //q     = data = 3   next = (data = 9   next = null)
        p.next.next = q;                                //p     = data = 2   next = (data = 4   next = (data = 3   next = (data = 9   next = null)))
        q = q.next;                                     //q     = data = 9   next = null
        p.next.next.next = null;                        //p     = data = 2   next = (data = 4   next = (data = 3   next = null))
        ListNode node = dummy;
        while(node != null){
            System.out.print(node.data + " ");
            node = node.next;
        }
    }
}