class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_end(self,data):

        new_node=Node(data)

        if self.head is  None:
            self.head=new_node
            return

        temp=self.head
        while temp.next is not None:
            temp=temp.next

        temp.next=new_node

    def display(self):
        temp=self.head
        while temp.next is not None:
            print(temp.data,end=" > ")
            temp=temp.next

        print("None")
        

l1=LinkedList()
l1.insert_end(10)
l1.insert_end(20)
l1.insert_end(30)
l1.insert_end(40)
l1.insert_end(50)
l1.insert_end(60)

l1.display()
        