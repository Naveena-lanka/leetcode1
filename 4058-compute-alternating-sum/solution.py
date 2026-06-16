class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        odds=0
        evens=0
        for i in range(len(nums)):
            if i%2==0:
                evens+=nums[i]
            else:
                odds+=nums[i]
        return evens-odds
