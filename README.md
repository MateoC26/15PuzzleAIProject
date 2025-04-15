# 15 Puzzle AI Project
Using Sum of Chessboard Distance and A* search to provide a solution to a 15 puzzle (https://en.wikipedia.org/wiki/15_puzzle) given the Initial and Goal states.

A* Search

4 x 4 Board

Tiles: 1 - 15 (w/ 0 being blank tile)

Actions: 
1. Left
2. Up-Left
3. Up
4. Up-Right
5. Right
6. Down-Right
7. Down
8. Down-Left

Heuristic: Sum of Chessboard Distances

n: Initial State

m: Goal State

d: Depth of solution

N: Number of nodes generated

A: Actions taken to reach solution

f: f values of nodes along solution path

Input: 

n n n n

n n n n

n n n n

n n n n

m m m m

m m m m

m m m m

m m m m

Output:

n n n n

n n n n

n n n n

n n n n


m m m m

m m m m

m m m m

m m m m

d

N

A A A A A A ...

f f f f f f ...

Instructions to run:
1. Install python on your console with “Brew” or “pip” on your root directory as such: “Brew install python”
2. Download the entire folder as it is. Then navigate to the directory “15PuzzleAIProject” as such: “cd 15PuzzleAIProject”.
3. Run “python 15PuzzleProblem.py”.
4. You will be prompted to enter an input file name, until a match is found. Press enter once you have written it down in the console. Note: only files in the root of the project directory will be found, otherwise you must include the relative path to this directory.
5. The generated output will be written down in “sampleoutput.txt”. Note: this file gets re-written every time the algorithm is run with a new input. If you want to keep a record of the output, make a copy of “sampleoutput.txt” before rerunning the code.
6. The output files of “InputFile1”, “InputFile2”, “InputFile3”, have been included in the directory for your convenience.
