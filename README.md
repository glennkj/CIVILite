#CIVILite

Author: Glenn Joseph

Class: ICS-3U1-02

Date: May 22, 2019
Version: 1.0.0

Unit: All Encompassing CA!

Programming Language: 3.4.4.

Problem Description: 
    The ICS-3U1 Culminating activity is a practical test of all that was learned so far in the course. 
A game or useful program is created using all the features found in the course: if statements, lists, 
strings, variables, and any other pertinent data structure or holder.

    The ultimate game of strategy and history is finally here. Grow a country, Farm your land, grow your
population, conquer your enemies or race to space in the python-based clone of Sid Meier's CIVILIZATION 
series, CIVILite!

Program Assumptions: 

    User must have a computer with a running Python interpreter with the Python 3.4.4., a 
keyboard for commands and inputs, and a monitor to display the terminal.

Features of Program: 
    Program features a full menu experience with a help, quit and start selections, each having
options that can be interacted with, particularly a sub-menu for the help section which differentiates help 
depending on the player's experience. The game includes a randomly generated terrain with movable units, and a
skill tree of researchable technology. The game also includes 3 civilizations that each include their own 
strengths and weaknesses in terms of stats and special structure buildability. The user can create structures,
which helps the population of the city grow. The units can pillage other neighboring civilizations, and defend
their own civilization. The user's civilization has statuses for population, food, production, science, 
unit damage, and the capital's health, which each contribute to winning. The program also features checking
instances for each user input, both for general validity and for gameplay/map validity.

Restrictions:
    Gameplay restrictions include that you can't wage war on two civilizations at the same time, units
cannot move diagonally, units cannot move onto CPU civilization's territory without waging war, CPU civilizations
cannot react in a meaningful way to war, if you enter a unit order greater than 2 characters, the program only
intakes the first 2, when the user finds another civ, they don't see the territory they expand into, unless they
go back to that civ, and you have to finish your turn if you beat the game. The program also can't display unit 
battle information, nor can it display capital battle information, only displaying when a civ declares, loses, or
wins a war. Finally, depending on the civ's visibility, they can declare war on another civ even if they can't see
them.

Known Errors:
    The only known error occurs when the user enters ctrl + c into the compiler.

Implementation Details:
1. Turn on your computer
2. Open the python shell
3. Click "File", then "Open" near the top of the shell window, and select Simon_Joseph_CA.py
4. Click the open button next to the file name
5. Click F5 on the keyboard to start the program
6. Enter "S" to start the program  

Additional Files:
    Other than CiviLite.py and CiviLite_README.txt (this file), no extra files are 
needed

Additional Considerations:
    The restrictions given when creating this program outlined heavy limitations on the usage of
object-oriented-programming principles, particularly the restriction of classes, as uniquely defined classes were
not allowed to be used, so repeated function calls for specific objects were used in place of a more useful class.
As well, modules and extra files could not be used-outside of the python source code and this file- due to 
restrictions present in the software available at the school. 
