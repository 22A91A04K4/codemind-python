import math  
a=int(input())
b=int(input())
c=int(input())
d=int(input())
dis=((c-a)*(c-a)+(d-b)*(d-b))
r=math.sqrt(dis)
print(f"{r:.4f}")