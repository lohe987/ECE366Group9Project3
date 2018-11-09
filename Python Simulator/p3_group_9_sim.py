print("ECE366 Fall 2018 - Project 3 - Group 9 Python Simulator")
print()

def simulate(I,M):
    PC = 0
    DIC = 0
    Reg = [0,0,0,0]
    Memory = M

    print("###### Start of Simulation ######")

    finished = False
    while(not(finished)):
        fetch = I[PC]
        DIC += 1
        print(fetch)
        if (fetch[1:8] == "1111100"):
            result = Reg[2] ^ Reg[1]    #XorR2R1: R2 = R2 XOR R1
            Reg[2] = result
            PC += 1

        elif (fetch[1:8] == "1111101"):
            result = Reg[3] & 1     #AndR3: R3 = R3 AND 1
            Reg[3] = result
            PC += 1

        elif (fetch[1:8] == "1111001"):
            Reg[2] = Reg[2] >> 1     #ShiftR: R2 >>
            PC += 1

        elif (fetch[1:8] == "1111000"):
            Reg[2] = Reg[2] << 1  #ShiftL: R2 <<
            PC += 1

        elif (fetch[1:5] == "1110"):
            Rx = int(fetch[5:7],2)
            imm = int(fetch[7],2)
            Reg[Rx] = imm       #Init: Rx = imm
            PC += 1

        elif (fetch[1:4] == "110"):
            Rx = int(fetch[4:6],2)
            Ry = int(fetch[6:8],2)
            if(Reg[Rx] < Reg[Ry]):
                Reg[1] = 1      #SltR1: if Rx < Ry, R1 = 1
                PC += 1
            else:
                PC +=1

        elif (fetch[1:4] == "011"):
            Rx = int(fetch[4:6],2)
            Ry = int(fetch[6:8],2)
            Memory[Reg[Ry]] = Reg[Rx]   #Store: M[Ry] <- Rx
            PC += 1

        elif (fetch[1:4] == "010"):
            Rx = int(fetch[4:6], 2)
            Ry = int(fetch[6:8], 2)
            Reg[Rx] = Memory[Reg[Ry]]  # Load: M[Ry] -> Rx
            PC += 1

        elif (fetch[1:4] == "001"):  # Rx = Rx - Ry
            Rx = int(fetch[4:6], 2)
            Ry = int(fetch[6:8], 2)
            Reg[Rx] = Reg[Rx] - Reg[Ry]
            PC += 1

        elif (fetch[1:4] == "000"):  # Rx = Rx + Ry
            Rx = int(fetch[4:6], 2)
            Ry = int(fetch[6:8], 2)
            Reg[Rx] = Reg[Rx] + Reg[Ry]
            PC += 1

        elif (fetch[1:6] == "10000"):  # PC -= Rx
            Rx = int(fetch[6:8], 2)
            PC = PC - Reg[Rx]

        elif (fetch[1:6] == "10100"):  # If R1==1, PC += Rx
            Rx = int(fetch[6:8], 2)
            if (Reg[1] == 1):
                PC = PC + Reg[Rx]
            else:
                PC += 1

        elif (fetch[0] == "/"):
            PC += 1
        elif (fetch[1:8]=="1111111"):
            finished = True
        else:
            finished = True

    print("******** Simulation finished *********")
    print("Dynamic Instr Count: ", DIC)
    print("Registers R0-R3: ", Reg)
    print("Memory :", Memory)


def main():
    input_file = open("p3_group_9_p1_mc.txt", "r")
    input_pattern = open("patternC.txt", "r")
    Nlines = 0  # How many instrs total in input.txt
    Instruction = []  # all instructions will be stored here
    Memory = []

    for line in input_file:
        Instruction.append(line)  # Copy all instruction into a list
        Nlines += 1

    for line in input_pattern:
        if(line == "\n"):
            continue
        line = line.replace("\n","")
        Memory.append(int(line,2))

    simulate(Instruction,Memory)

if __name__ == "__main__":
    main()