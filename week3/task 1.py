
def wordReverser(Astring):
  
  spaces=" "#used with split to identify words and later with join to add them back as separate words
  
  Astring=Astring.split(spaces)#split the words/goes into a list
  
  Astring=spaces.join(Astring[::-1])#joins the words 
  
  return Astring
  
print(wordReverser("awesome this is"))
