/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        
        //Count ListNodes
        ListNode current = head;
        int counter = 0;
        while(current != null){
            current = current.next;
            counter += 1;
        }

        //if (n == counter): 

        ListNode beforeDelete = null;
        current = head; //back to start
        counter -= n;
        while(counter > 0){
            if (counter == 1) beforeDelete = current;
            current = current.next;
            counter -= 1;
        }
        
        Console.WriteLine(beforeDelete.val);
        Console.WriteLine(current.val);

        return head;
    }
}
