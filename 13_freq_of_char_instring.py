str1='NikhilSagaaagaggarrr'
str2=str1.lower()
dict={}

#   USING COUNT FUNCTION 

# for i in str2:
#     dict[i]=str2.count(i)
# print(dict)


for i in str2:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

print(dict)