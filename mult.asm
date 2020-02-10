// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[3], respectively.)
// Blaine Broussard
    @0   
    D=A   //Set D register as zero
    @R2
    M=D   //Set D equal to multiple
    @R1   
    D=M
    @counter  //Make counter variable store the multiple
    M=D
(LOOP)
    @counter
    D=M
    @END  
    D;JEQ   //While loop that checks if multiple has run out yet
    @R0     //Set number being multiplied to d register
    D=M
    @R2          
    M=M+D     //Add R2 to iteself plus whatever is being multiplied 
    @counter   
    M=M-1     //Subtract from the counter, which is the same as the multiple
    @LOOP     //Loop
    0;JMP
(END)
    @END
    0;JMP