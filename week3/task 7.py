def primeNumber(num,num2):
  """user enters the value they want checked (twice) and function returns if it's a prime number or not by method of recursion"""
  
  num2=num2-1
  a=num/num2

  if num2==1:
    return print("is a prime number")

  
  if (a).is_integer()==True:
    return(print("not a prime"))
    
  if num/num2!=type(int):
    return primeNumber(num,num2)
    

primeNumber(5,5)
