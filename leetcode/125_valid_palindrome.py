
s='A man, a plan, a canal: Panama'
s=s.lower()
left=0
right=len(s)-1
while(left<right):
    if not s[left].isalnum():
        left+=1

    elif not s[right].isalnum():
        right-=1

    elif(s[left]==s[right]):
        left+=1
        right-=1
    else:
        print("not a palindrome")
        break

else:
    print("palindrome")