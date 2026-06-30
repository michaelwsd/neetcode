class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        
        words.add(beginWord)
        # construct graph
        graph = defaultdict(list)

        for word in words:
            for i in range(len(word)):
                sb = list(word)
                for j in range(26):
                    sb[i] = chr(ord('a') + j)
                    newStr = "".join(sb)
                    if newStr != word and newStr in words:
                        graph[word].append(newStr)
        
        heap = []
        heapq.heappush(heap, [1, beginWord])
        visited = set()
        visited.add(beginWord)

        while len(heap) > 0:
            step, word = heapq.heappop(heap)

            if word == endWord:
                return step
            
            for nei in graph[word]:
                if nei in visited:
                    continue
                visited.add(nei)
                heapq.heappush(heap, [step+1, nei])

        return 0


