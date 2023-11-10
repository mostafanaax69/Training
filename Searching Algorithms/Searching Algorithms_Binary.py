def Binary_search(arr, N, x): 
    
    #arr should be sorted so make sure to use a sorted array or basiclly uncomment this line :
    #arr.sort()
    low = 0 
    high = N-1

    while low <= high :
        mid = low + (high-low) // 2 ## can be written as low + high // 2 but take care of overfloww

        if (arr[mid] == x): 
            return mid
        elif ( arr[mid] > x) :
            high = mid -1 
        else:
            low = mid + 1

    return -1
  
  
if __name__ == "__main__": 
    arr = [2, 3, 4, 10, 40] 
    x = 10
    N = len(arr) 
  
    # Function call 
    result = Binary_search(arr, N, x) 
    if(result == -1): 
        print("Element is not present in array") 
    else: 
        print("Element is present at index", result) 