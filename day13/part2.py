import functools
from copy import deepcopy

def read_input(filename):
    packets = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            if not line == '':
                item = eval(line)
                packets.append(item)

    packets.extend([[[2]], [[6]]])
    return tuple(packets)
    


def compare(left_in, right_in):
    left = deepcopy(left_in)
    right = deepcopy(right_in)

    # print(f'Comparing {left} and       {right}')
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            # print("NOOO")
            return -1
        elif left < right:
            # print('YEY')
            return 1
        else:
            return 0

    elif isinstance(left, list) and isinstance(right, list):

        while left:
            # print(f"----> {left}, {right}")
            if right == []:
                # print("NOOO")
                return -1

            left_elem = left.pop(0)
            right_elem = right.pop(0)
            ans = compare(left_elem, right_elem)
            if ans != 0:
                return ans

        if left == [] and len(right) > 0:
            # print(f"----> {left}, {right}")
            # print("YEY")
            return 1

    elif isinstance(left, int) and isinstance(right, list):
        ans = compare([left], right)
        if ans != 0:
            return ans
    elif isinstance(left, list) and isinstance(right, int):
        ans = compare(left, [right])
        if ans != 0:
            return ans
                
    return 0


if __name__ == "__main__":

    packets = read_input('input.txt')

    results = sorted(packets, key=functools.cmp_to_key(compare), reverse=True)
    ans = 1
    for idx, item in enumerate(results):
        if item in [[[6]],[[2]]]:
            ans *= idx+1

    print("Ans: ", ans)


