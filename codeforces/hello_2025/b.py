from collections import Counter
for _ in range(int(input())):
    n,k = map(int,input().split())
    b = sorted(Counter(input().split()).values())
    m = len(b)
    for i in b:
        if (i > k):
            break
        k -= i
        m -= 1
    
    print(max(m,1))
