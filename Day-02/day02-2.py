def main(puzzle_input):
    memory = [int(_) for _ in puzzle_input.split(',')]
    for noun in range(100):
        for verb in range(100):
            if run_program(memory[:], noun, verb) == 19690720:
                return 100 * noun + verb


def run_program(memory, noun, verb):
    memory[1] = noun
    memory[2] = verb
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