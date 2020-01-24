a=input()
k=''
for i in a:
    if i not in k:
       
       b=a.count(i)
       print(i,':',b)
       k+=i  
    
