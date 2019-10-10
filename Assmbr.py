"""Name: Rachit Mittal (2018302)
   Name: Siddharth Sadhwani (2018313)"""
import sys
def addToOpcode(instruction,assemblyToOpcode,memory,literalTable):
    opcodeTableValue = ["null","null","null"]
    if (instruction[0] == "STP" or instruction[0] == "CLA"):
        try:
            x = instruction[1]
            joined_string = ' '.join([str(v) for v in instruction])
            print("Error: Too many arguments in the instruction- "+ joined_string)
            sys.exit()
        except IndexError:
            pass
        opcodeTableValue[0] = instruction[0]
        opcodeTableValue[2] = assemblyToOpcode[instruction[0]]
        opcLit = [opcodeTableValue,literalTable]
        return opcLit
    elif (instruction[0]=="DIV" or instruction[0] == "LAC" or instruction[0] == "SAC" or instruction[0] == "ADD" or instruction[0] == "SUB" or instruction[0] =="INP" or instruction[0] =="DSP" or instruction[0] =="MUL" or instruction[0] =="BRZ" or instruction[0] =="BRP" or instruction[0] =="BRN"):
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
        opcodeTableValue[2] = assemblyToOpcode[instruction[0]]
        if (instruction[0] =="BRZ" or instruction[0] =="BRP" or instruction[0] =="BRN"):
            if instruction[1].isdigit():
                if memory[instruction[1]]=="nullValue":
                    print("Error: Memory address "+str(instruction[1])+ " is empty")
                    sys.exit()
                else:
                    memory[instruction[1]] = "used"
            opcodeTableValue[1] = instruction[1]
            opcLit = [opcodeTableValue,literalTable]
            return opcLit
        elif (instruction[1][0]=="'" or instruction[1][0]=='"'):
            try:
                const=int(instruction[1][1:-1])
                if (const>4095):
                    print("Error: Constant cannot exceed 12 bits of data, ie 4095(decimal).")
                    sys.exit()
                memLoc=32767-const
                literalTable[const] = memLoc
                opcodeTableValue[1]=str(memLoc)
                opcLit = [opcodeTableValue,literalTable]
                return opcLit
            except:
                print("Error: Wrong constant format")
                sys.exit()
        else:
            if (instruction[1].isdigit()):
                if int(instruction[1]) <= 28671:
                    if instruction[0]=="INP" or instruction[0]=="SAC":
                        if memory[instruction[1]]!="nullValue":
                            print("Error: Memory address "+str(instruction[1])+ " is used")
                            sys.exit() 
                    else:
                        if memory[instruction[1]]=="nullValue":
                            print("Error: Memory address "+str(instruction[1])+ " is empty")
                            sys.exit()
                    opcodeTableValue[1] = instruction[1]
                    memory[instruction[1]] = "used"
                    opcLit = [opcodeTableValue,literalTable] 
                    return opcLit
                else:
                    print("Error: Memory address "+ instruction[1]+" not available. Memory address cannot exceed 28671")
                    sys.exit()
            elif(len(instruction[1])!=0 and not instruction[1][0].isdigit() and instruction[1].isalnum()):
                if(instruction[1] not in assemblyToOpcode.keys()):
                    opcodeTableValue[1] = instruction[1]
                    opcLit = [opcodeTableValue,literalTable]
                    return opcLit
                else :
                    print("Error: Opcodes cannot be used as variable names")          
            else:
                print("Error: Instruction format error: "+ instruction[1]+" is not a valid input format.")
                sys.exit()
    else:
        print("Not a valid instruction.")
        sys.exit()

