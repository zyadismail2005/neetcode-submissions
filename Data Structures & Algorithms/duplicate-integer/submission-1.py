#class Solution:
#    def hasDuplicate(self, nums: List[int]) -> bool:
#        for i in range(len(nums) ): 
#            for j in range(i+ 1 , len(nums)): 
#                if nums[i] == nums[j]:
#                    return True 
#        else: 
#            return False 
            # you will need to pay more attention to the indentation as python is very strick when it comes to that : ) 


# the solution up there will work when it comes to the logic part but the efficency will be O(N*N) 
#And that wont satiate the constraints that we are given Constraints: 0 <= nums.length <= 10^5 /  -10^9 <= nums[i] <= 10^9



# The O(n) Solution 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = set()

        for i in nums:
            if i in seen: 
                return True

            seen.add(i)
        return False 










