class ListNode:
    def __init__(self, val, next_node=None):  # Use 'next_node' consistently
        self.val = val
        self.next_node = next_node  # Use 'next_node' for the next reference

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(0)  # Sentinel node
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next_node  # Skip the sentinel node and use 'next_node'
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next_node  # Use 'next_node'
            i += 1
        return -1
    
    def insertHead(self, val: int) -> None:
        new_element = ListNode(val)
        new_element.next_node = self.head.next_node  # Use 'next_node'
        self.head.next_node = new_element  # Update head
        if self.tail == self.head:  # If the list was empty
            self.tail = new_element

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next_node = new_node  # Use 'next_node'
        self.tail = new_node  # Update the tail
    
    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while i < index and curr.next_node:  # Use 'next_node'
            curr = curr.next_node
            i += 1
        
        if curr.next_node:
            if curr.next_node == self.tail:  # Update the tail if needed
                self.tail = curr
            curr.next_node = curr.next_node.next_node  # Use 'next_node'
            return True
        return False
    
    def getValues(self) -> list:
        curr = self.head.next_node  # Use 'next_node'
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next_node  # Use 'next_node'
        return values
