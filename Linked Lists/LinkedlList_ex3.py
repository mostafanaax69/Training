
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


    def is_cycle(self):
        curr_slow = self.head
        curr_fast = self.head

        while(curr_slow and curr_fast!= None and curr_fast.next != None):
            curr_slow = curr_slow.next
            curr_fast = curr_fast.next.next
            if curr_slow == curr_fast:
                #there is a loop  Floyd’s Cycle-Finding Algorithm 
                return True 
        

        return False


    















def main():
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)
    llist.push(90)

    llist.head.next.next.next.next = llist.head
    res = llist.is_cycle()
    if(res):
        print("There is a LOOP :( ")
    else:
        print("There is NO LOOP :D ")

    









if __name__ == "__main__":
    main()