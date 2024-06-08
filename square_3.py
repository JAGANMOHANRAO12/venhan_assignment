from typing import List 
def sum_of_squares(lst: List[int]) -> int:  
   sums=0  
   for i in lst:
      sums+=i**2         
   return sums 
       
lists=list(map(int,input().split()))
result=sum_of_squares(lists)
print(result)