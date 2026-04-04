class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        res = []

        for i in range(1,len(words)):
            prev = words[i-1]
            curr = words[i]
            if len(prev)>len(curr):
                n  = len(curr)
                tryy = prev[:n]
                if tryy == curr:
                    return ""
            for j in range(min(len(prev),len(curr))):
                print("we in this bih")
                if prev[j] != curr[j]:
                    graph[prev[j]].append(curr[j])
                    break
        print(graph)
        leaf = deque()
        other = defaultdict(int)
        temp = set()
        for i in words:
            for j in i:
                temp.add(j)
        print(graph)
        for key,val in graph.items():
            for i in val:
                other[i] += 1
        for i in temp:
            if i not in other:
                leaf.append(i)
        # if not graph :
        #     return ""
        while leaf:
            curr = leaf.popleft()
            res.append(curr)
            for child in graph[curr]:
                other[child] -= 1
                if other[child] == 0 :
                    leaf.append(child)
                    del other[child]
        if len(res) == len(temp):
            return "".join(res)
        else:
            return ""

        