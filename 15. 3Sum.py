class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        for index, x in enumerate(nums):
            tail = index + 1
            head = len(nums) - 1
            while head > tail:
                if x + nums[head] + nums[tail] == 0:
                    print(index, tail, head)
