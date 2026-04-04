class Solution:

    def encode(self, strs: List[str]) -> str:
        self.s=""
        for word in strs:
            for letter in word:
                self.s+=letter
            self.s+="|"
        return self.s
    def decode(self, s: str) -> List[str]:
        self.orig=[]
        prev=0
        for i in range(len(s)):
            if s[i]=="|":
                self.orig.append(s[prev:i])
                prev=i+1
        return self.orig