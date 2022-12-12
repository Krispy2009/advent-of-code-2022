MONKEYS = []
import math

class Monkey:
   
    def __init__(self, id=None, items=None, operation=None, test=None, t_monkey=None, f_monkey=None):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.t_monkey = t_monkey
        self.f_monkey = f_monkey
        self.result = None
        self.inspect_count = 0
        self.worry_modulo = 1
    
    def apply_operation(self, item):
        operation = self.operation.replace('old', str(item))
        result = eval(operation)
        result %= self.worry_modulo
        self.result = math.floor(result)

    def do_test(self):
        item = self.result
        if item % self.test == 0:
            MONKEYS[self.t_monkey].items.append(item)
        else:
            MONKEYS[self.f_monkey].items.append(item)

    def inspect_item(self):
        self.inspect_count += 1
        return self.items.pop(0)

    def __repr__(self):
        return f"""Monkey {self.id}
            Items: {self.items}
            Operation: {self.operation}
            Test: / {self.test}
                T: throw to {self.t_monkey}
                F: throw to {self.f_monkey}

            Worry Modulo: {self.worry_modulo}
        """

def read_input(filename):
    with open(filename) as f:
        for line in f.readlines():
            if line.startswith("Monkey"):
                params = {}
                params['id'] = int(line[:len(line)-2].split()[1])
            elif line.startswith('  Starting'):
                line = line.split(': ')[1]
                params['items'] = [int(i) for i in line.split(', ')]
            elif line.startswith('  Operation'):
                line = line.split(': ')[1].strip()
                params['operation'] = line.replace('new = ', '')
            elif line.startswith('  Test'):
                params['test'] = int(line.strip().split('by ')[1])
            elif line.startswith('    If true'):
                params['t_monkey'] = int(line.strip()[-1])
            elif line.startswith('    If false'):
                params['f_monkey'] = int(line.strip()[-1])
                MONKEYS.append(Monkey(**params))
            
    
               

def play_round():
    for monkey in MONKEYS:
        while len(monkey.items) > 0:
            item = monkey.inspect_item()
            monkey.apply_operation(item)
            monkey.do_test()


read_input('input.txt')

all_worry = 1
for monkey in MONKEYS:
    all_worry *= monkey.test
for monkey in MONKEYS:
    monkey.worry_modulo = all_worry


for i in range(10000):
    play_round()

inspect_counts = []
for monkey in MONKEYS:
    inspect_counts.append(monkey.inspect_count)
inspect_counts = sorted(inspect_counts, reverse=True)
print(f"{inspect_counts[0]} * {inspect_counts[1]}")
print(f"Monkey business: {math.prod(inspect_counts[:2])}")


print(MONKEYS)

