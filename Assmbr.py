def firstPass(inpt,memory):
    symbolTable = {}
    unattendedLabels = {}
    for i in range(len(inpt)):
        instruction = inpt[i]
        try:
            if instruction[0][-1] ==":":
                newInst = instruction[0][:-1]
            else:
                newInst = instruction[0]
            if unattendedLabels[newInst]==0:
                symbolTable[newInst] =i+1
            # else:
            #     print(newInst+" label is not used anywhere.")
            #     sys.exit()     
            #     symbolTable[instruction[]]
        except:


        if instruction[0]=="BRZ" or instruction[0]=="BRN" or instruction[0]=="BRP":
            unattendedLabels[instruction[1]] = 0



if __name__ == "__main__":
    assemblyToOpcode = {"CLA":"0000","LAC":"0001","SAC": "0010","ADD":"0011","SUB":"0100", "BRZ":"0101","BRN":"0110","BRP":"0111","INP":"1000","DSP":"1001","MUL":"1010","DIV":"1011","STP":"1100"}
    memory = {}
    for i in range(32766):
        # print(int(str(bin(i+1))[2:]))
        memory[i+1] = "nullValue"
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
