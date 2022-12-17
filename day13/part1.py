def read_input(filename):
    pairs = []
    with open(filename) as f:
        pair = []
        for line in f.readlines():
            line = line.strip()
            if line == '' and len(pair) == 2:
                pairs.append(pair)
                pair = []
            else:
                item = eval(line)
                pair.append(item)

    return pairs


def compare(left, right):

    print(f'Comparing {left} and       {right}')
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            print("NOOO")
            return False
        elif left < right:
            print('YEY')
            return True
        else:
            return None

    elif isinstance(left, list) and isinstance(right, list):

        while left:
            print(f"----> {left}, {right}")
            if right == []:
                print("NOOO")
                return False

            left_elem = left.pop(0)
            right_elem = right.pop(0)
            ans = compare(left_elem, right_elem)
            if ans is not None:
                return ans

        if left == [] and len(right) > 0:
            print(f"----> {left}, {right}")
            print("YEY")
            return True

    elif isinstance(left, int) and isinstance(right, list):
        ans = compare([left], right)
        if ans is not None:
            return ans
    elif isinstance(left, list) and isinstance(right, int):
        ans = compare(left, [right])
        if ans is not None:
            return ans
                

if __name__ == "__main__":

    pairs = read_input('input.txt')
    results = []
    for idx, pair in enumerate(pairs):
        print(f"=== Pair {idx+1} ===")
        left, right = pair
        res = compare(left, right)
        results.append((idx+1, res))
        print("==============")

    print(len([i for i in results if i[1] is not False]))

    print(f"Sum of idx: {sum([i[0] for i in results if i[1] is not False])}")