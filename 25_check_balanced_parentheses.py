s='({{[]}})'

lt=[]
x=0
for i in s:
    if i in '([{':
        lt.append(i)
    
    else:
        ch=lt.pop()
        if ((i ==")" and ch=='(') or (i =="}" and ch=='{') or (i =="]" and ch=='[')):
            x=1

            


if x==1:
    print("Balanced Parentheses")

else:
    print("UnBalanced Parentheses")
            
            
