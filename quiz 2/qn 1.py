from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[list]) -> bool:
        if head is None:
            return False
        
        tortoise = head
        hare = head
        
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            
            if tortoise == hare:
                return True
        
        return False

