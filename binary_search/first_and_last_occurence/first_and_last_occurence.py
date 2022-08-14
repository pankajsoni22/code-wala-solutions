class Solution:
    def binarySearch(self, nums, target, isFirst):
        left, right=0, len(nums)-1
        mid=right//2
        while left<=right:
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                if (isFirst and mid!=0 and nums[mid-1]==nums[mid]) or (not isFirst and mid!=len(nums)-1 and nums[mid+1]==nums[mid]):
                    if isFirst:
                        right=mid-1
                    else:
                        left=mid+1
                else:
                    return mid
            mid=(left+right)//2
        return -1
    
    
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if not nums:
            return res
        
        res[0]=self.binarySearch(nums, target, True)
        if res[0]!=-1:
            res[1]=self.binarySearch(nums, target, False)
        
        return res