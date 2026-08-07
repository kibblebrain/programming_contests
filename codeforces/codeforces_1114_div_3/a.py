for _ in range(int(input())):
    # A game with tokens.
    # Each round, before the beginning they check:
    # If any two players have the same number of tokens, the game ends
    # Otherwise, the player with the most tokens gives 1 token to the player with the least tokens.
    # Determine the number of rounds before the game ends.

    players = sorted(list(map(int, input().split())))

    # The middle player will never give a token away.
    # Thus the number of rounds is the minimum difference between either the most token player or the least token player from the middle token player.
    
    print(min(players[1]-players[0], players[2]-players[1]))
