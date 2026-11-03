class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapped:dict[str, int] = {}
        for n in nums:
            key:str = str(n)
            if key in mapped:
                mapped[key] += 1
            else:
                mapped[key] = 1
        max_number = list(mapped)[0]
        result:list[str] = sorted(mapped, key=mapped.get, reverse=True)
        return result[0:k]