import sys
sys.path.insert(0,"C:/Users/sidd/Desktop/Linked_List/")
import linkedlist


mylinkedlist=linkedlist.linkedlist()
mylinkedlist.add_from_begin(22)
mylinkedlist.add_from_begin(24)
mylinkedlist.add_from_begin(22222)
mylinkedlist.add_from_begin(900)
mylinkedlist.add_from_end(1000)
mylinkedlist.traverse()
print("******")
mylinkedlist.delete_a_node_front()
mylinkedlist.traverse()
print("******")
mylinkedlist.delete_a_node_end()
mylinkedlist.traverse()
print("******")
mylinkedlist.count_nodes()
