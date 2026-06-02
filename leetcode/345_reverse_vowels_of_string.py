s = "leetcode"
s1=list(s)
ptr1=0
ptr2=len(s)-1

while(ptr1<ptr2):
    if s1[ptr1] in 'AEIOUaeiou':
        if s1[ptr2] in 'AEIOUaeiou':
            s1[ptr1],s1[ptr2]=s1[ptr2],s1[ptr1]
            ptr2-=1
            ptr1+=1
        else:
            ptr2-=1
    else:
        ptr1+=1


print(''.join(s1))