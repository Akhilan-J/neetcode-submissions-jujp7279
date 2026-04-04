class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        if we take x we have to go until all the chars of that x are taken
        on the way if we see any other char we will have to apply the same ofr that also 
        that is why if we take x we have to go till index 4 but we fo an extra one so that
        so i was thinking of something like a hashmap that tracks first and last index of a number and then 
        we fo to x see that x ends at 4 get all of the letters between 0 and 4 and then do the same for all of them 
        and then we can find a substring and then do it till the last index
        '''
        last = defaultdict(int)
        for i,val in enumerate(s):
            last[val] = i
        res = []
        i = 0
        start = 0
        end = last[s[i]]
        while i < len(s):
            end = max(last[s[i]],end)
            if i == end:
                print(start,end)
                res.append(end + 1 - start)
                start = end + 1
                print(start)
                end = float("-inf")
            i += 1         
        return res