debug = False # Flag to enable/disable debug output

def add_new_state(transition_table, input_counter, qx_0, qx_1):
    """
    Add transitions for a new state to the transition table.

    Args:
        transition_table (list): The transition table of the DFA.
        input_counter (int): The index of the current state.
        qx_0 (str): The destination state on input 0.
        qx_1 (str): The destination state on input 1.

    """
    if input_counter > 0:
        new_state_operations = [int(qx_0), int(qx_1)]
        transition_table.append([])
        transition_table[input_counter].extend(new_state_operations)
    else:
        new_state_operations = [int(qx_0), int(qx_1)]
        transition_table[input_counter].extend(new_state_operations)

def add_final_states(transition_table):
    """
    Add final states to the transition table.

    Args:
        transition_table (list): The transition table of the DFA.

    """
    while True:
        final_state_code = str(input("\nFinal state (insert !end! to stop adding final states): q"))
        if final_state_code == "!end!":
            break
        else:
            transition_table[int(final_state_code)].append("x")

def create_transition_table(transition_table, input_counter):
    """
    Guides the user to create the transition table for the DFA.

    Args:
        transition_table (list): The transition table of the DFA.
        input_counter (int): The index of the current state.
    
    """
    while True:
        print("\n\nSTATE Q" + str(input_counter) + " - (Insert !end! to stop creating new states)\n")

        qx_0 = str(input("Insert (q" + str(input_counter) + ", 0) = q"))
        if qx_0 == "!end!":
            break

        qx_1 = str(input("\nInsert (q" + str(input_counter) + ", 1) = q"))
        if qx_1 == "!end!":
            break
        
        add_new_state(transition_table, input_counter, qx_0, qx_1)
        
        input_counter += 1
    
    add_final_states(transition_table)
    if debug : print(transition_table)

def run_dfa(transition_table, dfa_input):
    """
    Runs the DFA on the input string to determine acceptance.

    Args:
        transition_table (list): The transition table of the DFA.
        dfa_input (str): The input string for the DFA.
    
    """
    current_state = 0
    start_char = 0
    end_char = 1

    while (end_char <= len(dfa_input)):
        char_input = int(dfa_input[start_char:end_char])
        next_state = int(transition_table[current_state][char_input])
        if debug : print("\nq" + str(next_state))
        start_char += 1
        end_char += 1
        current_state = next_state
    
    try:
        if transition_table[current_state][2] == 'x':
            print("\nInput Accepted!")
    except:
        print("\nINPUT NOT ACCEPTED!")

def take_input(transition_table):
    """
    Allows the user to input strings to test DFA acceptance.

    Args:
        transition_table (list): The transition table of the DFA.
    
    """
    while True:
        print("\n\n\nInsert an Input for the DFA - (insert !end! to stop the software):")
        dfa_input = str(input())

        if dfa_input == "!end!":
            print("\nProgram stopped")
            break
        else:
            run_dfa(transition_table, dfa_input)

def main():
    transition_table = [[]]
    input_counter = 0

    print("===========================================")
    print("DFA Language Analyzer by Nicola Canzonieri")
    print("===========================================\n")
    print("This software take a DFA and an Input and it will verify")
    print("that the Input is accepted by the DFA")

    create_transition_table(transition_table, input_counter)
    take_input(transition_table)

main()
