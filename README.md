# Assembler

#Group
-------------
*2018302 Rachit Mittal
*2018313 Siddharth Sadhwani

#Introduction
--------------------
Our Assembler(12 bit) converts assembly language code to machine language(binary) 
that can be executed by the microprocessor. It is a two-pass assembler i.e. it parses
through the code twice.

First-pass: During this opcode table, symbol table and literal table are formed.

Second-pass: In this pass, forward referencing of labels and variables are handled.

Opcode Table: Our opcode table holds Assembly code, operand, machine code and 
memory address respectively. 

Literal Table: It holds literal value and its address in the memory respectively.

Symbol Table: It holds the initialized Labels and Variables along with their memory addresses.

#Instructions handled by our assembler
-----------------------------------------------------------
Assembly Code      Machine Code      Meaning
       
      0000                      CLA            Clear accumulator                
      0001                       LAC            Load into accumulator from address  
      0010                       SAC            Store accumulator contents into address 
      0011                       ADD           Add address contents to accumulator contents
      0100                       SUB            Subtract address contents from accumulator contents
      0101                       BRZ            Branch to address if accumulator contains zero
      0110                       BRN            Branch to address if accumulator contains negative value
      0111                        BRP            Branch to address if accumulator contains positive value
      1000                       INP            Read from terminal and put in address 
      1001                       DSP            Display value in address on terminal 
      1010                       MUL           Multiply accumulator and address contents 
      1011                        DIV            Divide accumulator contents by address content.
      1100 		      STP	         Stop execution
 
#Input format followed in our assembler:
-----------------------------------------------------------

->Make sure that the input file is in the same directory as the Assemblr.py file.
->Maximum instruction length (word length) is 19 bits.
->All commands are to be entered in uppercase.
->Memory addresses are to entered as decimals.
->Valid Memory addresses include addresses from 0 to 28671(decimal).
->All constants are to be enclosed within single or double quotes(eg. '7' or "7").
->Label are to be followed by a semi-colon and a single space.(eg. L1: DSP 123).
->Label and Variables declaration is alpha-numeric and cannot start with a number.
->Variables can only be used to declare constants.
->Comments can be written either after an instruction or in a new line.
->Comments are preceded by a '#'  and a " " in case of comments after a instruction.
->Comments are preceded only by a "#" in case the comments aquire a whole line.    
->The assembler only processes instructions between keyword "START" and "END".
->Any instruction or comment cannot preceed the START instruction.
->Maximum value of a constant that can be initialized is 4095.
->A particular Label or Variable cannot be declared twice.
->Branching statement only branch to a Label or an address.

#Input
-----------
A file containing assembly code according to the given instructions above.

#Output
-------------
Opcode Table, Symbol Table and Literal Table followed by the respective translated 
memory-mapped machine code.

