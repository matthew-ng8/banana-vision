# Initialise the Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Class for doubly Linked List
class doublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert Element to Empty list
    def InsertToEmptyList(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("The list is empty")
    
    # Insert element at the end
    def InsertToEnd(self, data):
        # Check if the list is empty
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        n = self.head
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
    
    # Delete the elements from the start
    def DeleteAtStart(self):
        if self.head is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.prev = None
    
    # Delete the elements from the end
    def delete_at_end(self):
        # Check if the List is empty
        if self.head is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None


    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                node.next.prev = new_node
                new_node.next = node.next
                node.next = new_node
                new_node.prev = node
                return

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.InsertToEmptyList(new_node, target_node_data)

        for node in self:
            if node.data == target_node_data:
                new_node.prev = node.prev
                node.prev.next = new_node
                node.prev = new_node
                new_node.next = node
                return


    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head.prev = None
            self.head = self.head.next
            return

        for node in self:
            if node.data == target_node_data:
                node.next.prev = node.prev
                node.prev.next = node.next
                return

    def getNode(self, index):
        if self.head is None:
            print("The list is empty")
            return
        node = self.head
        for i in range(index - 1) :
            if node.next is None:
                print("No node exists at index")
            node = node.next
        return node

    # Traversing and Displaying each element of the list
    def Display(self):
        if self.head is None:
            print("The list is empty")
            return
        else:
            n = self.head
            while n is not None:
                print("Element is: ", n.data)
                n = n.next
        print("\n")


# Create a new Doubly Linked List
NewDoublyLinkedList = doublyLinkedList()
# Insert the element to empty list
NewDoublyLinkedList.InsertToEmptyList(10)
# Insert the element at the end
NewDoublyLinkedList.InsertToEnd(20)
NewDoublyLinkedList.InsertToEnd(30)
NewDoublyLinkedList.InsertToEnd(40)
NewDoublyLinkedList.InsertToEnd(50)
NewDoublyLinkedList.InsertToEnd(60)
# Display Data
NewDoublyLinkedList.Display()
# Delete elements from start
NewDoublyLinkedList.DeleteAtStart()
# Delete elements from end
NewDoublyLinkedList.DeleteAtStart()
# Display Data
NewDoublyLinkedList.Display()