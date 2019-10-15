"""Name: Rachit Mittal (2018302)
   Name: Siddharth Sadhwani (2018313)"""
import sys
def addToOpcode(instruction,assemblyToOpcode,memory,literalTable):
    opcodeTableValue = ["null","null","null"]
    err = True
    if (instruction[0] == "STP" or instruction[0] == "CLA"):
        try:
            x = instruction[1]
            if (x[0]=="#"):
                err = False
            if err:
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
            if (x[0]=="#"):
                err = False
            if err:
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
                    if instruction[0]=="INP" or instruction[0]=="SAC":
                        print("Error: Cannot store to a variable.")
                        sys.exit()
                    opcodeTableValue[1] = instruction[1]
                    opcLit = [opcodeTableValue,literalTable]
                    return opcLit
                else :
                    print("Error: Opcodes cannot be used as variable names")
                    sys.exit()          
            else:
                print("Error: Instruction format error: "+ instruction[1]+" is not a valid input format.")
                sys.exit()
    else:
        x = instruction[0]
        if (x[0]=="#"):
            pass
        else:
            print("Error: Not a valid instruction.")
            sys.exit()

def firstPass(inpt,memory,assemblyToOpcode):
    symbolTable = {}
    labelorvariableTable={}
    opcodeTable= {}
    literalTable = {}
    ans = []
    start = False
    startCounter = 0
    end = False
    for i in range(len(inpt)):
        instruction = inpt[i]
        if (not start):
            if instruction[0] == "START":
                if len(instruction)<2:
                    print("Error: Less parameters defined in the instruction START")
                    sys.exit()
                elif len(instruction)>2:
                    if instruction[2][0]=="#":
                        start = True
                        if (instruction[1].isdigit()):
                            startCounter = int(instruction[1])
                            for j in range(i+1, len(inpt)):
                                memory[str((j-1)+startCounter)] = "used"
                        else:
                            print("Error: Start format incorrect. Needs to define an address.")
                            sys.exit()
                    else:    
                        print("Error: More than required parameters defined in the instruction START")
                        sys.exit()
                else:
                    start = True
                    if (instruction[1].isdigit()):
                        startCounter = int(instruction[1])
                        for j in range(i+1, len(inpt)):
                            memory[str((j-1)+startCounter)] = "used"
                    else:
                        print("Error: Start format incorrect. Needs to define an address.")
                        sys.exit()
            else:
                print("Error: The program should always begin with START.")
                sys.exit()
        else:
            if (instruction[0]=="START"):
                print("Error: START is defined multiple times in the program.")
                sys.exit()
            if (instruction[0]=="END"):
                end = True
                if (len(instruction)>1):
                    if (instruction[1][0]=="#"):
                        pass
                    else:
                        print("Error: More than required parameters defined in the instruction END")
                        sys.exit()
                break
            if (len(instruction)>=3 and instruction[1]=="DW"):
                
                if (len(instruction)<3):
                    joined_string = ' '.join([str(v) for v in instruction])
                    print("Error: Less arguments in the instruction- "+joined_string)
                    sys.exit()  
                try:
                    x = instruction[3]
                    if x[0]=="#":
                        pass
                    else:
                        joined_string = ' '.join([str(v) for v in instruction])
                        print("Error: Too many arguments in the instruction- "+ joined_string)
                        sys.exit()
                except IndexError:
                    pass
                if(instruction[0] not in symbolTable.keys()):
                    if(len(instruction[0])!=0 and not instruction[0][0].isdigit() and instruction[0].isalnum()):
                        if(instruction[0] not in assemblyToOpcode.keys()):
                            if (instruction[2][0]=="'" or instruction[2][0]=='"'):
                                try:
                                    const=int(instruction[2][1:-1])
                                    if (const>4095):
                                        print("Error: Constant cannot exceed 12 bits of data, ie 4095(decimal).")
                                        sys.exit()
                                    memLoc=32767-const
                                    symbolTable[instruction[0]]=str(memLoc)
                                    labelorvariableTable[instruction[0]]="V"            #capital V
                                    opcodeTable[startCounter + i-1]=["DW",instruction[0],assemblyToOpcode["DW"]]    
                                except:
                                    print("Error: Wrong constant format")
                                    sys.exit()    
                            else:
                                print("Error: Wrong variable declaration for "+instruction[0]+". Only constants are allowed.")
                                sys.exit()        
                        else :
                            print("Error: Opcodes cannot be used as variable names: "+instruction[0])
                            sys.exit()          
                    else:
                        print("Error: Instruction format error: "+ instruction[1]+" is not a valid input format.")
                        sys.exit()
                else:
                    print("Error: Variable: " +instruction[0]+ " already declared")
                    sys.exit()        
            else:
                try:
                    instructionName = assemblyToOpcode[instruction[0]]
                    opcLit = addToOpcode(instruction,assemblyToOpcode,memory,literalTable)
                    opcodeTable[startCounter + i-1] = opcLit[0]
                    literalTable = opcLit[1]
                except KeyError:
                    if instruction[0][-1]!=":":
                        print("Error: "+instruction[0]+" is not a valid opcode.")
                        sys.exit()
                    else:
                        try:
                            labelName = instruction[0][:-1]
                            if(labelName not in symbolTable.keys()):
                                instructionName = assemblyToOpcode[instruction[1]]
                                symbolTable[labelName] = startCounter + i-1
                                labelorvariableTable[labelName]="L"
                                opcLit = addToOpcode(instruction[1:],assemblyToOpcode,memory,literalTable)
                                opcodeTable[startCounter + i-1] = opcLit[0]
                                literalTable = opcLit[1]
                            else:
                                print("Error: Label: " +labelName+ " already declared")
                                sys.exit()    

                        except:
                            print("Error: Label "+ instruction[0][:-1]+" not defined correctly.")
                            sys.exit()
    if not start:
        print("Error: Start not specified.")
        sys.exit()
    elif (not end):
        print("Error: End of program not specified.")
        sys.exit()
    ans.append(symbolTable)
    ans.append(opcodeTable)
    ans.append(literalTable)
    ans.append(labelorvariableTable)
    ans.append(startCounter)
    return ans

