class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        solution:List[int] = []
        hash_table: dict[int, int] = {}
        size = len(numbers)
        for i in range(0, size):
            hash_table[numbers[i]] = i
        print(hash_table)
        for i in range(0, size):
            found = hash_table.get(target - numbers[i], 'error')  
            if found != 'error':
                solution.append(i+1)
                solution.append(found+1)
                return solution
        return solution   