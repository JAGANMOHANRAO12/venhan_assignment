def quicksort(arr):     
   if len(arr) <= 1: 
      return arr     
   else:  
      pivot = arr[0]  
      less_than_pivot = [x for x in arr[1:] if x <= pivot]         
      greater_than_pivot = [x for x in arr[1:] if x > pivot]  
      return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot) 
lists=list(map(int,input().split()))
result=quicksort(lists)
print(result)