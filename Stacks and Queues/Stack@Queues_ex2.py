

class Queue:
 
    def __init__(self):
        # Two inbuilt queues
        self.s1 = []
        self.s2 = []
 
    def Enqueue(self, x):
        self.s1.append(x)

    def Dequeue(self):
         
        #case 1 : both empty
        if len(self.s1) == 0 and len(self.s2) == 0:
            return -1
        
        #case 2 the dequeue stack which is s2 is empty so we transfer elements from s1 in an oppsoite way
        elif len(self.s2) == 0 and len(self.s1) > 0 : 
            while len(self.s1) > 0 :
                self.s2.append(self.s1.pop())
            #now the stack is "mirrored like a queue" , bottom elemnt in s1 is top element in s2 == FIFO
            return self.s2.pop()
        #case 3 which is that the s2 stack which is the dequeue stack is not empty which means the element in it should be out first 
        return self.s2.pop()
    
    def front(self) -> int:
        #case 1 : both empty
        if len(self.s1) == 0 and len(self.s2) == 0:
            return -1
        
        #case 2 the dequeue stack which is s2 is empty so we transfer elements from s1 in an oppsoite way
        elif len(self.s2) == 0 and len(self.s1) > 0 : 
            while len(self.s1) > 0 :
                element = self.s1.pop()
                self.s2.append(element)
            #now the stack is "mirrored like a queue" , bottom elemnt in s1 is top element in s2 == FIFO
            return self.s2[-1]
        

        #case 3 which is that the s2 stack which is the dequeue stack is not empty which means the element in it should be out first 
        return self.s2[-1]






        

    


if __name__ == '__main__':
    q = Queue()
    q.Enqueue(1)
    q.Enqueue(2)
    q.Enqueue(3)
 
    print(q.Dequeue())
    print(q.Dequeue())
    print(q.Dequeue())