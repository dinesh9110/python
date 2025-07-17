def insert_at_beginning(head,data):
    new_node=Node(data)
    new_node.next=head
    return new_node
head=None
head=insert_at_beginning(head,10)
head =insert_at_beginning(head,20)

temp=head
while temp:
    print(temp.data,end="--> ")
    temp=tem.next
print("None")