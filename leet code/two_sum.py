class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ret = []
        
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x != y and nums[x] + nums[y] == target:
                    ret.append(x)
                    ret.append(y)
                    break
            if ret:
                break
        
        return ret
        