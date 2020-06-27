class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def printList(self):
        cur_node = self.head
        while cur_node: 
            print(cur_node.data)
            cur_node = cur_node.next

    
    def size(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count


    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node


    def insert(self, prev_node, data):
        if not prev_node:
            print("Previous node is not present in the list.")
            return
        
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node


    def insert2(self, index, data):
        if index >= self.size():
            print("Index out of bounds")
        elif index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            position = 0
            cur_node = self.head
            prev_node = self.head
            while cur_node:
                if position == index:
                    new_node = Node(data)
                    new_node.next = cur_node
                    prev_node.next = new_node
                    break
                
                prev_node = cur_node
                cur_node = cur_node.next
                position += 1
    
    def delete(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node = None
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node = None


    def remove(self, position):
        cur_node = self.head

        if position == 0:
            self.head = cur_node.next
            cur_node = None

        prev_node = None
        count = 0
        while cur_node and count != position:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node = None

    
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev
        

if __name__ == "__main__":
    llist = LinkedList()
    llist.append("a")
    llist.append("b")
    llist.append("c")
    llist.append("d")

    llist.printList()
