class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        # If llist is not empty
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

    def insertTail(self, val: int) -> None:
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = ListNode(val)
        else:
            self.head = ListNode(val)

    def remove(self, index: int) -> bool:
        if self.head:
            if index == 0:
                self.head = self.head.next
                return True
            curr = self.head
            i = 0
            while curr:
                if i == index - 1 and curr.next:
                    curr.next = curr.next.next
                    return True
                curr = curr.next
                i += 1
        return False

    def getValues(self) -> List[int]:
        items = []
        curr = self.head
        while curr:
            items.append(curr.val)
            curr = curr.next
        return items
