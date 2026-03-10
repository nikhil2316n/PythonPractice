str1="The longest word in a sentence sentenc1"

words=str1.split()

print(words)
longest=''

for word in words:
    if len(word)>len(longest):
        longest=word
print(f"Longest word in ""{str1}"" is :")
print(longest)
