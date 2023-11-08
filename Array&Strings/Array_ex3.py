








def duplicate_first(arr : list) -> list:
    return set(arr)





def duplicate_sec(arr : list) -> list:
    n = len(arr)
    if n == 0 or n == 1:
        return n
 
    # To store index of next unique element
    swap = 0

    for i in range(n-1):
        if(arr[i] != arr[i+1]):
            arr[swap] = arr[i]
            swap = swap+1

    arr[swap] = arr[n-1]
    swap = swap + 1 
    return swap






def main():
    #tests
    lst = []
    # number of elements as input
    n = int(input("Enter number of elements of the sorted array : "))
    # iterating till the range
    for i in range(0, n):
        ele = int(input())
        # adding the element
        lst.append(ele)  
 
    #res = duplicate_first(lst)
    res = duplicate_sec(lst)
    for i in range(res):
        print(lst[i] , end=" ")






if __name__ == "__main__":
    main()