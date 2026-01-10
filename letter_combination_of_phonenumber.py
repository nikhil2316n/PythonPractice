class Solution:
    def letterCombinations(self, digits):
        
        if digits == "":
            return []

        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []

        def backtrack(i, current):
            # i = index of digit  #example i=0,current='',digit=23
            # current = word formed so far

            if i == len(digits): 
                result.append(current)
                return

            for j in phone[digits[i]]:# digits[i]=> 2 , j in phone[2]=> 'abc' , j=>a->b->c
                backtrack(i + 1, current + j)

        backtrack(0, "")
        return result

obj=Solution()
print(obj.letterCombinations('23'))