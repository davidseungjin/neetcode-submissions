class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hmap = defaultdict(list)
        visited = [False] * n

        for u, v in edges:
            hmap[u].append(v)
            hmap[v].append(u)
        
        def dfs(node):
            for nei in hmap[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        
        def bfs(node):
            q = deque([node])
            visited[node] = True
            while q:
                cur = q.popleft()
                for nei in hmap[cur]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)
        
        res = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                # dfs(node)
                bfs(node)
                res += 1
        return res