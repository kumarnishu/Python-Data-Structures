# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class
class LinkedList:
    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None  # assign null to head node

    # function to insert node at front
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # function to insert node after a given node
    def insert_after(self, prev_item, data):
        temp = self.head
        while temp:
            if temp.data == prev_item:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print("item not found in the linkedList")
        return

    # function to insert node at last
    def insert_end(self, data):
        new_node = Node(data)

        # if linkedList is empty then new node is head
        if self.head is None:
            self.head = new_node
            return
        # else traverse to the last node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # function to print the whole linkedList
    def print(self):
        temp = self.head
        while temp:
            print("->", temp.data)
            temp = temp.next

    # count the length of linkedList
    def length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    # function to check empty linkedList
    def is_empty(self):
        if self.head is None:
            return True
        return False

    # function to print pos of item
    def find_pos(self, item):
        temp = self.head
        count = 0
        while temp:
            count += 1
            if temp.data == item:
                print(f"{item}  found at {count} position in the linkedList")
                return
            temp = temp.next
        print(f"{item}  not found  in the linkedList !UnderFlow")

    # function to find nth node iterative
    def find_item(self, pos):
        temp = self.head
        counter = 0
        while temp:
            counter += 1
            if counter == pos:
                print(f"at {pos} position  {temp.data} found in the linkedList")
                return
            temp = temp.next
        print(f"{pos} position not a valid position !Underflow")

    # function to delete item from start
    def delete_first(self):
        temp = self.head
        self.head = temp.next
        del temp

    # function to delete an element
    def delete_item(self, item):
        temp = self.head
        prev_node = None
        while temp:
            prev_node = temp
            temp = temp.next
            if temp.data == item:
                break
        prev_node.next = temp.next
        del temp

    # function to delete from end
    def delete_last(self):
        temp = self.head
        prev_node = None
        while temp.next:
            prev_node = temp
            temp = temp.next
        prev_node.next = temp.next
        del temp

    # function to search an element Recursive method
    counter = 0

    def search(self, head, item):
        if head is None:
            print("item not exists !overflow")
            return True
        if head.data == item:
            print(f"{item} found")
        else:
            self.search(head.next, item)
        print("item not found in the linkedList")

    # reverse a linked linkedList
    def reverse(self):
        current_node = self.head
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
        self.print()


if __name__ == '__main__':
    linkedList = LinkedList()
    for i in range(1, 5):
        linkedList.insert_end(i)
    linkedList.delete_last()
    linkedList.print()
