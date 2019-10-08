def addToOpcode(instruction,address,assemblyToOpcode):
    opcodeTableValue = ["null","null","null","null","null"]
    if (instruction[0] == "STP" or instruction[0] == "CLA"):
        try:
            x = instruction[1]
            joined_string = ' '.join([str(v) for v in instruction])
            print("Error: Too many arguments in the instruction- "+ joined_string)
        except IndexError:
            pass
        opcodeTableValue[0] = instruction[0]
        opcodeTableValue[4] = assemblyToOpcode[instruction[0]]
        return opcodeTableValue
    elif (instruction[0] == "LAC" or instruction[0] == "SAC" or instruction[0] == "ADD" or instruction[0] == "SUB" or instruction[0] =="INP" or instruction[0] =="DSP" or instruction[0] =="MUL" or instruction[0] =="BRZ" or instruction[0] =="BRP" or instruction[0] =="BRN"):
        if (len(instruction)<2):
            joined_string = ' '.join([str(v) for v in instruction])
            print("Error: Less arguments in the instruction- "+joined_string)
        try:
            x = instruction[2]
            joined_string = ' '.join([str(v) for v in instruction])
            print("Error: Too many arguments in the instruction- "+ joined_string)
        except IndexError:
            pass

        opcodeTableValue[0] = instruction[0]
        opcodeTableValue[4] = assemblyToOpcode[instruction[0]]
        if (instruction[0] =="BRZ" or instruction[0] =="BRP" or instruction[0] =="BRN"):
            opcodeTableValue[1] = instruction[1]
            return opcodeTableValue
        elif (instruction[1][0]=="'" or instruction[1][0]=='"'):
            const=int(instruction[1][1:-1])


        else:
            if (instruction[1].isdigit()):
                if int(instruction[1]) <= 28671:
                    opcodeTableValue[1] = instruction[1]
                else:
                    print("Memory address "+ instruction[1]+" not available. Memory address cannot exceed 28671")
            else:
                print("Instruction format error: "+ instruction[1]+" is not a valid memory address.")

    elif (instruction[0]=="DIV"):
        if (len(instruction)<4):
            joined_string = ' '.join([str(v) for v in instruction])
            print("Error: Less arguments in the instruction- "+joined_string)
        try:
            x = instruction[4]
            joined_string = ' '.join([str(v) for v in instruction])
            print("Error: Too many arguments in the instruction- "+ joined_string)
        except IndexError:
            pass
        opcodeTableValue[0] = instruction[0]
        opcodeTableValue[4] = assemblyToOpcode[instruction[0]]
        if (instruction[1].isdigit()):
            if int(instruction[1]) <= 28671:
                opcodeTableValue[1] = instruction[1]
            else:
                print("Memory address "+ instruction[1]+" not available. Memory address cannot exceed 28671")
        else:
            print("Instruction format error: "+ instruction[1]+" is not a valid memory address.")

    else:
        print("Not a valid instruction.")