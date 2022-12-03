priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def make_compartments(filename):
    compartments = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            half = int(len(line)/2)
            left, right = line[:half], line[half:]
            compartments.append((left, right))
    return compartments

def find_common(compartment):
    left, right = compartment
    left = set(list(left))
    right = set(list(right))
    common = left.intersection(right).pop()
    return common

def get_priority(letter):
    return priority.index(letter) + 1


if __name__ == '__main__':
    compartments = make_compartments('input.txt')

    priority_score = 0
    for c in compartments:
       common =  find_common(c)
       priority_score += get_priority(common)

    print(f"Priority: {priority_score}")
