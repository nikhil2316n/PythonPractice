#Given two strings needle and haystack, return the index of 
#the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


class Solution(object):
    def strStr(self, haystack, needle):
    

        n=len(haystack)
        m=len(needle)

        for i in range(n-m+1):
            j=0
            while j<m and haystack[i+j]==needle[j]:
                j+=1
            
            if j == m:
                return i
        return -1
    
haystack ='sadbutsad'
needle ='sad'
        
obj=Solution()
print(obj.strStr(haystack,needle))