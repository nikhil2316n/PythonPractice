# # You have a bomb to defuse, and your time is running out! Your 
# # informer will provide you with a circular array code of length of n and a key k.
# # To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

# # If k > 0, replace the ith number with the sum of the next k numbers.
# # If k < 0, replace the ith number with the sum of the previous -k numbers.
# # If k == 0, replace the ith number with 0.
# # As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

#Example :
# Input: code = [5,7,1,4], k = 3
# Output: [12,10,16,13]
# Explanation: Each number is replaced by the sum of the next 3 numbers.
#  The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.


nums=[1,2,3,4,5,6,7,8,9]
start=3
n=len(nums)
for i in range(n):
    index=(start+i)%n
    print(nums[index])