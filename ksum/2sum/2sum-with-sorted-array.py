'''
This code is written and maintained by instainterview team
if you find any bug or
'''
class Solution:
    def twoSum(self, nums, target):
        nums.sort() # nums is sorted and took O(n.log(n)) TC

        '''
        we have nums array sorted now, can ordering the number give us some advantage ?
        may be yes - how ?
        example test case: 
        nums=[-2, 0, -1 ,0, 4, 2], target=3
        nums.sort() # [-2, -1, 0, 0, 2, 4] 
        think : left to right number increases
        right to left number decreases
        lets have left at 0 and right at last_index
        temp_sum=nums[left]+nums[right]
        temp_sum will increase if we go from left to right i.e. increase left one by one
        temp_sum will decrease if we go from right to left i.e. decrease right one by one
        keep checking target value
        '''
        left, right=0, len(nums)-1
        indices=[]
        while left<right:
            temp_sum=nums[left] + nums[right]
            if temp_sum < target: # can we optimize this condition for repeated values? yes -> add (left>0 and nums[left-1]==nums[left])
                # try to increase temp_sum
                left+=1
            elif temp_sum > target:  # can we optimize this condition for repeated values? yes -> add (right<len(nums)-1 and nums[right+1]==nums[left])
                # try to decrease temp sum
                right-=1
            else:
                # i.e. we find the numbers so return indices or numbers which ever 
                # required in solution
                indices=[left, right]
                break
        '''
        while left<right:
            temp_sum=nums[left] + nums[right]
            if temp_sum < target or (left>0 and nums[left-1]==nums[left]):
                # don't process repeated values as they have same temp_sum
                # try to increase temp_sum
                left+=1
            elif temp_sum > target or (right<len(nums)-1 and nums[right+1]==nums[right]):
                # don't process repeated values as they have same temp_sum
                # try to decrease temp sum
                right-=1
            else:
                # i.e. we find the numbers so return indices or numbers which ever 
                # required in solution
                indices=[left, right]
                break
        '''
        return indices



