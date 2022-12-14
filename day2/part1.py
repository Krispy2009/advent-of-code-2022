# A X Rock
# B Y Paper
# C Z Scissors

#  winning moves
wins ={'A': 'Z', 'C': 'Y', 'B': 'X', 'X': 'C', 'Z':'B', 'Y': 'A' }
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
    player1 = pair[0]
    player2 = pair[1]

    score = scores[player2]

    if draw[player1] == player2:
        # draw
        score += 3
    elif wins[player2]  == player1:
        # I win
        score += 6
    
    return score

if __name__ == '__main__':
    score = 0
    strategy = read_stategy_guide('input.txt')
    for pair in strategy:
        score += play_round(pair)
    print(f"Total: {score}")