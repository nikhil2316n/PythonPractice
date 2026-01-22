str1='Nnikhilsagarrr'.lower()

# dict={}
# for i in str1:
#     dict[i]=str1.count(i)
# print(dict)

# print("The Non repeating character in string are")
# for j in dict:
#      if dict[j]==1:
#           print(j)

for ch in str1:
    if str1.count(ch)==1:
        print(ch)