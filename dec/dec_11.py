#%%

# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3562/

def removeDuplicates(nums):
    toDelete = []
    for i in range(len(nums) - 2):
        if (nums[i] == nums[i + 1] and nums[i] == nums[i + 2]):
            toDelete.append(i + 2)
    
    toDelete.reverse()
    for i in toDelete:
        del nums[i]
    
    return len(nums)


nums = [0,0,1,1,1,1,2,3,3]
removeDuplicates(nums)
print(nums)
