priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def make_compartments(filename):
#every 3 lines is one 

    compartments = []
    count = 0
    with open(filename) as f:
        group = []
        for line in f.readlines():
            if count < 3:
                line = line.strip()
                group.append(set(list(line)))
                count += 1
            else:
                compartments.append(group)
                group = []
                group.append(set(list(line.strip())))
                count = 1 
        compartments.append(group)
    return compartments

def find_common(group):
    one, two, three = group
    common = one.intersection(two).intersection(three).pop()
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
