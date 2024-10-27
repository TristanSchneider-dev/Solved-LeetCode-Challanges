from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        threeSums = []

        for index, x in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                continue  # Überspringe gleiche Werte für x

            target = -x
            tail = index + 1
            head = len(nums) - 1
            
            while tail < head:
                current_sum = nums[tail] + nums[head]

                if current_sum == target:
                    threeSums.append([x, nums[tail], nums[head]])

                    # Überspringe alle gleichen Werte für tail und head
                    while tail < head and nums[tail] == nums[tail + 1]:
                        tail += 1
                    while tail < head and nums[head] == nums[head - 1]:
                        head -= 1

                    tail += 1
                    head -= 1

                elif current_sum < target:
                    tail += 1
                else:
                    head -= 1

        return threeSums
