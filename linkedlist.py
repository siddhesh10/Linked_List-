import sys
sys.path.insert(0,"C:/Users/sidd/Desktop/Linked_List/")
import node



class linkedlist:

    def __init__(self):
        self.head=None
        self.count=0

    def add_from_begin(self,data):
        self.count=self.count+1
        new_node=node.node(data)

        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node

    def add_from_end(self,data):
        new_node=node.node(data)
        self.count=self.count+1
        if self.head==None:
            self.head=new_node
        else:
            temp_node=self.head

            while(temp_node.next!=None):
                temp_node=temp_node.next

            temp_node.next=new_node

    def traverse(self):
        temp_node=self.head

        while(temp_node!=None):
            print(temp_node.data)
            temp_node=temp_node.next

        print("NuLL")

        #deleting head of a linkedlist
    def delete_a_node_front(self):
        self.count=self.count-1
        if self.head==None:
            print("Empty linkedlist")
        else:
            temp_node=self.head.next
            del self.head
            self.head=temp_node

    def  delete_a_node_end(self):
        self.count=self.count-1
        if self.head==None:
            print("EMpty Linked list")
        else:
            temp_node_1=self.head
            temp_node_2=self.head.next

            while(temp_node_2.next!=None):
                temp_node_1=temp_node_1.next
                temp_node_2=temp_node_2.next

            del temp_node_2
            temp_node_1.next=None

    def count_nodes(self):
        print(self.count)
