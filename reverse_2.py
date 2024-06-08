def reverse_string(s:str)->str:  
   return s[::-1]    
strs=input("Enter a word")
result=reverse_string(strs)
print(result)