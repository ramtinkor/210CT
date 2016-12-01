def LookingFpsqr(PosINt):
  
  """function to find highest possible square. recives postive integer which it calculates to see if it is a perfect square if not the function calls itself but this time -1 until eventually the highest perfect square is found"""
  
  if PosINt==1:#advoid errors
   return(print("the highest perfect square is",PosINt))
    
    
  square = PosINt // 2
  shown = set([])
  while square * square != PosINt:#a perfect square is one which can be expressed by two postive integers

    square = (square + (PosINt // square)) // 2#formula
    
    if square in shown: 
      return LookingFsqr(PosINt-1)#if found not to be an perfect square call the function again this time -1 from the input until a perfect square is found
      
    shown.add(square)#not square
 

  print("the highest perfect square is",PosINt)#shows highedt perfect square 


LookingFsqr(8)  
