





def find_max_min(arr : list) -> list:
    max_num = max(arr)
    min_num = min(arr)
    
    return [min_num,max_num]






def main():
    #tests
    lst = []
    # number of elements as input
    n = int(input("Enter number of elements : "))
    # iterating till the range
    for i in range(0, n):
        ele = int(input())
        # adding the element
        lst.append(ele)  
 
    print(find_max_min(lst))






if __name__ == "__main__":
    main()