def mergeSort(arr):
    
    if len(arr) > 1 : 
        mid = len(arr)//2
        
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L) # divide and sort first half
        mergeSort(R) # divide and sort second half

        i = j = k = 0 

        while j < len(L) and i < len(R):
            if L[j] < R[i] :
                arr[k] = L[j]
                j+=1
            else :
                arr[k] = R[i]
                i+=1
            
            k += 1

        while j< len(L):
            arr[k] = L[j]
            j += 1
            k += 1

        while i < len(R):
            arr[k] = R[i]
            i+= 1 
            k +=1 

            




if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    mergeSort(arr)
    print("Sorted array: " , end= '')
    print(arr)
    