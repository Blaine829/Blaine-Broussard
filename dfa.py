#Jacob Tucker Vannoy and Blaine Broussard

class DFA():
    state = []
    alphabet = []
    initial = []
    final = []
    transitions = []
#Filename: DFA rules. Input: words to be put into DFA. Output: file to display acceptance or rejection
def DFA_Interpret(filename, input, output):
    read_file = open(filename, "r")
    file_lines = read_file.read()
    file_array = file_lines.split("\n")

    output_file = open(output, "w")

    dfa = DFA()
    dfa.state = file_array[0].split(",")
    dfa.alphabet = file_array[1].split(",")
    dfa.initial = file_array[2]
    dfa.final = file_array[3].split(",")
    for num in file_array[4:]:
         dfa.transitions.append(num.split(","))

    input_file = open(input,"r")
    input_lines = input_file.read()
    input_array = input_lines.split("\n")



    for lines in input_array:
        curr_state = dfa.initial
        for line in lines:
            for transitions in dfa.transitions:
                #If statement checks for a valid tranistion. If true update curr_state, if false keep looking
                if curr_state == transitions[0] and line == transitions[1]:
                    curr_state = transitions[2]
                    break #Found a valid transition, leave transitions loop

        if curr_state in dfa.final:
            output_file.write("accept\n")
        else:
            output_file.write("reject\n")


    print(curr_state)
    print(file_array)
    print(dfa.state)
    print(dfa.alphabet)
    print(dfa.initial)
    print(dfa.final)
    print(dfa.transitions)
    print(input_array)


    read_file.close()
    input_file.close()
    output_file.close()

def main():
    DFA_Interpret("dfa.txt","input.txt","output.txt")

if __name__ == "__main__":
    main()