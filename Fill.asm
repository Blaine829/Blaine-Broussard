//Blaine Broussard
  
// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

    @SCREEN
    D=A
    @currword   //Memory currword stores the first screen memory address
    M=D
(1Loop)
    @KBD
    D=M
    @1Loop
    D;JEQ   //Check if keyboard is pressed, continue if it is
(BLACK)
     @KBD
     D=M
     @WHITE
     D;JEQ //If the keyboard is released, head to white loop
     @currword
     D=M
     @24576
     D=D-A    //Compare the currword minus max memory address, if it is zero, end and head to Bcleanup (screen is all black)
     @Bcleanup
     D;JGT
     @currword
     A=M      //Store currword value
     M=-1     //Set pixels to black
     @currword //A is currword again
     M=M+1     //Increment currword by one
     @BLACK
     0;JMP     //repeat the loop
(Bcleanup)
     @24575
     D=A
     @currword  //Set currword back to the max value, so that you are not exceeding max memory value
     M=D
     @2Loop     //Go back to the start of everything
     0;JMP
(2Loop)
     @KBD
     D=M
     @2Loop
     D;JGT   //Check if key is released, countinue if it is not
(WHITE)
     @KBD
     D=M
     @1Loop
     D;JNE   //If keyboard is pressed, head to top of loop
     @SCREEN
     D=A
     @currword  //If currword minus the screen value equals zero, the two are equal, and you have finshed clearing the screen, so send to Wcleanup
     D=M-D
     @Wcleanup
     D;JEQ
     @currword 
     A=M       //Store currword value
     M=0      //Set pixel to white
     @currword //A is currword again
     M=M-1     //Decrement currword
     @WHITE    //Repeat loop
     0;JMP
(Wcleanup)
     @SCREEN   //Set first screen value to white
     M=0
     @1Loop    //Go to the top
     0;JMP

