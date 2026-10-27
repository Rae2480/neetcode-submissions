class Node:

    def __init__(self, value: int):
        self.value = value
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    
    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1
        else:
            curr = self.head

            for i in range(index):
                curr = curr.next
            
            return curr.value

        

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        
        if self.length == 0: # if ll initially empty
            self.tail = node # both head and tail are node
        self.length += 1
        

    def insertTail(self, val: int) -> None:
        node = Node(val)

        if self.length == 0: # if ll initially empty
            self.head = node # head is also the new node added to tail
        else:
            self.tail.next = node # curr tail node's next is new node

        self.tail = node # ll tail is new node
        self.length += 1

        

    def remove(self, index: int) -> bool:
        
        if index >= self.length or index < 0:
            return False
        else:
            if index == 0: # head node removed
                self.head = self.head.next
                if self.length == 1: # if there was only 1 node which we just removed
                    self.tail = None
            else:
                prev = self.head

                for i in range(index-1): # traverse down the list
                    prev = prev.next

                removed = prev.next
                prev.next = removed.next

                if removed == self.tail: # last node removed
                    self.tail = prev # set prev one before removed node as tail
                
            self.length -= 1

            return True

        

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head
        for i in range(self.length):
            arr.append(curr.value)
            curr = curr.next

        return arr

        
