#!/usr/bin/env python2

instructions = {
    "0000 0000": "NOP",
    "0000 0001": "CALL",
    "0000 0010": "RET",
    "0000 0011": "OUT",
    "0000 0101": "HLT",

    "0001 1000": "JMP",
    "0001 1001": "JZ",
    "0001 1010": "JNZ",
    "0001 1100": "JE",
    "0001 1101": "JNE",

    "0100 0000": "ADD",
    "0100 1000": "SUB",
    "0101 0000": "INC",
    "0101 1000": "DEC"
}

regs = {
    "000": "A",
    "001": "B",
    "010": "C",
    "011": "D",
    "100": "E",
    "101": "F",
    "110": "G"
}

for k, v in regs.items():
    instructions["0001 0" + k] = "LDI " + v

for k1, v1 in regs.items():
    for k2, v2 in regs.items():
        if k1 == k2:
            txt = "invalid"
        else:
            txt = " ".join((v1, v2))

        instructions[" ".join(("10", k1, k2))] = "MOV " + txt


for k, v in regs.items():
    instructions["10 111 %s" % k] = "MOV M %s" % v
    instructions["10 %s 111" % k] = "MOV %s M" % v

for k, v in instructions.items():
    print k.replace(" ", ""), v