class Solution(object):
    def mysqrt(self,x):
        for i in range(x+1):
            if i*i>x:
                return i-1

        return x

print(Solution().mysqrt(4))