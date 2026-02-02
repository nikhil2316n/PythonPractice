str1='Nikhil Sagar'

vowels='aeiou'

count=0
for i in range(len(str1)):
    for j in range(len(vowels)):
        if str1[i]==vowels[j]:
            print(str1[i])
            count+=1
print(f"The total number of vowels are: {count}")