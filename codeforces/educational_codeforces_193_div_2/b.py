for _ in range(int(input())):
    # n signals of color a[i]
    n = int(input())
    a = list(map(int, input().split()))

    # do not allow two adjacent modules of the same color.
    # you can remove any number of modules and can swap two adjacent modules at most once, after which you cannot do anything else.
    # determine the number of modules that can be kept.

    # since you can only swap once, assume you should delete any adjacent modules for all other operations.
    
    max_swap_reduction = 1
    max_swap_index = -1
    for i in range(n-1):
        if a[i] != a[i+1]:
            swap_reduction = 0
            if i-1 >= 0:
                swap_reduction -= int(a[i] != a[i-1])
                swap_reduction += int(a[i-1] != a[i+1])
            if i+2 < n:
                swap_reduction -= int(a[i+1] != a[i+2])
                swap_reduction += int(a[i] != a[i+2])
            if swap_reduction >= max_swap_reduction:
                max_swap_reduction = swap_reduction
                max_swap_index = i
    if max_swap_index != -1:
        tmp = a[max_swap_index]
        a[max_swap_index] = a[max_swap_index+1]
        a[max_swap_index+1] = tmp
    # Count the number of adjacents by traversing.
    cnt = 1
    for i in range(n-1):
        if a[i] != a[i+1]:
            cnt += 1
    print(cnt)
    