def secondPass(symbolTable,opcodeTable,literalTable,labelorvariableTable, startCounter):
    ans=[]
    for i in range(len(opcodeTable)):
        instruction=opcodeTable[startCounter + i]
        if instruction[0]=="DW":
            pass
        elif instruction[1]=="null":
            ans.append(instruction[2])
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
    a = open("DOCUMENTATION.txt","r")
    for i in a:
        print(i)
    a.close()
    print("Enter the name for the input file.")
    name = input()     
    f = open(name, "r")
    l = []
    for x in f:
        l.append(x.split())
    t = firstPass(l,memory,assemblyToOpcode)
    print()
    displ=secondPass(t[0],t[1],t[2],t[3],t[4])
    print("SYMBOL TABLE:")
    print("SYMBOL TYPE     MEMORY ADDRESS")
    for i in (t[0]):
        address = str(bin(int(t[0][i])))[2:]
        while(len(address)<15):
            address="0"+address
        print(str(i)+ "\t"+ str(t[3][i])+"\t" + address)
    print()
    print("OPCODE TABLE:")
    print("ASSEMBLY OPCODE      OPERAND   MACHINE OPCODE   MEMORY ADDRESS")
    for i in t[1]:
        x = t[1][i]
        address = str(bin(int(i)))[2:]
        if (x[1]=="null"):
            operand = "-"
        else:
            operand = x[1]            
        while(len(address)<15):
            address="0"+address
        print("\t"+x[0] + "\t\t"+ operand + "\t"+ x[2] + "\t\t"+address)
    print()
    print("LITERAL TABLE:")
    print("LITERAL MEMORY ADDRESS")
    for i in t[2]:
        x = t[2][i]
        address = str(bin(int(x)))[2:]        
        while(len(address)<15):
            address="0"+address
        print("   "+str(i)+ "\t"+ address)
    print()

    print("MEMORY ADDRESS     MACHINE CODE")
    cnt = 0
    for i in displ:
        address = str(bin(t[4]+cnt))[2:]
        while(len(address)<15):
            address="0"+address
        print(address+"    "+i)
        cnt +=1