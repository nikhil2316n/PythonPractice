str1=input("Enter the string 1 :").lower()
str2=input("Enter the string 2 :").lower()

freq1={}
freq2={}
for i in str1:
    freq1[i]=str1.count(i)
for j in str2:
    freq2[j]=str2.count(j)

if freq1==freq2:
    print("strings are anagrams")

else:
    print("strings are not anagrams")