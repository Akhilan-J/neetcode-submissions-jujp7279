class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) #mapping charCount to the list of anagrams
        for s in strs: #individual string
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")]+=1

            res[tuple(count)].append(s)
        return res.values()