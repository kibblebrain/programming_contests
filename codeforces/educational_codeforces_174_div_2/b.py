for _ in range(int(input())):
    n,m = map(int,input().split())
    g = [list(map(int,input().split())) for i in range(n)]
    freq = [0]*(n*m+1)
    done = [False]*(n*m+1)
    ans = 0
    for i in range(n):
        for j in range(m):
            freq[g[i][j]] = 1
            if i and g[i-1][j] == g[i][j] and not done[g[i][j]]:
                done[g[i][j]] = True
                ans += 1
            if j and g[i][j-1] == g[i][j] and not done[g[i][j]]:
                done[g[i][j]] = True
                ans += 1
    ans += sum(freq)-1
    if True in done:
        ans -= 1
    print(ans)
