#Linear Search
l = [1,2,32,4,5,6,7,8,89]
found = 0
search = int(input("Enter The Number to be Searched: "))
for i in range (0,len(l)):
    if(l[i] == search):
        print("Element found at Index : ",i)
        found = 1
        break
if(found == 0):
     print("Element Not Found ")
