#!/usr/local/bin/python3
from io import UnsupportedOperation

def load_program(filename):
    a_val, b_val, c_val = 0, 0, 0
    program = ""
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith("Register A"):
                a_val = int(line.split(":")[1])
            if line.startswith("Register B"):
                b_val = int(line.split(":")[1])
            if line.startswith("Register C"):
                c_val = int(line.split(":")[1])
            if line.startswith("Program:"):
                program = line.split(":")[1]
                program = [int(n) for n in program.split(",")]

    return Computer(
        a_val, b_val, c_val, program
    )


class Computer():
    OPCODES = {
        0: "adv",
        1: "bxl",
        2: "bst",
        3: "jnz",
        4: "bxc",
        5: "out",
        6: "bdv",
        7: "cdv"
    }

    def __init__(self, register_a, register_b, register_c, program):
        self.register_a = register_a
        self.register_b = register_b
        self.register_c = register_c
        self.program = program
        self.pc = 0
        self.output = []

    def __repr__(self):
        return f"Computer({self.register_a=}, {self.register_b=}, {self.register_c=}, {self.program}"

    def get_output(self):
        return ",".join(str(o) for o in self.output)

    def combo(self, operand):
        if operand in [0,1,2,3]:
            return operand
        if operand == 4:
            return self.register_a
        if operand == 5:
            return self.register_b
        if operand == 6:
            return self.register_c
        else:
            raise UnsupportedOperation(operand)

    def adv(self, operand):
        self.register_a = int(self.register_a / 2 ** self.combo(operand))
        self.pc += 2

    def bxl(self, operand):
        self.register_b = self.register_b ^ operand
        self.pc += 2

    def bst(self, operand):
        x = self.combo(operand)
        x = x % 8
        self.register_b = x
        self.pc += 2

    def jnz(self, operand):
        if self.register_a == 0:
            self.pc += 2
            return
        self.pc = operand

    def bxc(self, ignored=None):
        self.register_b = self.register_b ^ self.register_c
        self.pc += 2

    def out(self, operand):
        self.output.append(self.combo(operand) % 8)
        self.pc += 2

    def bdv(self, operand):
        self.register_b = int(self.register_a / 2 ** self.combo(operand))
        self.pc += 2

    def cdv(self, operand):
        self.register_c = int(self.register_a / 2 ** self.combo(operand))
        self.pc += 2

    def run(self):
        while True:
            if self.pc >= len(self.program):
                break

            opcode = self.program[self.pc]
            operand = self.program[self.pc+1]
            f = getattr(self, self.OPCODES[opcode])
            f(operand)


c = load_program("day17ex.txt")
c.run()
assert c.get_output() == "4,6,3,5,6,3,5,2,1,0"

c = load_program("day17.txt")
c.run()
assert c.get_output() == "2,7,2,5,1,2,7,3,7"
