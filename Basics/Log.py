#Calculation Of Log Value
import math
x = int(input("Enter The number To find Logarthm : "))
m = 0;
print("Actual Log Value : ",round(math.log(x,2)))
while x>0:
   
        m=m+1
        x=x//2
a = 2**m
print("Approx Log value : ",m)
