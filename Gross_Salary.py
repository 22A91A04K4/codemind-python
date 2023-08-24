a=int(input())
if a<=10000:
    da=a*0.8
    hra=a*.2
elif a<=20000:
    da=a*0.9
    hra=a*0.25
elif a>20000:
    da=a*0.95
    hra=a*0.3
gs=a+da+hra    
print(f"{gs:.2f}")    