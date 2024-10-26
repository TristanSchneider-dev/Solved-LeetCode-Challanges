class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sumEqualsZero = []
        nums.sort()
        
        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            for y in range(x + 1, len(nums)):
                if y > x + 1 and nums[y] == nums[y - 1]:
                    continue
                for z in range(y + 1, len(nums)):
                    if z > y + 1 and nums[z] == nums[z - 1]:
                        continue
                    if nums[x] + nums[y] + nums[z] == 0:
                        sumEqualsZero.append([nums[x], nums[y], nums[z]])
        
        return sumEqualsZero
