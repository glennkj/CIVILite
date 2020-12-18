# CIVILite

## Note About the Project
The restrictions given when creating this program outlined heavy limitations on the usage of multiple files and
object-oriented-programming principles, particularly the restriction of classes, as uniquely defined classes were
not allowed to be used, so repeated function calls for specific objects were used in place of a class. 
Additionally the entire project had to be completed using python only, and no external modules.

### Problem Description: 

The ICS-3U1 Culminating activity is a practical test of all that was learned so far in the course. 
A game or useful program is created using all the features found in the course: if statements, lists, 
strings, variables, and any other pertinent data structure or holder. The description is relatively 
open ended, so my project revolved around a text based version of Sid Meier's CIVILIZATION, complete
with a text-based map that updates every turn.

### Program Assumptions: 

User must have a computer with a running Python interpreter with the Python 3.4.4., a 
keyboard for commands and inputs, and a monitor to display the terminal.

### Features of Program: 

Program features a full menu experience with a help, quit and start selections, each having
options that can be interacted with, particularly a sub-menu for the help section which differentiates help 
depending on the player's experience. The game includes a randomly generated terrain with movable units, and a
skill tree of researchable technology. The game also includes 3 civilizations that each include their own 
strengths and weaknesses in terms of stats and special structure buildability. The user can create structures,
which helps the population of the city grow. The units can pillage other neighboring civilizations, and defend
their own civilization. The user's civilization has statuses for population, food, production, science, 
unit damage, and the capital's health, which each contribute to winning. The program also features checking
instances for each user input, both for general validity and for gameplay/map validity.

### Restrictions:

Gameplay restrictions include that you can't wage war on two civilizations at the same time, units
cannot move diagonally, units cannot move onto CPU civilization's territory without waging war, CPU civilizations
cannot react in a meaningful way to war, if you enter a unit order greater than 2 characters, the program only
intakes the first 2 (only first character if entrance is "S" or "s"), when the user finds another civ, they don't
see the territory they expand into, unless they go back to that civ, and you have to finish your turn if you beat
the game. The program also can't display unit battle information, nor can it display capital battle information,
only displaying when a civ declares, loses, or wins a war. Finally, depending on the civ's visibility, they can
declare war on another civ even if they can't see them.
