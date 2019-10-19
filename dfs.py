N = int(input())
adjList = [[] for i in range(N)]
visited = [False for i in range(N)]

def dfs(start):
    if not visited[start]:
        print(start, end = ' ')
        visited[start] = True

    for i in range(len(adjList[start])):
        if not visited[adjList[start][i]]:
            visited[adjList[start][i]] = True
            print(adjList[start][i], end = ' ')
            dfs(adjList[start][i])

for n in range(N):
        adjList[n] = list(map(int, input().split()))
dfs(0)
print("Hacktober Fest")
