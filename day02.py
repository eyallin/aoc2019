
# opcodes
ADD, MULT, HALT = 1, 2, 99

def run_program(prog):
    ip = 0
    while True:
        op = prog[ip]
        if op in (ADD, MULT):
            operand1 = prog[prog[ip+1]]
            operand2 = prog[prog[ip+2]]

            if op == ADD:
                result = operand1 + operand2
            else:
                result = operand1 * operand2
            
            prog[prog[ip+3]] = result
            ip += 4
        elif op == HALT:
            return prog[0]
        else:
            raise RuntimeError(f'Unknown opcode {op} at position {ip}')


def test_run_program():
    assert(run_program([1,9,10,3,2,3,11,0,99,30,40,50]) == 3500)
    assert(run_program([1,1,1,4,99,5,6,0,99]) == 30)


if __name__ == "__main__":
    with open('day02_input.txt') as f:
        program = [int(a) for a in f.read().split(',')]
    
    program[1] = 12
    program[2] = 2
    run_program(program)
    print(f'The value at position 0 is {program[0]}')


def determine_values(initial_program, required_result):
    for noun in range(100):
        for verb in range(100):
            program = initial_program[:]
            program[1] = noun
            program[2] = verb
            result = run_program(program)
            if result == required_result:
                return noun, verb
    else:
        raise Exception('Could not find noun and verb')


if __name__ == "__main__":
    with open('day02_input.txt') as f:
        initial_program = [int(a) for a in f.read().split(',')]
    noun, verb = determine_values(initial_program, 19690720)
    print(f'Noun and verb are {noun} and {verb} ({100 * noun + verb})')