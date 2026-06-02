s='abc'
t='ahbgdc'
def isSubsequence(s,t):
    s1=list(s)
    t1=list(t)
    if len(s1)>len(t1):
        s1,t1=t1,s1

    ptr1=0
    ptr2=0
    while(ptr1<len(s1) and ptr2<len(t1)):
        if(s1[ptr1]==t1[ptr2]):
            ptr1+=1
        ptr2+=1
    
    return ptr1==len(s1)
print(isSubsequence(s,t))
