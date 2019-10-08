import sys
def addToOpcode(instruction,address,assemblyToOpcode,memory):
    opcodeTableValue = ["null","null","null","null","null"]
    if (instruction[0] == "STP" or instruction[0] == "CLA"):
        try:
            x = instruction[1]
            joined_string = ' '.join([str(v) for v in instruction])
            print("Error: Too many arguments in the instruction- "+ joined_string)
            sys.exit()
        except IndexError:
            pass
        opcodeTableValue[0] = instruction[0]
        opcodeTableValue[4] = assemblyToOpcode[instruction[0]]
        return opcodeTableValue
    elif (instruction[0] == "LAC" or instruction[0] == "SAC" or instruction[0] == "ADD" or instruction[0] == "SUB" or instruction[0] =="INP" or instruction[0] =="DSP" or instruction[0] =="MUL" or instruction[0] =="BRZ" or instruction[0] =="BRP" or instruction[0] =="BRN"):
        if (len(instruction)<2):
            joined_string = ' '.join([str(v) for v in instruction])
            print("Error: Less arguments in the instruction- "+joined_string)
            sys.exit()
        try:
            x = instruction[2]
            joined_string = ' '.join([str(v) for v in instruction])
            print("Error: Too many arguments in the instruction- "+ joined_string)
            sys.exit()
        except IndexError:
            pass

        opcodeTableValue[0] = instruction[0]
        opcodeTableValue[4] = assemblyToOpcode[instruction[0]]
        if (instruction[0] =="BRZ" or instruction[0] =="BRP" or instruction[0] =="BRN"):
            if instruction[1].isdigit():
                if memory[instruction[1]]=="nullValue":
                    print("Error:memory address "+str(instruction[1])+ " is empty")  
                    sys.exit()
            opcodeTableValue[1] = instruction[1]
            return opcodeTableValue
        elif (instruction[1][0]=="'" or instruction[1][0]=='"'):
            try:
                const=int(instruction[1][1:-1])
                memLoc=32767-const
                opcodeTableValue[1]=memLoc
                return opcodeTableValue
            except:
                print("Error:Wrong constant format")
                sys.exit()
        else:
            if (instruction[1].isdigit()):
                if int(instruction[1]) <= 28671:
                    if instruction[0]=="INP" or instruction[0]=="SAC":
                        if memory[instruction[1]]!="nullValue":
                            print("Error:memory address "+str(instruction[1])+ " is used")
                            sys.exit() 
                    else:
                        if memory[instruction[1]]=="nullValue":
                            print("Error:memory address "+str(instruction[1])+ " is empty")
                            sys.exit()
                    opcodeTableValue[1] = instruction[1]   
                    return opcodeTableValue
                else:
                    print("Memory address "+ instruction[1]+" not available. Memory address cannot exceed 28671")
                    sys.exit()
            else:
                print("Instruction format error: "+ instruction[1]+" is not a valid memory address.")
                sys.exit()
    elif (instruction[0]=="DIV"):
        if (len(instruction)<4):
            joined_string = ' '.join([str(v) for v in instruction])
            print("Error: Less arguments in the instruction- "+joined_string)
            sys.exit()
        try:
            x = instruction[4]
            joined_string = ' '.join([str(v) for v in instruction])
            print("Error: Too many arguments in the instruction- "+ joined_string)
            sys.exit()
        except IndexError:
            pass
        opcodeTableValue[0] = instruction[0]
        opcodeTableValue[4] = assemblyToOpcode[instruction[0]]
        for i in range(1,4):
            if (instruction[i].isdigit()):
                if int(instruction[i]) <= 28671:
                    if i==1:
                        if memory[instruction[i]]=="nullValue":
                            print("Error:memory address " +str(instruction[i])+" is empty")
                            sys.exit()
                    else:
                        if memory[instruction[i]]!="nullValue":
                            print("Error:memory address "+str(instruction[i])+ " is already in use")
                            sys.exit()
                    opcodeTableValue[i] = instruction[i]                    
                else:
                    print("Memory address "+ instruction[i]+" not available. Memory address cannot exceed 28671")
                    sys.exit()
            elif (instruction[i][0]=="'" or instruction[i][0]=='"'):
                if i==1:
                    try:
                        const=int(instruction[i][1:-1])
                        memLoc=32767-const
                        opcodeTableValue[i]=memLoc
                    except:
                        print("Error:Wrong constant format")
                        sys.exit()
                else:
                    print("Error: constant passed where memory address required") 
                    sys.exit()       
            else:
                print("Instruction format error: "+ instruction[i]+" is not a valid memory address.")
                sys.exit()
        return opcodeTableValue        

    else:
        print("Not a valid instruction.")
        sys.exit()




def firstPass(inpt,memory):
    symbolTable = {}
    opcodeTable= {}
    literalTable = {}
    unattendedLabels = {}
    for i in range(len(inpt)):
        instruction = inpt[i]
        if (len(instruction)>=3):
            if (instruction[0]!="DIV"):
                symbolTable[instruction[0]]=i
                # if instruction[1] == "STP" or instruction[1] == "CLA":
                #     opcodeTable[i] = ("STP")
                #     pass
                # elif symbolTable



if __name__ == "__main__":
    assemblyToOpcode = {"CLA":"0000","LAC":"0001","SAC": "0010","ADD":"0011","SUB":"0100", "BRZ":"0101","BRN":"0110","BRP":"0111","INP":"1000","DSP":"1001","MUL":"1010","DIV":"1011","STP":"1100"}
    memory = {}
    for i in range(32768):
        # print(int(str(bin(i+1))[2:]))
        if (i>28671):
            memory[str(i)] = 32767-i
        else:
            memory[str(i)] = "nullValue"
    # print(assemblyToOpcode)
    print("Make sure that the input file is in the same directory as the Assemblr.py file")
    print("Enter the name for the input file.")
    name = input()     
    f = open(name, "r")
    l = []
    for x in f:
        l.append(x.split())
    print(l)
    # for i in l: