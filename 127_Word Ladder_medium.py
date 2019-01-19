先建立一个图G，然后用BFS去找到目标的宽度即可
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def graph(wordlist):
            graph = dict()
            for word in wordlist:
                for i in range(len(word)):
                    s = word[:i] + '_' + word[(i+1):]
                    graph[s] = graph.get(s,[]) + [word]
            return graph
        #print(graph(wordList))
        if endWord not in wordList:
            return 0
        queue = [beginWord]
        visited = set()
        iteration = 0
        G = graph(wordList)
        #print(G)
        now_cnt = 1
        next_cnt = 0
        while queue:  
            tmp = queue.pop(0)
            now_cnt -= 1
            if tmp == endWord:return iteration + 1
            if now_cnt == 0:iteration += 1

            for i in range(len(tmp)):
                s = tmp[:i] + '_' +tmp[(i+1):]
                if G.get(s,0):
                    temp_G = G[s]
                else:
                    temp_G = []
                check = []
                for word in temp_G:
                    if word not in visited:
                        check.append(word)
                        visited.add(word)
                queue += check
                next_cnt += len(check)
            if now_cnt == 0:
                now_cnt = next_cnt
                next_cnt = 0
            #queue += ['#']
        return 0

        
        
