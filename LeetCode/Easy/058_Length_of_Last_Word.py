class Solution(object):
    def lengthOfLastWord(self, s):
        count=0

        for ch in s[::-1]:
            if ch!=" ":
                count+=1
            elif count>0:
                break
        return count

print(Solution().lengthOfLastWord("hello world"))