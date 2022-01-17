class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, sums = 0, 0
        running_sum = defaultdict(int)
        running_sum[0] = 1
        
        for n in nums:
            sums += n
            count += running_sum[sums-k]

            running_sum[sums] += 1
            # print(sums,count,running_sum)

        return count