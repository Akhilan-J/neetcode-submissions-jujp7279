import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        heap = []
        for key ,val in freq.items():
            heapq.heappush(heap,(-val,key))
        builder = []
        prev = None
        while heap:
            val,key = heapq.heappop(heap)
            builder.append(key)
            if len(builder) < 1 and builder[-1] == builder[-2]:
                return ""
            val += 1
            if prev:
                heapq.heappush(heap,prev)
            if val == 0:
                prev = None
            else:
                prev = (val,key)
        print(prev)
        return "".join(builder) if not prev else ""
            

