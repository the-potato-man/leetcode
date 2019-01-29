'''
In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  
If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  
More specifically, there exists a natural number K so that for any choice of where to walk,
 we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  
The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
'''

class Solution(object):
#     def eventualSafeNodes(self, graph):
#         """
#         :type graph: List[List[int]]
#         :rtype: List[int]
#         """
#         n = len(graph)
        
#         self.hasCycle = False

#         def helper(i, graph, visited, cycleStack):
#             if self.hasCycle == True: return # end search early
#             if i in sol: return # end search early
#             visited[i] = True
#             cycleStack[i] = True
#             for neigh in graph[i]:
#                 if neigh in sol: continue # end search early
#                 if neigh not in visited:
#                     helper(neigh, graph, visited, cycleStack)
#                 elif cycleStack[neigh]:
#                     self.hasCycle = True
#             cycleStack[i] = False
        
#         sol = []
#         for i in range(n):
#             visited = {}
#             cycleStack = {}
#             helper(i, graph, visited, cycleStack)
#             if self.hasCycle == False:
#                 sol.append(i)
#             self.hasCycle = False
        
#         return sol

    def eventualSafeNodes(self, graph):        
            def dfs(graph, i, visited):                                         
                for j in graph[i]:
                    if j in visited: return False
                    if j in ans: continue # end early
                    visited.add(j)                
                    if not dfs(graph, j, visited): return False
                    visited.remove(j)                                                                            
                ans.add(i)     
                return True                        
            ans = set()
            for i in range(len(graph)):            
                visited = set([i])
                dfs(graph, i, visited)        
            return sorted(list(ans))

