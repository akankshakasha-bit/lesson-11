base=int(input("enter the base number: "))
power=int(input("enter the power: "))
result=1
i=1
while i<=power:
    result=result/base
    i+=1
print("result", result)