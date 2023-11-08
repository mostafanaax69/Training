
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


    def middle_element(self):
        curr_slow = self.head
        curr_fast = self.head

        while(curr_fast!= None and curr_fast.next != None):
            curr_slow = curr_slow.next
            curr_fast = curr_fast.next.next
        

        return curr_slow


    















def main():
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)
    llist.push(90)
    res = llist.middle_element()
    print(res.val)
    









if __name__ == "__main__":
    main()