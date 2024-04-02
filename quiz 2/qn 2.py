from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[list]) -> Optional[list]:
        if head is None:
            return None
        
        tortoise = head
        hare = head
        
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            
            if tortoise == hare:
                break
        
        if hare is None:
            return None
        
        # Find the start of the cycle
        pointer1 = head
        pointer2 = hare
        
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        # Find the length of the cycle
        length = 0
        while pointer2.next != pointer1:
            pointer2 = pointer2.next
            length += 1
        
        # Reverse the cycle
        prev = None
        current = pointer1
        
        for _ in range(length):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return pointer1

