input_file = open("p3_group_9_p1_mc.txt","r")

print("ECE366 Fall 2018 - Project 3 - Group 9 Python Simulator")
print()

def simulate(I,NSteps):
    PC = 0
    DIC = 0
    Reg = [0,0,0,0]
    Memory = [0 for i in range(10)]

    print("###### Start of Simulation ######")

    finished = False
    while(not(finished)):
        fetch = I[PC]
        DIC += 1
        print(fetch)
        if (line[1:8] == "1111100"):
            result = Reg[2] ^ Reg[1]    #XorR2R1: R2 = R2 XOR R1
            Reg[2] = result
            PC += 1

    elif (line[1:8] == "1111101"):
        output_file.write("AndR3                // R3 AND 1 \n")

    elif (line[1:8] == "1111001"):
        output_file.write("ShiftR               // R2 >> \n")

    elif (line[1:8] == "1111000"):
        output_file.write("ShiftL               // R2 << \n")

    elif (line[1:5] == "1110"):
        register = str(int(line[5:7],2))
        immediate = str(int(line[7],2))
        output_file.write("Init R" + register + ", " + immediate)
        output_file.write("         // R" + register + " = " + immediate + "\n")

    elif (line[1:4] == "110"):
        register1 = str(int(line[4:6],2))
        register2 = str(int(line[6:8],2))
        output_file.write("SltR1 R" + register1 + ", R" + register2)
        output_file.write("         // if R" + register1 + " < R" + register2 + ", R1 = 1 \n")

    elif (line[1:4] == "011"):
        register1 = str(int(line[4:6],2))
        register2 = str(int(line[6:8],2))
        output_file.write("Store R" + register1 + ", (R" + register2 + ")")
        output_file.write("         // M[R" + register2 + "] <- R" + register1 + "\n")

    elif (line[1:4] == "010"):
        Rx = (int(line[4:6],2))
        Ry = (int(line[6:8],2))
        output_file.write("Load R" + register1 + ", (R" + register2 + ")")
        output_file.write("         // R" + register1 + " <- M[R" + register2 + "] \n")

    elif (line[1:4] == "001"):          #Rx = Rx - Ry
        Rx = (int(line[3:4],2)
        Ry = (int(line[5:6],2)

        Rx = Rx - Ry
        
    elif (fetch[1:4] == "000"):         #Rx = Rx + Ry
        Rx = int(line[3:4], 2)
        Ry = int(line[5:6], 2)
        
        Rx = Rx + Ry

    elif (fetch[1:6] == "10000"):       #PC -= Rx
        Rx = int(line[5:7], 2)
        PC = PC - Rx

    elif (fetch[1:6] == "10100"):       #If R1==0, PC += Rx
        Rx = int(line[5:7],2)
        if (Reg[1] == 0):
            PC = PC + Rx
        else:
            PC = PC + 1
            
            
        
        
        register = str(int(line[6:8], 2))
        output_file.write("bezR1, R" + register)
        output_file.write("         // if R1 ==0: PC = PC + R" + register + " | else: PC++ \n")
