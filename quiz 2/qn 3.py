from typing import Optional

class Solution:
    def reverseList(self, head: Optional[list]) -> Optional[list]:
        if head is None:
            return None
        
        stack = []
        current = head
        
        while current is not None:
            stack.append(current)
            current = current.next
        
        new_head = stack.pop()
        current = new_head
        
        while stack:
            next_node = current.next
            current.next = stack.pop()
            current = next_node
        
        return new_head