def firstPass(inpt,memory,assemblyToOpcode):
    symbolTable = {}
    labelorvariableTable={}
    opcodeTable= {}
    literalTable = {}
    ans = []
    for i in range(len(inpt)):
        instruction = inpt[i]
        if (len(instruction)==3 and instruction[1]=="DW"):
            if (len(instruction)<3):
                joined_string = ' '.join([str(v) for v in instruction])
                print("Error: Less arguments in the instruction- "+joined_string)
                sys.exit()
            try:
                x = instruction[3]
                joined_string = ' '.join([str(v) for v in instruction])
                print("Error: Too many arguments in the instruction- "+ joined_string)
                sys.exit()
            except IndexError:
                pass
            if(instruction[0] not in symbolTable.keys()):
                if(len(instruction[0])!=0 and not instruction[0][0].isdigit() and instruction[0].isalnum()):
                    if(instruction[0] not in assemblyToOpcode.keys()):
                        #symbolTable[0] = instruction[0]
                        if (instruction[2][0]=="'" or instruction[2][0]=='"'):
                            try:
                                const=int(instruction[2][1:-1])
                                if (const>4095):
                                    print("Error: Constant cannot exceed 12 bits of data, ie 4095(decimal).")
                                    sys.exit()
                                memLoc=32767-const
                                #literalTable[const] = memLoc
                                symbolTable[instruction[0]]=str(memLoc)
                                labelorvariableTable[instruction[0]]="V"            #capital V
                                opcodeTable[i]=["DW",instruction[0],assemblyToOpcode["DW"]]    
                            except:
                                print("Error: Wrong constant format")
                                sys.exit()    
                        else:
                            print("Error: Wrong variable declared "+instruction[2]+" .Only constants are allowed.")        
                    else :
                        print("Error: Opcodes cannot be used as variable names: "+instruction[0])          
                else:
                    print("Error: Instruction format error: "+ instruction[1]+" is not a valid input format.")
                    sys.exit()
            else:
                print("Error: Variable: " +instruction[0]+ " already declared")        
        else:
            try:
                instructionName = assemblyToOpcode[instruction[0]]
                opcLit = addToOpcode(instruction,assemblyToOpcode,memory,literalTable)
                opcodeTable[i] = opcLit[0]
                literalTable = opcLit[1]
            except KeyError:
                if instruction[0][-1]!=":":
                    print("Error: "+instruction[0]+" is not a valid opcode.")
                    sys.exit()
                else:
                    try:
                        labelName = instruction[0][:-1]
                        # print(instruction)
                        # print(labelName)
                        if(labelName not in symbolTable.keys()):
                            instructionName = assemblyToOpcode[instruction[1]]
                            symbolTable[labelName] = i
                            labelorvariableTable[labelName]="L"
                            opcLit = addToOpcode(instruction[1:],assemblyToOpcode,memory,literalTable)
                            opcodeTable[i] = opcLit[0]
                            literalTable = opcLit[1]
                        else:
                            print("Error: Label: " +labelName+ " already declared")    

                    except:
                        print("Label "+ instruction[0][:-1]+" not defined correctly.")
                        sys.exit()
    ans.append(symbolTable)
    ans.append(opcodeTable)
    ans.append(literalTable)
    ans.append(labelorvariableTable)
    return ans
def secondPass(symbolTable,opcodeTable,literalTable,labelorvariableTable):
    ans=[]
    for i in range(len(opcodeTable)):
        instruction=opcodeTable[i]
        if instruction[0]=="DW":
            pass
        elif instruction[1]=="null":
            ans.append(instruction[2])
        # elif instruction[0]: 
        else:
            if instruction[1].isdigit():
                st=""
                st+=instruction[2]+" "
                address=str(bin(int(instruction[1])))[2:]
                while(len(address)<15):
                    address="0"+address
                ans.append(st+address)   
            else:
                st=""
                st+=instruction[2]+" "
                if instruction[1] in symbolTable.keys():
                    if (instruction[0] =="BRZ" or instruction[0] =="BRP" or instruction[0] =="BRN"):
                        if labelorvariableTable[instruction[1]] != "L":
                            print("Error: "+instruction[1]+" is a variable and hence cannot be branched to.")
                            sys.exit() 
                    else:
                        if labelorvariableTable[instruction[1]] != "V":
                            print("Error: "+instruction[1]+" is a Label and hence cannot be operated on.")
                            sys.exit()            
                    address=str(bin(int(symbolTable[instruction[1]])))[2:]
                    while(len(address)<15):
                        address="0"+address
                    ans.append(st+address)
                else:
                    print("Error: Label/Variable: "+instruction[1]+" is not initialized")
                    sys.exit()    
    return ans

if __name__ == "__main__":
    assemblyToOpcode = {"CLA":"0000","LAC":"0001","SAC": "0010","ADD":"0011","SUB":"0100", "BRZ":"0101","BRN":"0110","BRP":"0111","INP":"1000","DSP":"1001","MUL":"1010","DIV":"1011","STP":"1100","DW":"1101"}
    memory = {}
    for i in range(32768):
        if (i>28671):
            memory[str(i)] = 32767-i
        else:
            memory[str(i)] = "nullValue"
    print("Make sure that the input file is in the same directory as the Assemblr.py file")
    print("Enter the name for the input file.")
    name = input()     
    f = open(name, "r")
    l = []
    for x in f:
        l.append(x.split())
    # print(l)
    t = firstPass(l,memory,assemblyToOpcode)
    print(t[0])
    print(t[1])
    print(t[2])
    displ=secondPass(t[0],t[1],t[2],t[3])
    for i in displ:
        print(i)