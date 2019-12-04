# Simple Turing Machine Simulator


# Usage

To run the simulator **Python 2.7** needs to be installed. The program is run as a normal python script. The simulator expects two main arguments. The first one, using option `-t`, is a file containing the turing machine (see below for an example) and the second one is a input word.

`./turingSim.py -f fileName inputWord`

Ex.

`./turingSim.py -f doubleBalancig.tm aabb`


options:

  
  -h, --help show this help message and exit
  -t, --traceset for trace turing machine
  -r, --result        Print the output from the first track
  -b, --clearBlanks   Clear unused blanks from tracks
  -f fileName, --file=fileName  Filename for turing machine

#### The turing file sytax should

init: initialState
final: list of all final states
state char_1 ... char_n -> new_char_1 ... new_char_n move_1 .. move_n

allowed moves are R - right, L - left, S - stop. Reserved symbol on the tape is B for blank.

##### Exemple input turing file

init: q0
final: q1
q0 B -> q1 B S


