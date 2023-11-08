


def reverse_first(arr : list) -> list:
    arr.reverse()






def reverse_second(arr : list) -> list:
    left = 0
    right = len(arr)-1
    while (left < right):
        # Swap
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
 
    return arr
    






def main():
    #tests
    lst = []
    # number of elements as input
    n = int(input("Enter number of elements of the list you want to reverse : "))
    # iterating till the range
    for i in range(0, n):
        ele = int(input())
        # adding the element
        lst.append(ele)  
 
    #res = reverse_first(lst)
    res = reverse_second(lst)
    for i in lst:
        print(i , end=" ")






if __name__ == "__main__":
    main()