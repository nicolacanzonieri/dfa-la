# DFA Language Analyzer

This Python program creates a transition table for a Deterministic Finite Automaton (DFA). It then accepts a binary string of 0s and 1s and verifies whether this string is accepted by the DFA or not.

## Usage

To use the program:

1. Run the program.
2. Follow the prompts to input transitions for each state of the DFA, denoted as `q0`, `q1`, etc.
3. Input `!end!` to stop adding transitions for each state.
4. Add final states by inputting the state number of the final states, then input `!end!` to stop.
5. Once the DFA is defined, input binary strings when prompted to check if they are accepted by the DFA.
6. Input `!end!` to stop the program.

## Program Structure

- **`add_new_state(transition_table, input_counter, qx_0, qx_1)`:** Adds transitions for a new state to the transition table.
- **`add_final_states(transition_table)`:** Adds final states to the transition table.
- **`create_transition_table(transition_table, input_counter)`:** Guides the user to create the transition table for the DFA.
- **`run_dfa(transition_table, dfa_input)`:** Runs the DFA on the input string to determine acceptance.
- **`take_input(transition_table)`:** Allows the user to input strings to test DFA acceptance.
- **`main()`:** Main function to execute the program.

## Example

Suppose we have a DFA defined with transitions:

- `q0` on input `0` goes to `q1` and on input `1` goes to `q2`.
- `q1` on input `0` goes to `q3` and on input `1` goes to `q2`.
- `q2` on input `0` goes to `q3` and on input `1` goes to `q3`.
- `q3` on input `0` goes to `q3` and on input `1` goes to `q3`.
- `q2` is the only final state.

Then, running the program and inputting a binary string like `0101` would output "Input Accepted!", while a string like `1010` would output "INPUT NOT ACCEPTED!".
