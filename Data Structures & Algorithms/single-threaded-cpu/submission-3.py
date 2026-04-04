class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        for i in range(len(tasks)):
            tasks[i] = tasks[i] + [i]
        print(tasks)
        tasks.sort()
        res = []
        time = tasks[0][0]
        i = 0
        while i < len(tasks) or heap:
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap,tasks[i][1:])
                i += 1
            if not heap:
                time = tasks[i][0]
            else:
                curr = heapq.heappop(heap)
                time += curr[0]
                res.append(curr[1])
        return res
        