class Solution:
    def twoSum(self, nums, target):
        '''
        one pass solution
        '''
        presence=dict()
        for i in range(len(nums)):
            remaining=target-nums[i]
            if remaining in presence:
                return sorted([presence[remaining], i])
            presence[nums[i]]=i
