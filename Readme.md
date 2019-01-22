## Problem  Description:

- The game starts with an empty board with 8x8 cells. 
- It will be a 2 player game, let one player be red and one be green. 
- Players take turns to place their orbs in a cell. One can add an orb in an empty cell or in a cell with his/her orbs. (e.g. a green player can place a green orb at an empty cell or in a cell with green orbs. Green orb cannot be placed in a cell containing red orb.) 
- When a cell has 3 orbs, adding a fourth one makes it explode, which causes 4 orbs to be added to adjacent 4 cells (up, down, left and right cell). If those 4 cells contain orbs of different color, they will convert to the color of exploded orb’s. 
- If cell A has 3 orbs already, and one of adjacent cells of A gets exploded, then one orb is added to A, which causes A to explode also. This may result to a chain reaction. 
- The player to claim all of the orbs will be the winner. 
- If the cell is located at one corner or in the edge, then it won’t have 4 adjacent cells. Corner cells have 2 adjacent cells, cells located in the edge have 3 adjacent cells, so a corner cell will explode if it has 2 orbs, and an edge cell will explode when 3rd orb is added to it.

N.B. : This problem is designed from the game “Chain Reaction” . You can get it from Google Play for more clarification. 

[Play Store] (https://play.google.com/store/apps/details?id=com.BuddyMattEnt.ChainReaction&hl=en)

## Instruction for running:

- Download the sample code from (https://github.com/kaykobad/ChainReactionAIBot/)
- Run the aicontest_file.py using python3 adding graphics speed as a command line argument. Here graphics speed denotes the speed of moves shown in the ui. You can try with different speed for your convenience.  [ python3 aicontest.py 1000 ]. You may have to install package "numpy", "PyOpenGl" ( >=3.0), "Pygame" (>=1.9.0) to run this script (can be installed using pip) . 
- Run the player_code_file_random_killer.py/player_code_file_decent_heuristic.py using python3 adding “R/G” as  a commandline argument. [ python3 player_code_file_random_killer.py R /python3 player_code_file_decent_heuristic.py]

### Before running the aicontest.py or aicontest_file.py install required packages using:
**pip install -r Requirements.txt**

### Run:
```
python aicontest_file.py 1000
python player_code_file_random_killer.py R
python player_code_file_decent_heuristic.py G
```
