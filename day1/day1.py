
supplies = []

with open('input.txt') as f:
    elf = []
    for line in f.readlines():
        line = line.strip()
        if line == '':
            supplies.append(elf)
            elf = []
            continue
        elf.append(int(line))

calories = sorted([sum(elf) for elf in supplies], reverse=True)
print(f"Part 1: {calories[0]}")
print(f"Part 2: {sum(calories[:3])}")

