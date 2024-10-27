class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        nearestSum = float('inf') #Very big number
        for index, x in enumerate(nums):

            tail = index + 1
            head = len(nums) - 1

            while tail < head:
                total = x + nums[tail] + nums[head]

                if abs(total - target) < abs(nearestSum - target): nearestSum = total

                if total == target: return total

                if total < target: tail += 1

                if total > target: head -= 1
        
        return nearestSum
