def deleteduplicates(nums):
    result=[]

    for i in nums:
        if i not in result:
            result.append(i)

    return result

print(deleteduplicates([1,1,2,3,3]))