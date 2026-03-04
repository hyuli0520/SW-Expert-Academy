from collections import defaultdict

T = int(input())

def dfs(start, g):
    visited[start] = True

    if visited[g]: return True

    for adj_v in graph[start]:
        if visited[adj_v]: continue
        res = dfs(adj_v, g)
        if res: return True
    
    return False


for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    graph = defaultdict(list)
    visited = [None] * (V + 1)
    for _ in range(E):
        start_v, end_v = map(int, input().split())
        graph[start_v].append(end_v)
    S, G = map(int, input().split())

    res = dfs(S, G)

    print(f"#{test_case} {int(res)}")
