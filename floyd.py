n = int(input("Number of vertices: "))
m = [[int(x) for x in input().split()] for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if m[i][k] + m[k][j] < m[i][j]:
                m[i][j] = m[i][k] + m[k][j]

for i in m:
    print(*i)
