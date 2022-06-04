class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = math.inf
        freq = {}
        for i, val in enumerate(nums):
            l, r = i+1, len(nums)-1
            while l < r: 
                three_sum = nums[l] + nums[r] + val 
                freq[three_sum] = abs(three_sum-target)
                if three_sum > target: 
                    r -= 1
                elif three_sum < target:
                    l += 1
                else: 
                    return target
        # print(nums)
        return min(freq, key=freq.get)
                
        