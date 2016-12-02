def RmeVolsF(UStr):
  
    """user enters string checked for any vowels(lower & upperCase) if found then removed and returns string - all vowels """
    
    if UStr=="": # empty string
        return UStr#every possible element checked

    if UStr[0] in "AEIOUaeiou":
      return RmeVolsF(UStr[1:])#call function but only gives values starting form element 1 effectivly deleting the element if it contained a vowel
    
    return UStr[0]+RmeVolsF(UStr[1:])#if there wasn't vowel in the letter then return the element but call the function and check the next element
    
    
print(RmeVolsF("beautiful"))
