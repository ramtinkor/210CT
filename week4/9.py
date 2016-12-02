def binarySearch(alist,Low,High):
“” checking using Binary search  if a value within an interval given by the user(two numbers, one lower than the other, ) is in a list. 


 firstE = 0
 lastE = len(alist)-1
 found = False
  
 for x in range(Low,High+1):
  print (x)
  
  if firstE<=lastE and found==False:
    halfway = (firstE + lastE)//2
    
    if alist[halfway] == x:
      found = True
      return True
    
    else:
      if x < alist[halfway]:
        lastE = halfway-1
        
      else:
         firstE = halfway+1
         
 return found


searchL = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(SearchL,5,9))
