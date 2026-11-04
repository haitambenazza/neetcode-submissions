class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result: list[int] = []
        prefix:int = []
        total_prefix = 1
        for n  in range(len(nums) - 1, 0, -1):
            total_prefix *= nums[n]
            prefix.append(total_prefix)
        prefix.insert(0, 1)
        prefix.reverse()

        total = 1
        suffix:int = []
        for n in range(0, len(nums) - 1):
            total *= nums[n]
            suffix.append(total)
        suffix.insert(0, 1)
        result = [suffix[n] * prefix[n] for n in range(0, len(suffix))]
        return (result)