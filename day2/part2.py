# A X Rock
# B Y Paper
# C Z Scissors

#  winning moves
wins ={'A': 'Z', 'C': 'Y', 'B': 'X', 'X': 'C', 'Z':'B', 'Y': 'A' }
loses = {v: k for k, v in wins.items()}
draw = {'A': 'X', "B": "Y", 'C': 'Z'}

scores = {'A': 1, 'X':1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3 }

def read_stategy_guide(filename):
    strategy = []
    with open(filename) as f:
        for line in f.readlines():
            if line.strip() != '':
                pair = tuple(line.strip().split())
                strategy.append(pair)

    return strategy

def play_round(pair):
    score = 0
    player1 = pair[0]
    outcome = pair[1]
    player2 = None

    if outcome == 'X':
        # I lose, player1 wins
        player2 = wins[player1]
    elif outcome == 'Y':
        # draw
        score += 3
        player2 = draw[player1]
    else:
        # I win, player1 loses
        score += 6
        player2 = loses[player1]

    # print(f"My choice ({player2}) score:  {scores[player2]}")
    score += scores[player2]
    return score

if __name__ == '__main__':
    score = 0
    strategy = read_stategy_guide('input.txt')
    for pair in strategy:
        score += play_round(pair)
    print(f"Total: {score}")