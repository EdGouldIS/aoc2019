import time
start = time.time()

def main(puzzle_input):
    memory = [int(_) for _ in puzzle_input.split(',')]
    memory[1] = 12
    memory[2] = 2

    for i in range(0, len(memory), 4):
        operation = memory[i]
        if (operation == 1):
            memory[memory[i+3]] = memory[memory[i+1]] + memory[memory[i+2]]
        
        elif (operation == 2):
            memory[memory[i+3]] = memory[memory[i+1]] * memory[memory[i+2]]

        else:
            return memory[0]

    return memory[0]


def get_input(filename):
    with open(filename) as f:
        return f.read()


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    main(puzzle_input)
    print(time.time() - start)