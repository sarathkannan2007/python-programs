l = [8,1,7,2,9]
for i in range (0,len(l)-1):
    minn = i
    for j in range (i+1,len(l)):
        if(l[minn]>l[j]):
           minn = j
    if(minn != i):
        temp = l[minn]
        l[minn] = l[i]
        l[i] = temp

print(l)
