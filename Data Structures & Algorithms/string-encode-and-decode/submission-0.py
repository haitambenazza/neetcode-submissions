class Solution:
    key: list[str] = []
    def encode(self, strs: List[str]) -> str:
        encoded:str = ""
        Solution.key = strs.copy()
        for string in strs:
            encoded.join(string)
        return encoded

    def decode(self, s: str) -> List[str]:

        return Solution.key