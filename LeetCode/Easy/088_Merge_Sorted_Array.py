class Solution(object):
    def merge(self,nums1,m,nums2,n):
        for i in range(n):
            nums1[m+i]=nums2[i]

        nums1.sort()
        return nums1
    
print(Solution().merge([1,2,3,0,0,0],3,[2,5,6],3))

