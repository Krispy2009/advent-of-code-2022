def read_input(filename):
    pairs = []
    with open(filename) as f:
        for line in f.readlines():
            pair = line.strip().replace('-',',').split(',')
            pair = [int(p) for p in pair]
            pairs.append(((pair[0],pair[1]),(pair[2],pair[3])))
    return pairs

def find_overlap(pair):
    left, right = pair

    left = set(range(left[0], left[1]+1))
    right = set(range(right[0], right[1]+1))

    if left.intersection(right):
        return 1
    return 0        

if __name__ == '__main__':
    overlaps = 0
    pairs = read_input('input.txt')
    for pair in pairs:
       overlaps += find_overlap(pair)

    print(overlaps)