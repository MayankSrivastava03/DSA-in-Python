class Solution:
    def customSortString(self, order: str, s: str) -> str:
        letter_count = {}
        for char in s:
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
        res = ""
        for i in order:
            if i in s:
                while(letter_count[i]!=0):
                    res += i
                    letter_count[i] -=1
        for i in letter_count:
            while letter_count[i] > 0:
                res += i
                letter_count[i] -= 1
        return res
