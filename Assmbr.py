def addToOpcode(instruction,address,assemblyToOpcode):
    opcodeTableValue = ["null","null","null","null","null"]
    if (instruction[0] == "STP" or instruction[0] == "CLA"):
        opcodeTableValue[0] = instruction[0]
        opcodeTableValue[4] = assemblyToOpcode[instruction[0]]
        return opcodeTableValue
    elif (instruction[0] == "LAC" or instruction[0] == "SAC" or instruction[0] == "ADD" or instruction[0] == "SUB" or instruction[0] =="INP" or instruction[0] =="DSP" or instruction[0] =="MUL" or instruction[0] =="BRZ" or instruction[0] =="BRP" or instruction[0] =="BRN"):
        opcodeTableValue[0] = instruction[0]
        opcodeTableValue[4] = assemblyToOpcode[instruction[0]]
        if (instruction[0] =="BRZ" or instruction[0] =="BRP" or instruction[0] =="BRN"):
            opcodeTableValue[1] = instruction[1]
            return opcodeTableValue
        else:





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
            memory[i] = 32767-i
        else:
            memory[i] = "nullValue"
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
