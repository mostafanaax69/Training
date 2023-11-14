



def countbit_first(num) :
    #this program is o(log h) while h is the number for set bits

    cnt = 0 

    while (num != 0 ):
        num = num &(num-1)
        cnt += 1

    return cnt



def countbit_sec(num):
    #this program is o(log n) while n is the number for bits in num

    cnt = 0

    while (num != 0 ):
        if (num&1) : cnt +=1 
        num = num >>1

    return cnt




if __name__ == "__main__":
 
    n = input("Insert the number you want to count its bits number : ")
    print(countbit_first(int(n)))
 