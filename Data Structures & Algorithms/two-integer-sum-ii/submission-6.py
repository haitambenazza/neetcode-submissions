class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end:int = len(numbers)
        start = 0
        while start < end:
            if numbers[end - 1] + numbers[start] == target:
                return [start + 1, end ]
            elif numbers[end - 1] + numbers[start] < target:
                start += 1
            elif numbers[end - 1] + numbers[start] > target:
                end -= 1
        return []   