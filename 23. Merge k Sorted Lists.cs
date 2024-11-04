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
            if (startNode == null) continue;
            heap.Enqueue(startNode, startNode.val);
        }

        ListNode head = new ListNode(0);
        ListNode tail = head;

        while(heap.Count > 0){
            ListNode node = heap.Dequeue();
            tail.next = node;
            tail = tail.next;

            if (node.next != null) heap.Enqueue(node.next, node.next.val);
        }


        return head.next;
    }
}
