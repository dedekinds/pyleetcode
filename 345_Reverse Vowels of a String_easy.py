
'''
345. Reverse Vowels of a String
2017.12.21
'''
前后双指针
class Solution:
    def reverseVowels(self, S):
        #[a.]  [b.]失败
        length=len(S)
        left=0
        right=length-1
        vowels=['a','e','i','o','u','A','E','I','O','U']
        s=list(S)
        while True:
            while left<length and s[left] not in vowels:
                left+=1
            while right>=0 and s[right] not in vowels:
                right-=1
            if left>=right:
                break
            s[right],s[left]=s[left],s[right]
            left+=1
            right-=1
        return ''.join(s)