def twoSum(nums, target):
    my_map={}
    for i in range(len(nums)):
        if target - nums[i] in my_map:
            return [i, my_map[target-nums[i]]]
    my_map[nums[i]]=i


def twoSumBruteForce(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]