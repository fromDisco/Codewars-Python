def rps(p1, p2):
    """ Rock Paper Scissors
    Let's play! You have to return which player won! In case of a draw return Draw!.
    """
    # Player one wins with these combinations, otherwise he loses
    oneWon = ('scissorspaper', 'paperrock', 'rockscissors')

    if p1 == p2:
        return "Draw!"

    # concatinate p1 and p2 and compare with the set()
    return "Player 1 won!" if (p1 + p2) in oneWon else "Player 2 won!"


print(rps('rock', 'scissors'))
print(rps('scissors', 'rock'))
print(rps('rock', 'rock'))

