class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
class LinkedList:
    def __init__(self):
        # 哨兵结点
        self.head = Node()
        self.length = 0
    
    def peek(self):
        # O(1)
        if not self.head.next:
            raise Exception('LinkedList is empty')
        return self.head.next
    
    def get_last(self):
        # O(n)
        if not self.head.next:
            raise Exception('LinkedList is empty')
        p = self.head
        while p.next != None:
            p = p.next
        return p
    
    def get(self, index):
        # O(n)
        if (index < 0 or index >= self.length):
            raise Exception( 'index is out of bound' );
        if not self.head.next:
            raise Exception( 'LinkedList is empty' )
        p = self.head.next
        for i in range(index):
            p = p.next
#         while index != 0:
#             p = p.next
#             index -= 1
        return p
    
    def add_first(self, value):
        # O(1)
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.length += 1
    
    def add_last(self, value):
        # O(n)
        node = Node(value)
        p = self.head
        while p.next != None:
            p = p.next
        p.next = node
        self.length += 1
    
    def add(self, index, value):
        # O(n)
        if (index < 0 or index > self.length):
            raise Exception( 'index is out of bound' )
        if not self.head.next:
            raise Exception( 'LinkedList is empty' )
        node = Node(value)
        p = self.head
        for i in range(index):
            p = p.next
        node.next = p.next
        p.next = node
        self.length += 1
    
    def remove_first(self):
        # O(1)
        if not self.head.next:
            raise Exception( 'LinkedList is empty' )
        value = self.head.next
        self.head.next = self.head.next.next
        self.length -= 1
        return value
    
    def remove_last(self):
        # O(n)
        if not self.head.next:
            raise Exception( 'LinkedList is empty' )
        p = self.head.next
        pre = self.head
        while p.next != None:
            pre = p
            p = p.next
        pre.next = None
        return value
    
    def remove(self, index):
        # O(n)
        if (index < 0 or index > self.length):
            raise Exception( 'index is out of bound' )
        if not self.head.next:
            raise Exception( 'LinkedList is empty' )
        p = self.head
        for i in range(index):
            p = p.next
        result = p.next
        p.next = result.next
        result.next = None
        self.length -= 1
        return result.value
    
    def printlist(self):
        # O(n)
        node = self.head.next
        count = 0
        while node and count < 20:
            print(node.value, end=" ")
            node = node.next
            count += 1
        print("")