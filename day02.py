
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