class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.searchHelper(nums, 0, len(nums) - 1, target)
    
    # Method 3 - Recursion
    def searchHelper(self, nums, min, max, target):
        if min > max:
            return -1
        mid = (min + max) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.searchHelper(nums, mid +1, max, target)
        else:
            return self.searchHelper(nums, min, max - 1, target)
        
        
        # Method 1 - Time limit exceeded??
#         min, max = 0, len(nums) - 1
        
#         while min <= max:
#             mid = (min + max)//2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 min = mid + 1
#             else:
#                 min = mid - 1
                
#         return -1


        # Method 2 - same as 1 but works ??
#         low = 0
#         high = len(nums) - 1
#         mid = 0
        
#         while low <= high:
#             mid = (high + low) // 2
#             if target == nums[mid]:
#                 return mid
#             elif nums[mid] < target:
#                 low = mid + 1
#             elif nums[mid] > target:
#                 high = mid - 1        
#         return -1

# ===============

class Solution:
    # memoizing = remember the old values you've computed so you don't recompute them again
 
    def fib(self, n: int) -> int:
        computedValues = {0:0, 1:1}
        return self.memoizedFib(n, computedValues)    
    
    def memoizedFib(self, n, computedValues):
        if n in computedValues:
            return computedValues[n]
        computedValues[n] = self.memoizedFib(n-1, computedValues) + self.memoizedFib(n-2, computedValues)
        return computedValues[n]
        
    
    
    
    
#     def fib(self, n: int) -> int:
        
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
        
#         return self.fib(n-1) + self.fib(n-2)

# ===============

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        min, max = 1, n
        
        while min <= max:
            mid = (min + max) // 2
            
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res == -1:
                max = mid -1
            else:
                min = mid + 1
                
        return -1