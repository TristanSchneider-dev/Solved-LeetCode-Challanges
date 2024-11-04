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
    public ListNode MergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode, int> heap = new PriorityQueue<ListNode, int>();

        foreach(ListNode startNode in lists){
            if (startNode != null) heap.Enqueue(startNode, startNode.val);
            Console.WriteLine(startNode.val);
        }

        ListNode head = new ListNode(0);
        ListNode tail = head;

        /*
        while(heap.Count > 0){
            tail = heap.Dequeue();
        }
        */
        return null;
    }
}
