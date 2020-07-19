n= int(input())
c = n
str1 = input()
str2 = input()
if len(str1)==4 and len(str2)==4:
  for i in str1:
    for j in str2:
      if i == 'r':
        if j == 'r':
          c-=1
        else:
          str2 = str2.replace(str2[-1],j)
          c+=1
      else:
        if j == 'm':
          c-=1
          
        else:
            str2 = str2.replace(str2[-1],j)
            c+=1
          
print(c)
        
