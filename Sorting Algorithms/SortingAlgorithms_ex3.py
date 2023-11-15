
def partition(arr,low,high):

    pivot = arr[high]
    i = low - 1 
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[j] , arr[i] = arr[i] , arr[j]

    arr[i+1] , arr[high] = arr[high] , arr[i+1]


    return i+1





def quickSort(arr , low , high):

    if(low < high):

        pi=partition(arr,low,high)


        quickSort(arr,low , pi-1 )
        quickSort(arr,pi,high)
    





if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    n = len(arr)
    quickSort(arr, 0 , n-1 )
    print("Sorted array: " , end= '')
    print(arr)
    