num1=[1,2,3,0,0,0]
num2=[2,5,6]
result=[]
a=0
b=0
i=0
m=len(num1)
n=len(num2)
while(a!=m & b!=n):
    if(num1[a]<=num2[b]):
        result[i]=num1[a]
        i=i+1
        a+=1

    else:
        result[i]=num2[b]
        i+=1
        b+=1

while(a<m):
    result[i]=num1[a]
    i+=1
    a+=1

while(a<n):
    result[i]=num2[b]
    i+=1
    b+=1


print(result)