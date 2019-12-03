def process_opcodes(opcodes):
    for opcode in range(0, len(opcodes), 4):
        if opcodes[opcode] == 1:
            opcodes[opcodes[opcode+3]] = opcodes[opcodes[opcode+1]] + opcodes[opcodes[opcode+2]]
        elif opcodes[opcode] == 2:
            opcodes[opcodes[opcode + 3]] = opcodes[opcodes[opcode + 1]] * opcodes[opcodes[opcode + 2]]
        elif opcodes[opcode] == 99:
            return opcodes
        else:
            print("Something went terribly wrong, exiting...")
            return -1


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read().split(',')

    input = list(map(int, input))
    input[1] = 12
    input[2] = 2

    print(process_opcodes(input))