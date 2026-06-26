y = str(input("Enter your String TO Arrange in alphabetical Order : "))
s=list(y)

print(y)
for i in range (0,len(s)-1):
    for j in range ( i+1,len(s)):
        if(s[i]>s[j]):
           temp = s[i]
           s[i]=s[j]
           s[j] = temp
print(s) 
