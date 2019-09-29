def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_map = {}
        if len(nums) <= 1:
            return False
        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in freq_map.keys():
                print(i)
                print(nums[i])
                return [i,freq_map[nums[i]]]
            else:
                freq_map[complement] = i
            
        return []

nums = [2, 7, 11, 15]
target = 9
twoSum(nums,target)