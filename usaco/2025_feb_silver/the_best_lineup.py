from bisect import bisect_right

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    def ls(arr):
        n = len(arr)
        stack = []
        
        for i in range(n - 1, -1, -1):  # Traverse the array from right to left
            if not stack or arr[i] >= stack[-1]:  
                stack.append(arr[i])  # Keep appending if it's greater or equal
        
        return stack[::-1]  # Reverse to maintain original order
    def lo(target):
        global a
        for i in range(len(a) - 1, -1, -1):  # Start from the end
            if a[i] == target:
                return i  # Return index of last occurrence
        return -1  # Return -1 if target is not found
    
    b = ls(a)
    d = b.copy()

    def move(i, j):
        global a
        global d
        c = a.copy()
        x = c[i]
        c.pop(i)
        c.insert(j,x)
        if ls(c) > d:
            d = ls(c)

    for i in range(len(b)):
        if i > 0:
            move(lo(b[i]), lo(b[i-1])+1)
        else:
            move(lo(b[i]), 0)
    
    print(*d)

