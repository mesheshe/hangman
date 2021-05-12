// Simple version of LinkedIntList with the appending add method

public class LinkedIntList {
    private ListNode front;


    public LinkedIntList(){
        front = null;
    }
    // post: appends the value to the end of the list
    public void add(int value) {
        if (front == null) {
            front = new ListNode(value);
        } else {
            ListNode current = front;
            while (current.next != null) {
                current = current.next;
            }
            current.next = new ListNode(value);
        }
    }

    public void addSorted(int value){
        if(front == null || front.data > value){
            front = new ListNode(value, front);
            return;    
        }
        ListNode current = front;      
        ListNode next = current.next;  
        while(next != null && next.data < value){
            current = next;
            next = current.next;
        }
        current.next = new ListNode(value, next);      
    }

    public String toString(){
        ListNode current = front;
        String str = "LL = ";
        while (current != null){
            str += current.data + " ";
            current = current.next;
        }
        return str;
    }

    public void removeLast(int value){
        if (front == null){
            System.out.println("Action on empty list is not allowed");
            return;
        }
        ListNode before = null;
        ListNode at = null;
        ListNode curr = front;
        if (front.data == value){
            at = front;
        }
        while (curr != null){
            if (curr.next != null && curr.next.data == value){
                before = curr;
                at = curr.next;
            } 
            curr = curr.next;
        }
        if (before == null && at != null){
            front = at.next;
        }else if (before == null && at == null){
            System.out.println("Number doesn't exist in list");
        }else{
            before.next = at.next;
        }
    }
    public void reorder(){
        ListNode negEnd = null;
        ListNode negFront = null;
        ListNode posFront = null;
        ListNode posCurr = null;
        ListNode curr = front;        
        while(curr != null){
            ListNode temp = curr.next;  // next node
            if (curr.data < 0){
                if (negEnd == null){
                    curr.next = negFront;    // curr.next references 
                    negEnd = curr;
                    negFront = curr;
                }else{
                    curr.next = negFront;
                    negFront = curr;
                }
            }else{
                if (posFront == null){
                    posFront = curr;
                    posCurr = posFront;
                    posCurr.next = null;
                }else{
                    posCurr.next = curr;
                    posCurr = curr;
                    posCurr.next = null;
                }
            }
            //curr.next = temp;   //curr.next is the next of curr, so doing this, I undid all the work I did. 
            curr = temp;               // curr is set to next node directly.
        }
        if (negFront != null && posFront != null){
            negEnd.next = posFront;
            front = negFront;
        }else if(negFront != null && posFront == null){
            front = negFront;
        }else{
            front = posFront;
        } 

    }

}


/*
2,4,6,8
4,6,8,2
4,8,2,6
*/

/*
10|, 20, 30|, 40, 50|, 60
20 , 30, 40|, 50, 60|, 10
20 , 30  50 , 60, 10|, 40
20 , 30  50 , 60, 40 , 10
*/

/*

*/