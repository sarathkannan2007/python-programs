l=[]

length = int(input("Enter the number of elements to be added: "))
for i in range (0,length):
    num = int(input("Enter the element : "))
    l.append(num)
    
for j in range (1,len(l)):
    for i in range (j,0,-1):
      if l[i] < l[i-1]:
        temp = l[i]
        l[i] = l[i-1]
        l[i-1] = temp
        
      else:
        break

print(l)  
