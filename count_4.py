def count_frequencies(s: str) -> dict:  
   frequency_dictionary = {}     
   for c in s:  
        frequency_dictionary[c]=s.count(c)     
   return frequency_dictionary 

strs=input("Enter a word")
result=count_frequencies(strs)
print(result)