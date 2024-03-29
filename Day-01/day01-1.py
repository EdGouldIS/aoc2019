def main(puzzle_input):
    puzzle_input = puzzle_input.split()
    total = 0
    for mass in puzzle_input:
        total += int(mass) // 3 - 2

    return total


def get_input(filename):
    with open(filename) as f:
        return f.read()


if __name__ == '__main__':
    puzzle_input = get_input('input.txt') 
    main(puzzle_input)
