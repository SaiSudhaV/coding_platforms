def removeDuplicates(self, nums):
    length = 1
    if len(nums)==0:
        return 0
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[length] = nums[i]
            length +=1
    return length
