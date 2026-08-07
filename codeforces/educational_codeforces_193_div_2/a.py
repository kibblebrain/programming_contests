for _ in range(int(input())):
    n = int(input())
    # n cards with values 2..n+1
    # if one of the numbers x and y is divisible by the other, the card with smaller value wins.
    # otherwise the card with larger value wins
    # There can only be a sole winner if there is a card in 2 .. n+1 that is smaller than the others and divisible to every other card, or if there is a card larger than every other card that is not divisible by them.
    # In other words, only if the nth+1 card is prime.
    flag = True
    for i in range(2,n):
        if (n+1)%i == 0:
            flag = False
    print("YES" if flag else "NO")
