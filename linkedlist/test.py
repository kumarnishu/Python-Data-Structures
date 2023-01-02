import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.size=5000
        self.llist=LinkedList()
        for i in range(0,self.size):
            self.llist.insert_end(i)
        super().setUp()
    
    def test_list_size(self):
        self.assertEqual(self.llist.length(), self.size)#size should be 5
    
    def test_empty_list(self):
        self.assertNotEqual(self.llist.head, None)#should not None

    def test_find_position(self):
        pos=self.llist.find_pos(2)
        if pos is not None:
            self.assertEqual(pos,3)#must be 3
    
    def test_find_item(self):
        item=self.llist.find_item(2)
        if item is not None:
            self.assertEqual(item,1)#must be 1

    def test_reverse(self):
        temp=self.llist.head
        while(temp):
            temp=temp.next
        last_node=temp
        self.llist.reverse()
        self.assertNotEqual(last_node,self.llist.head)#must be same
        
    def test_insert_beginning(self):
        self.llist.insert_beginning(22)  
        self.assertEqual(self.llist.head.data, 22)#should be 22
        self.llist.insert_beginning(21)  
        self.assertEqual(self.llist.head.data, 21)#should be 21

    def test_insert_after(self):
        temp=self.llist.head
        prev_item=4
        passed=False
        self.llist.insert_after(prev_item, 11)
        while(temp):
            if temp.data==prev_item:
                self.assertEqual(temp.next.data,11)#must be 11
                passed=True
                break
            temp=temp.next
        if not passed:
            self.assertEqual(temp,None)#must be None
       
    def test_insert_end(self):
        temp=self.llist.head
        while(temp.next):
            temp=temp.next
        self.llist.insert_end(13)
        self.assertEqual(temp.next.data,13)#must be 13
        self.assertEqual(temp.next.next,None)#must be None
    
    def test_delete_first(self):
        temp=self.llist.head
        self.llist.delete_first()
        self.assertEqual(temp.next,self.llist.head) #must be equal
    
    def test_delete_item(self):
        temp=self.llist.head
        item=4
        while(temp.next.data!=item):
            temp=temp.next
        next_node=temp.next.next
        self.llist.delete_item(4)
        self.assertEqual(temp.next,next_node) #must be equal

    def test_delete_last(self):
        temp=self.llist.head
        while(temp):
            temp=temp.next
        self.llist.delete_last()
        self.assertEqual(temp,None)#must be None
    

if __name__ == '__main__':
    unittest.main()
