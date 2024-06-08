def is_palindrome(s: str) -> bool:     
   return s == s[::-1] 

strs=input("Enter a word")
result=is_palindrome(strs)
if(result):
   print(True)
else:
   print(False)