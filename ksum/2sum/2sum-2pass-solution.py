class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        two pass hashmap: once put the nums in hashmap as value: index 
        then start searching remaining
        '''

        # first pass - O(n)
        presence=dict()
        for i,val in enumerate(nums):
            presence[val]=i
        
        # second pass - O(n)
        indices=[]
        for i in range(len(nums)):
            remaining=target-nums[i]
            j=presence.get(remaining) # j is not None if already present in presence
            if j is not None and j!=i:
                indices=[i, j]
                break
        
        return indices
        
