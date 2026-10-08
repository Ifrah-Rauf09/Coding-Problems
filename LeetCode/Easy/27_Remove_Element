class Solution(object):
    def removeElement(self, nums, val):
        j=0

        for i in range(len(nums)):
            if nums[i]!=val:
                nums[j]=nums[i]
                j+=1
        return j

if __name__ == "__main__":
    nums=[3,2,3,2]
    val=3
    k=Solution().removeElement(nums,val)
    print(k, nums[:k])