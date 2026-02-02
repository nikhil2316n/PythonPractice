num=121

st=str(num)
st1=''

for i in range(1,len(st)+1):
    st1=st1+st[-i]

if st1==st:
    print('hi babu thinara')
else:
    print("ledu thinale")