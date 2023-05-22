def solution(a):
   
   
   count= inputstring.count("(")
  for i in range(count):
       index1= inputstring.rindex("(")
       index2= inputstring[index1:].index(")")
       
       substring= inputstring[index1+1:index1:+ index2][::-1]
       inputsring= inputsring[:index1]+ substring + inputstring[index1+ index2+1:]
