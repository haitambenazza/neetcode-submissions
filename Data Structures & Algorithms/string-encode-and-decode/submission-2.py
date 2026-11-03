class Solution:
    key: list[str] = []
    def encode(self, strs: List[str]) -> str:
        encoded:str = ""
        Solution.key = strs.copy()
        encoded.join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        Solution.value = s
        return Solution.key