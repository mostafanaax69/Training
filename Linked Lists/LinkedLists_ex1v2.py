
class ListNode:
   def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.val, end=" ")
            temp = temp.next


    def reverseList(self):
        prev = None
        next = None
        curr = self.head

        while(curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        

        self.head = prev


    





        




def main():
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)

    llist.reverseList()
    llist.printList()









if __name__ == "__main__":
    main()