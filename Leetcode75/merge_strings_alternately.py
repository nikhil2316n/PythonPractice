x='ab'
y='pqrs'

test=''
ptr1=0
ptr2=0
if len(x)>len(y):

    while(ptr2<len(y)):
        test=test+x[ptr1]
        test=test+y[ptr2]
        ptr1+=1
        ptr2+=1
    test=test+x[ptr1:]


else:
    while(ptr1<len(x)):
            test=test+x[ptr1]
            test=test+y[ptr2]
            ptr1+=1
            ptr2+=1
    test=test+y[ptr2:]

print(test)