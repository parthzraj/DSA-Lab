def quickSort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[x for x in arr[1:] if x<=pivot]
    right=[x for x in arr[1:] if x>pivot]
    return quickSort(left)+[pivot]+quickSort(right)
n=int(input("enter the number of elements:"))
arr=list(map(int , input("enter the elemennts:").split() ))
arr=quickSort(arr)
print("sorted_array:",arr)