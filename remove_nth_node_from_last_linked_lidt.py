"""
given the head pointer, remove the nth node from the last from a linked list

Solution Approach
-----------------
Use two pointers, fast and slow
Advance fast pointer to the nth postion
if fast is none return head.next value
else move slow and fast pointer till fast is at the last (fast.next is null)
now these pointers are n position apart and slow 
is one pointer shy from the item to be delete, so delete slow.next

"""
class SingleLinkedList:
    def __init__(self, next, value: int):
        self.next = next
        self.value = value

def remove_nth_node_from_last(head: SingleLinkedList, n: int) -> SingleLinkedList:
    """
    Remove Nth node from the last of the linkedlist

    Parameters
    ----------
    head: head pointer of the linkedlist
    
    Returns
    -------
    head: head pointer to the linkedlist, after deletion
    """
    fast_pointer = slow_pointer = head
    for i in range(n): # move the fast pointer to nth postion
        fast_pointer = fast_pointer.next
    
    if not fast_pointer: # if fast is empty simply return the head.next value
        return head.next
    while fast_pointer:
        # now move both fast pointer and slow pointer
        fast_pointer = fast_pointer.next
        slow_pointer = slow_pointer.next
    # now the slow pointer and fast pointers are n postions apart
    # the slow pointer is one position away from the item to be deleted
    
    slow_pointer.next = slow_pointer.next.next # detete the slow pointers next 

    return head.next