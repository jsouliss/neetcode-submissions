class ListNode:
    def __init__(self, value = None, next = None):
        self.val = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode()
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index: 
                return curr.val
            curr = curr.next 
            i += 1
        return -1 

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head.next:
            newNode.next = self.head.next        
        self.head.next = newNode
            

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        tail = self.head.next
        if tail:
            while tail.next:
                tail = tail.next
            tail.next = newNode
        else: 
            self.head.next = newNode

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while curr.next:
            if i == index:
                curr.next = curr.next.next
                return True
            curr = curr.next
            i += 1
        return False
                   

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head.next 
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr 