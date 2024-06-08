from typing import List  
  
def find_duplicates(arr: List[int]) -> List[int]:  
   seen = set()     
   duplicates = set()  
      
   for num in arr:         
      if num in seen:  
         duplicates.add(num)         
      else:  
         seen.add(num)  
      
   return list(duplicates)  
  
lists=list(map(int,input().split()))
result=find_duplicates(lists)
print(result)