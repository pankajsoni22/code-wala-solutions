## TWO SUM
### Problem Statement
_Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice._
You can return the answer in any order.
 
__Example 1:__  
Input: nums = [2,7,11,15], target = 9  
Output: [0,1]  
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].  
  
__Example 2:__  
Input: nums = [3,2,4], target = 6  
Output: [1,2]  
  
**Example 3:**  
Input: nums = [3,3], target = 6  
Output: [0,1]  
  
   
Constraints:  
2 <= nums.length <= 10<sup>4</sup>  
-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>  
-10<sup>9</sup> <= target <= 10<sup>9</sup>  
Only one valid answer exists.  

### Let's understand the problem
1. Given array is not sorted
2. Exactly one solution is guaranteed  i.e. nums[i]+nums[j]=target such number  one and only one pair is available
3. for nums[i]+nums[j]==target, i!=j
4. we can't use same number twice but think numbers can repeat in the array i.e. same number from different indices can be picked.
5. Always keep the constraints in the mind.

Always try to take a simple input as example test case and build logic over it.
example test case: 
nums=[-2, 0, -1 ,0, 4, 2], target=3

#### Think about brute-force solution
1. simply target=nums[i]+nums[j] and let say i < j, so nums[j] = target-nums[i] call nums[j] as remaining
2. if we have nums[i], search for remaining in rest of the array i.e. right of index i because i < j
3. for every nums[i] we search nums[j] or remaining in the array will cost O(n<sup>2</sup>) solution
**NOTE**: Coding practice of a brute-force solution is always a good practice this may seem useless but optimization comes from brute-force let see how?

Put your finger on your head and start thinking about 3<sup>rd</sup> point mentioned above...

**search for remaining** takes O(n) can we optimize searching of an element in an array?
let's talk about it a bit
1. If array is sorted it takes O(log(n)) using binary search - but the current situation does not support us for the same
    - This leaves us with an idea of first sort the array (Okay good idea, we'll talk about it [here](./2sum-with-sorted-array.py))
2. When we talk about searching efficiently we always has hashmap at the top ([two pass solution](./2sum-2pass-solution.py), [one pass solution](./2sum-1pass-solution.py))
    - Hashmap solution fits with O(n) TC and O(n) SC (actually more than n because hash table is not memory efficient, we'll talk about it in upcoming sessions)