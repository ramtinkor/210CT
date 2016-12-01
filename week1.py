
import random 
def theShuffler(intlist):
  
  """function takes argument in the form of a list(int only) which returns list elements shuffled""" 
  
  #testing to insure that the datatype entered is a list
  if type(intlist)==list:
    pass
  else:
    raise TypeError("please ensure you have entered a list")
  
  
  #insures that all elements in the list entered are integers
  for a in intlist:
    if type(a)==int:
      pass
    else:
      raise ValueError("please only enter integers")
      
 
  #this insures there are at least two elements so that some form of a shuffle can take place
  a=len(intlist)
  if a <2:
    print("please enter at least two elements in the list to be shuffled")
    
    
    
  numbercount=[]#this will later insure the samenumber doesn't show up twice
  newlist=[0]*a #creates a list with the same amount of elements as the user 
  
  for x in intlist:
    t=random.randint(0,(a-1)) #(a- 1) elements start from 0 so last index number is one lower than the amount of elements in the list
    
    while t in numbercount:
      t=random.randint(0,(a-1))#insures the same number doesn't come up twice
    
    newlist[t]=x #index number and element added
    numbercount.extend([t])#evertime a new number is added to insure it doesn't appear twice
  
  print (newlist)
  return newlist

  


###

def Counting0zz(Num2b):
  """function finds the factorial of a number input by the user and returns the amount of trailing zeros in said number"""

  xF=Num2b-1
  OFacNum=Num2b*xF
  
  #finding the factorial number 
  while xF>1:
    xF=xF-1
    OFacNum=OFacNum*xF
  
#OFacNum string length(now calculated factorial number) - OFacNum-trailing 0s(length) 

  TZeros=str(OFacNum) 
  print ("trailing zeros of",str(Num2b),"factorial","(",str(OFacNum),") is", len(TZeros)-len(TZeros.rstrip("0")))
  
  #rstrip removes specified character from end of string until reaching a character that differs.  
  

Counting0zz(5)



  
