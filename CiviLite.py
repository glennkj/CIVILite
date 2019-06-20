# Name: Glenn Joseph
# Program Name: CIVILite
# Date: May 22 2019
# Description: Collect resources and gain power within this Civilization-inspired text-based game.

#Import random library for random number generators that will follow
import random

#####################################################
#UI FUNCTIONS
#####################################################

#Define function that prints space between outputs for clarity
def space():
    #Print space
    print('')

#Define a function that allows the user to enter a command
def menu_receive():
    #Displays the title of the program on user start
    print('''
     ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄               ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌             ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
    ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀  ▐░▌           ▐░▌  ▀▀▀▀█░█▀▀▀▀ ▐░▌           ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀
    ▐░▌               ▐░▌       ▐░▌         ▐░▌       ▐░▌     ▐░▌               ▐░▌          ▐░▌     ▐░▌
    ▐░▌               ▐░▌        ▐░▌       ▐░▌        ▐░▌     ▐░▌               ▐░▌          ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄
    ▐░▌               ▐░▌         ▐░▌     ▐░▌         ▐░▌     ▐░▌               ▐░▌          ▐░▌     ▐░░░░░░░░░░░▌
    ▐░▌               ▐░▌          ▐░▌   ▐░▌          ▐░▌     ▐░▌               ▐░▌          ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀
    ▐░▌               ▐░▌           ▐░▌ ▐░▌           ▐░▌     ▐░▌               ▐░▌          ▐░▌     ▐░▌
    ▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄█░█▄▄▄▄        ▐░▐░▌        ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄█░█▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌        ▐░▌        ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌
     ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀          ▀          ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀ ''')

    #Determine the user's input
    user_input = input('''
                Welcome to CIVILite! Enter a command:
 ____________________   ____________________   ___________________
|          S         | |         H          | |         Q         |
|    Open the Game   | |    Display Help    | |    Quit Program   |
|____________________| |____________________| |___________________|

''')#Shows the user the commands to enter in an aesthetically-pleasing manner

    #Print space for clarity
    space()

    #Return the user's input to the original variable
    return user_input

#Define a function that checks the menu inputs for validity
def menu_check(user_command):

    # While the user continues entering invalid commands, run them through a loop that notifies them.
    while user_command != "S" and user_command != "s" and user_command != "H" and user_command != "h" and user_command != "Q" and user_command != "q":
        #Clarify command is incorrect
        print('Please enter a valid command.')

        #Print space for clarity
        space()

        #Receive the user's input again
        user_command = menu_receive()

        #Print space for clarity
        space()

    #Return the user's command to the original variable
    return user_command

#Define a function that receives a help menu input
def game_help_input():
    #Split the menu up into multiple options to make it more user friendly
    help_menu_input = input('Enter "N" if you are new to civilization type games, or "E" if you are relatively experienced with these types of games\n')

    #Print space for clarity
    space()

    #Return the input to the original variable
    return help_menu_input

#Define a function that checks within help inputs
def game_help_check(help_input):
    #Begin a while loop that runs while the user keeps entering incorrect inputs
    while help_input != "N" and help_input != "n" and help_input != "E" and help_input != "e":
        #Notify the user of their mistake
        print('Please enter a valid help menu input.')

        #Print space for clarity
        space()

        #Let the user re-enter their input
        help_input = game_help_input()

    #Return the checked help input to the original variable
    return help_input

#Define a function that provides help to the user when requested
def game_help():

    #Receive the user's help input
    help_input = game_help_input()

    #Check the user's help input
    help_input = game_help_check(help_input)

    #Begin an if statement depending on which input the user entered
    if help_input == 'N' or help_input == 'n':

        #Print a statement explaining all the elements of the game
        print('''
INTRODUCTION
CIVILite is a game based around the game Sid Meier's CIVILIZATION. The game revolves around exploration and progression in a preset map. The map will randomly assign where your civilization (civ) starts- your capital. The game also randomly assigns where resources spawn, and where the other civs in your game start. You begin as all civilizations do- in the stone era. The game is split up into turns, where you command your units and city to move and begin building and researching things respectively. After you decide plans for your civilization, the computer makes semi-random decisions on its own moves, and all moves occur.

UNIT MOVEMENT
You can build and control units that explore and attack, and structures that harness resources that advance your society's efficiency and ability. Units compete in battle with units from other civs when both are on the same tile; the damage of both civs are compared, and the civ with a higher damage wins (in tie cases, the winner is random.). Unit battle is not notified, only shown, a unit defeated in battle will not show up on the map nor will it require orders, but the game will not explicitly notify the unit's outcome.

SCIENCE
Your city also chooses a technology it wants to research, furthering your understanding of science. Resources contribute to population increases, while production contributes to the development of new units and structures. Population contributes mostly to your level of science and research (your resources partially contribute to your science as well) which allows you to research technologies that increase your resource intake, unit damage or capital health. These two productions, units and science, contribute to the two ways to win the game, the Ruling Victory and the Research Victory.

VICTORY
The Ruling Victory is accomplished by destroying all other capitals in the game as your own (this is done by waging war, then attacking the capital with your units), forcibly cementing your civilization in the test of time. The Research Victory is accomplished by using science and researching technology until you gain the information required to place your civilization's flag on the moon, cementing your civilization in the cosmos of history. Your climb for victory comes in conflict with the other civs seeking the same goal. You can choose to wage war on civs you come across, or not interact at all (waging war occurs when you step into another civs territory). Each civ comes with a special structure, indicating the point at which they are strong, and increasing the amount of resource they receive from a tile. It's important to note that if a regular structure is in place, a special structure can't be built.


CIVILIZATIONS
The following list outlines each civ:

Rome - A once mighty empire has the chance to thrive again! Rome is a civilization best equipped in the early game, boasting powerful starting stats that support an early lead, with a weaker rate of increase overtime. Rome's special building is the Horreum, a building meant to facilitate food storage, allowing much more resource to be taken per tile. The horreum is available to be built from the metal era. Rome is ruled by Julius Caesar, a great emperor that will ensure Rome's survival in the test of time.

India - A just and long-surviving civilization, competes again in history's gladitorial pits! India is a balanced civilization sporting relatively strong starting stats with a good rate of increase as time continues. India's special building is the Sugar Mill, a refinery that processes sugar, allowing slightly more resource to be taken per tile. The sugar mill can be built in the medieval era. India is ruled by Mohandas Gandhi, a peaceful and just leader only seeking India's prosperity, but still capable in the face of opposition.

United States of America - A prosperous and patriotic country, proving itself against glorious civilizations, sure of its ability to survive! America is a civilization best equipped in the late game, equipped with modest starting stats with a strong rate of increase ensuring its power in the future. America's special building is the combine harvester farm, This allows more resource to be taken per tile. The combine harvester farm can be built from the modern era. America is ruled by George Washington, a ruler seeking the advancement of America until no other civilization approaches its ability.

CIVILIZATIONS NOTES
You are able to select any of these civilizations to represent you, however the other two become the computer's civs and your opponents. While they all tend to stray one way in terms of their strengths, the bigger priority is your strategy, and how well you can plan your decisions around accomplishing a specific goal. Planning the victory you want to achieve is key. The Research Victory is achieved when a spaceship is built, only possible when the last technology is researched. The Ruling Victory occurs when you control every other capital; in order to do this, war must be waged with all other civilizations. This happens instantly whenever you step into another civ's captured territory.

TILE GUIDE
The occurrences of a tile are indicated by whatever letters are present on a tile (up to 3). The following is a guide to what every letter means:

C - Your capital (regardless of selected civ)
c - Your territory (regardless of selected civ)
u - your unit (regardless of selected civ)
r - unfarmed resource
R - farmed resource
S - farmed resource by a special building
J - Roman capital
j - Roman territory
l - Roman unit
G - Indian capital
g - Indian territory
i - Indian unit
W - American capital
w - American territory
a - american unit
x - an undiscovered tile

In each tile, the information is shown in order of Ownership, Resource Status, and Unit Presence, for example, a captured tile owned by you, with a special building, and your unit looks like
=====
|   |
|cSu|
|   |
=====

This dictionary of indicators can be brought up during the production portion of a turn.


SCIENCE TREE
The science tree dictates the order in which you can research technologies. You must research both technologies before advancing to the next era. The tech tree in CIVILite looks like this:


      STONE ERA                       METAL  ERA                      MEDIEVAL ERA                   RENAISSANCE                   MODERN  ERA                     POST-MODERN ERA
    Primitive Tools                     Weaponry                       Feudalism                    Printing Press                   Computer                            AI
Increases resource intake         Increases unit damage           Increases unit damage         Increases capital health      Increases resource intake       Required to begin spaceship
                      ----->                          ----->                         ----->                         ----->                         ----->
      Agriculture                      Metallurgy                      Religion                      Hand Cannon                 Military Aircrafts                   Astronomy
Increases resource intake        Increases capital health       Increases resource intake        Increases unit damage          Increases unit damage        Required to complete spaceship

Every era, your units can move a little farther, going from 2 in the first two, 3 in the middle two, and finally 4 in the last two. This tree can be brought up during the research portion of a turn


CONCLUSION
With this information, you can begin with an apt understanding of how your civilization can thrive. The only thing left is to test how you will be recorded in the annals of time. Which will you be, Ruler or Researcher?

PLEASE PLAY IN MAX WINDOW SIZE FOR TITLE AND MAP FEATURE TO WORK''')

    #Otherwise, the user is requesting more basic help
    else:
        #Display more basic help
        print('''

INTRODUCTION
CIVILite is a game based around the game Sid Meier's CIVILIZATION. In CIVILite, you have three tasks per turn, moving a unit, producing a product, and researching a technology. There are three stats that increase every turn, your production, your science, and your population. Resources contribute to population increases, while production contributes to the development of new units and structures. Population contributes mostly to your level of science and research (your resources partially contribute to your science as well) which allows you to research technologies that increase your resource intake, unit damage or capital health.

VICTORY
These two productions, units and science, contribute to the two ways to win the game, the Ruling Victory and the Research Victory. The Ruling Victory is accomplished by destroying all other capitals in the game as your own (this is done by waging war, then attacking the capital with your units). The Research Victory is accomplished by using science and researching technology until you gain the information required to place your civilization's flag on the moon.

UNIT MOVEMENT
Units compete in battle with units from other civs when both are on the same tile, the damage of both civs are compared, and the civ with a higher damage wins (in tie cases, the winner is random.). Unit battle is not notified, only shown, a unit defeated in battle will not show up on the map nor will it require orders, but the game will not explicitly notify the unit's outcome

CIVILIZATIONS
Your climb for victory comes in conflict with the other civs seeking the same goal. Each civ comes with a special structure, indicating the point at which they are strong, and increasing the amount of resource they receive from a tile. It's important to note that if a regular structure is in place, a special structure can't be built. The following list outlines each civ:

Rome - A once mighty empire has the chance to thrive again! Rome is a civilization best equipped in the early game, boasting powerful starting stats that support an early lead, with a weaker rate of increase overtime. Rome's special building is the Horreum, a building meant to facilitate food storage, allowing much more resource to be taken per tile. The horreum is available to be built from the metal era. Rome is ruled by Julius Caesar, a great emperor that will ensure Rome's survival in the test of time.

India - A just and long-surviving civilization, competes again in history's gladitorial pits! India is a balanced civilization sporting relatively strong starting stats with a good rate of increase as time continues. India's special building is the Sugar Mill, a refinery that processes sugar, allowing slightly more resource to be taken per tile. The sugar mill can be built in the medieval era. India is ruled by Mohandas Gandhi, a peaceful and just leader only seeking India's prosperity, but still capable in the face of opposition.

United States of America - A prosperous and patriotic country, proving itself against glorious civilizations, sure of its ability to survive! America is a civilization best equipped in the late game, equipped with modest starting stats with a strong rate of increase ensuring its power in the future. America's special building is the combine harvester farm, This allows more resource to be taken per tile. The combine harvester farm can be built from the modern era. America is ruled by George Washington, a ruler seeking the advancement of America until no other civilization approaches its ability.

CIVILIZATIONS NOTES
You are able to select any of these civilizations to represent you, however the other two become the computer's civs and your opponents The Research Victory is achieved when a spaceship is built, only possible when the last technology is researched. The Ruling Victory occurs when you control every other capital; in order to do this, war must be waged with all other civilizations. This happens instantly whenever you step into another civ's captured territory.

TILE GUIDE
The occurrences of a tile are indicated by whatever letters are present on a tile (up to 3). The following is a guide to what every letter means:

C - Your capital (regardless of selected civ)
c - Your territory (regardless of selected civ)
u - your unit (regardless of selected civ)
r - unfarmed resource
R - farmed resource
S - farmed resource by a special building
J - Roman capital
j - Roman territory
l - Roman unit
G - Indian capital
g - Indian territory
i - Indian unit
W - American capital
w - American territory
a - american unit
x - an undiscovered tile

In each tile, the information is shown in order of Ownership, Resource Status, and Unit Presence, for example, a captured tile owned by you, with a special building, and your unit looks like
=====
|   |
|cSu|
|   |
=====

This dictionary of indicators can be brought up during the production portion of a turn.

SCIENCE TREE
The science tree dictates the order in which you can research technologies. You must research both technologies before advancing to the next era. The tech tree in CIVILite looks like this:


      STONE ERA                       METAL  ERA                      MEDIEVAL ERA                   RENAISSANCE                   MODERN  ERA                     POST-MODERN ERA
    Primitive Tools                     Weaponry                       Feudalism                    Printing Press                   Computer                            AI
Increases resource intake         Increases unit damage           Increases unit damage         Increases capital health      Increases resource intake       Required to begin spaceship
                      ----->                          ----->                         ----->                         ----->                         ----->
      Agriculture                      Metallurgy                      Religion                      Hand Cannon                 Military Aircrafts                   Astronomy
Increases resource intake        Increases capital health       Increases resource intake        Increases unit damage          Increases unit damage        Required to complete spaceship

Every era, your units can move a little farther, going from 2 in the first two, 3 in the middle two, and finally 4 in the last two. This tree can be brought up during the research portion of a turn.

CONCLUSION
With this information, you can begin with an apt understanding of how your civilization can thrive. The only thing left is to test how you will be recorded in the annals of time. Which will you be, Ruler or Researcher?

PLEASE PLAY IN MAX WINDOW SIZE FOR TITLE AND MAP FEATURE TO WORK''')

    #Print whitespace for clarity
    space()

#Define a function that determines which menu option the user wants
def menu(menu_command):
    #Run the user through an if statement for both the possible option, ending with an else statement for quitting
    if menu_command == 'S' or menu_command == 's':
        #Make the flag false so the game starts
        quitting_flag = False
    elif menu_command == 'H' or menu_command == 'h':
        #Run the user through the help function
        game_help()

        #Run the user through the receiving function and hold their answer
        menu_command = menu_receive()

        #Check the user's menu command
        menu_command = menu_check(menu_command)

        #Recursively call this function so there is a loop
        quitting_flag = menu(menu_command)
    else:
        #Make the flag true so the game quits
        quitting_flag = True

    #Return the quitting flag to the original variable
    return quitting_flag

################################################
#MAP FUNCTIONS
################################################

#Define a function that creates random values for each block of the map
def map_value_generator(map_unit_list):
    #Establish empty dictionary that will hold all the units with a list for each one that holds info on the unit's properies
    unit_info_dictionary = {}

    #Go through each row to access each unit
    for rows in map_unit_list:

        #Go through each unit in the row and assign the previously mentioned list to them
        for units in rows:
            #Establish a value that will determine whether a resource is on the block or nor
            resource_determiner = random.randint(1,5)

            #Begin an if statement that determines if there will be a resource or not
            if resource_determiner == 1 or resource_determiner == 2:
                #If the variable is either of these values, make a flag of the resource that indicates a resource is present
                resource_flag = True
            #Otherwise, there is no resource
            else:
                #Make the flag indicate no resource is present
                resource_flag = False

            #Add entries to the dictionary with the key being the current tile in the list, and the value being a list of several tile statuses, those statuses being [visibility, resource presence, whether the tile is a city's capital, whether a structure is present, whether a unit is present, which civ's unit (1 for India, 2 for Rome, 3 for America), whether the tile is captured in general, which civ captured it (0 for no one, 1 for India, 2 for Rome, 3 for America), whether the user owns it, and whether there is a special structure on it.]
            unit_info_dictionary[units] = [True,resource_flag, False, False, False, 0, False, 0, False, False]

    #Return the final dictionary to the original variable
    return unit_info_dictionary

#Define a function that re-generates the map given the updated info
def map_updater(unit_info_dictionary, user_civ_number):

    #Hold the string form of each row using 10 separate variables with a bottom one to cap it off. This makes it easier to use a loop for this mess
    row_1 = '''
=========================================
|   |   |   |   |   |   |   |   |   |   |
| x | x | x | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |   |   |'''

    row_2 = '''
=========================================
|   |   |   |   |   |   |   |   |   |   |
| x | x | x | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |   |   |'''

    row_3 = '''
=========================================
|   |   |   |   |   |   |   |   |   |   |
| x | x | x | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |   |   |'''

    row_4 = '''
=========================================
|   |   |   |   |   |   |   |   |   |   |
| x | x | x | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |   |   |'''

    row_5 = '''
=========================================
|   |   |   |   |   |   |   |   |   |   |
| x | x | x | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |   |   |'''

    row_6 = '''
=========================================
|   |   |   |   |   |   |   |   |   |   |
| x | x | x | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |   |   |'''

    row_7 = '''
=========================================
|   |   |   |   |   |   |   |   |   |   |
| x | x | x | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |   |   |'''

    row_8 = '''
=========================================
|   |   |   |   |   |   |   |   |   |   |
| x | x | x | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |   |   |'''

    row_9 = '''
=========================================
|   |   |   |   |   |   |   |   |   |   |
| x | x | x | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |   |   |'''

    row_10 = '''
=========================================
|   |   |   |   |   |   |   |   |   |   |
| x | x | x | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |   |   |'''

    bottom_row = '''
========================================='''

    #Make each row a list so the sequence is mutable
    row_1 = list(row_1)
    row_2 = list(row_2)
    row_3 = list(row_3)
    row_4 = list(row_4)
    row_5 = list(row_5)
    row_6 = list(row_6)
    row_7 = list(row_7)
    row_8 = list(row_8)
    row_9 = list(row_9)
    row_10 = list(row_10)

    #Establish an indexer for the dictionary that will be increased as the loop continues, but since it starts at key value 1, establish the variable at 1
    tile_value_index = 1

    #Hold all the rows in a list that will be looped
    row_list = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9, row_10]

    #Begin going through each row
    for rows in row_list:

        #Begin the numbers at the first instance of ' x ' in the list (86th up to not including 89th character)
        indexing_first_variable = 86
        indexing_last_variable = 89

        #Begin secondary loop that runs for all 10 blocks of the row
        for changes in range(10):
            change_to_be_made = [' ', ' ', ' ']

            #Hold the current value of the pertinent section in a variable
            #change_to_be_made = rows[indexing_first_variable:indexing_last_variable]

            #If the value to the corresponding key is true, the tile is undiscovered
            if unit_info_dictionary[tile_value_index][0] == True:
                #Make the tile appear undiscovered
                change_to_be_made[1] =  'x'
            else:
                #This is the if statement for the capture and ownership section, goes through all the possible permutations in the capture and ownership section of the changes to be made to a tile.
                if unit_info_dictionary[tile_value_index][2] == True and unit_info_dictionary[tile_value_index][8] == True:
                    #Make the tile appear to have been owned by the player and become their capital.
                    change_to_be_made[0] = 'C'

                elif unit_info_dictionary[tile_value_index][6] == True and unit_info_dictionary[tile_value_index][8] == True:
                    #Make the tile appear to have been captured by the player.
                    change_to_be_made[0] = 'c'

                elif unit_info_dictionary[tile_value_index][2] == True and unit_info_dictionary[tile_value_index][7] == 2:
                    #Make the tile appear to have been captured by rome and contain the capital.
                    change_to_be_made[0] = 'J'

                elif unit_info_dictionary[tile_value_index][6] == True and unit_info_dictionary[tile_value_index][7] == 2:
                    #Make the tile appear to have been captured by rome.
                    change_to_be_made[0] = 'j'

                elif unit_info_dictionary[tile_value_index][2] == True and unit_info_dictionary[tile_value_index][7] == 1:
                    #Make the tile appear to have been captured by india and contain the capital.
                    change_to_be_made[0] = 'G'

                elif unit_info_dictionary[tile_value_index][6] == True and unit_info_dictionary[tile_value_index][7] == 1:
                    #Make the tile appear to have been captured by india.
                    change_to_be_made[0] = 'g'

                elif unit_info_dictionary[tile_value_index][2] == True and unit_info_dictionary[tile_value_index][7] == 3:
                    #Make the tile appear to have been captured by rome and contain the capital.
                    change_to_be_made[0] = 'W'

                elif unit_info_dictionary[tile_value_index][6] == True and unit_info_dictionary[tile_value_index][7] == 3:
                    #Make the tile appear to have been captured by rome.
                    change_to_be_made[0] = 'w'

                #This is the if statement for the resource section, goes through all possible permutations in the resource section of the changes to be made to a tile.
                if unit_info_dictionary[tile_value_index][1] == True and unit_info_dictionary[tile_value_index][3] == False:
                    #Make the tile appear to have just a resource
                    change_to_be_made[1] = 'r'

                elif unit_info_dictionary[tile_value_index][1] == True and unit_info_dictionary[tile_value_index][9] == True:
                    #Make the tile appear to have a farmed resource
                    change_to_be_made[1] = 'S'

                elif unit_info_dictionary[tile_value_index][1] == True and unit_info_dictionary[tile_value_index][3] == True:
                    #Make the tile appear to have a farmed resource
                    change_to_be_made[1] = 'R'

                #This is the if statement for the unit section, goes through all possible permutations in the unit section of the changes to be made to a tile.
                if unit_info_dictionary[tile_value_index][5] == user_civ_number and unit_info_dictionary[tile_value_index][4] == True:
                    #Make the tile appear to contain a player unit.
                    change_to_be_made[2] = 'u'

                elif unit_info_dictionary[tile_value_index][4] == True and unit_info_dictionary[tile_value_index][5] == 2:
                    #Make the tile appear to contain a roman unit.
                    change_to_be_made[2] = 'l'

                elif unit_info_dictionary[tile_value_index][4] == True and unit_info_dictionary[tile_value_index][5] == 1:
                    #Make the tile appear to contain an india unit.
                    change_to_be_made[2] = 'i'

                elif unit_info_dictionary[tile_value_index][4] == True and unit_info_dictionary[tile_value_index][5] == 3:
                    #Make the tile appear to contain a american unit.
                    change_to_be_made[2] = 'a'

            #Change that section of the list to the changes made in the if statement
            rows[indexing_first_variable:indexing_last_variable] = change_to_be_made

            #Increase the indexer by 1 since the key values in the dictionary directly relate to integer values
            tile_value_index += 1


            #Increase the initial variable by 4 since that position is 4 characters ahead
            indexing_first_variable += 4

            #Increase the final variable by 4 since that position is 4 characters ahead
            indexing_last_variable += 4


    #Make all the rows a string by joining all the characters in the list with nothing inbetween them
    row_1 = ''.join(row_1)
    row_2 = ''.join(row_2)
    row_3 = ''.join(row_3)
    row_4 = ''.join(row_4)
    row_5 = ''.join(row_5)
    row_6 = ''.join(row_6)
    row_7 = ''.join(row_7)
    row_8 = ''.join(row_8)
    row_9 = ''.join(row_9)
    row_10 = ''.join(row_10)

    #Make the total map by combining all the rows together
    total_map = row_1 + row_2 + row_3 + row_4 + row_5 + row_6 + row_7 + row_8 + row_9 + row_10 + bottom_row

    #Return the assembled map
    return total_map

###############################################
#USER CIV CHOICE FUNCTIONS
###############################################

#Define a function that holds a user's chosen civ
def user_civ_receiver():
    #Receive the user's input for their choice of civilization
    user_civ = input('Which civilization will you rule? ("R" for Rome, "I" for India, and "A" for The United States.)\n')

    #Input white space for clarity
    space()

    #Return the user's chosen civ to the original variable
    return user_civ

#Define a function that checks the user's choice of civ
def user_civ_choice_check(user_civ):

    #Begin a while loop that runs while the user inputs incorrect entrances
    while user_civ != 'R' and user_civ != 'r' and user_civ != 'I' and user_civ != 'i' and user_civ != 'A' and user_civ != 'a':
        #Notify user civ choice is invalid
        print('Please enter a valid civ choice.')

        #Input white space for clarity
        space()

        #Let the user re-enter their civ choice
        user_civ = user_civ_receiver()

    #Return the user's choice of civ to the original variable
    return user_civ

#Define a function that makes the user's choice capital so it's only one item to worry about
def choice_capitalizer(chosen_item):
    #Capitalize the first (only one letter anyway) letter of the user's choice
    chosen_item = chosen_item.capitalize()

    #Return user's choice to original variable
    return chosen_item

#Define a function that changes the user's civ to a number to make dictionary use easier
def user_civ_number(user_civ):
    #Begin an if statement for 2 civs the user could have, and end with an else statement since the user could be no other civ
    if user_civ == 'I':
        user_civ = 1
    elif user_civ == 'R':
        user_civ = 2
    else:
        user_civ = 3

    #Return the numerical civ version to the original variable
    return user_civ

###############################################
#AREA CHECK FUNCTION & DICTIONARY MANUPULATORS
###############################################

#Define a function that checks if the area being expanded into is valid
def area_expansion_check(tile_info_dictionary, tiles_expanded_into, tile_expanded_from):
    #Begin a counter that indexes that item in the list
    index = 0

    #Determine the length of the tile list
    tiles_tupled = tuple(tiles_expanded_into)

    #Begin a for loop that runs for all tiles that need to be captured
    for tile in tiles_tupled:
        #Establish variables that will be used in if statements to determine invalid tiles
        side_test = tile_expanded_from % 10
        side_test2 = tile % 10

        #Establish an if statement that determines if the tile is off the map or not, if it is, delete it from the list
        if (tile < 1 or tile > 100) or (side_test == 0 and side_test2 == 1) or (side_test == 1 and side_test2 == 0) or (tile_info_dictionary[tile][7] != 0) or (tile_info_dictionary[tile][4] == True):
            #Remove the invalid tile from the list
            del(tiles_expanded_into[index])
        #Otherwise, increase the indexer so it keeps up with the list
        else:
            #Increase the indexer by 1 so it keeps up with items in the list
            index += 1

    #Return the list of tiles expanded into to the original variable
    return tiles_expanded_into

#Define a function that switches the dictionary info in a given set of tiles to show the user accurate info
def dictionary_value_changer(tile_info_dictionary, tiles_to_be_controlled, civ_number):
    #Begin a for loop that runs for all tiles in those to be controlled
    for tiles in tiles_to_be_controlled:
        #Make the corresponding number in the dictionary indicate that this tile is the corresponding civs corresponding tile by changing that key's corresponding list values.
        tile_info_dictionary[tiles][6] = True
        tile_info_dictionary[tiles][7] = civ_number

#Define a function that switches the dictionary info in a given set of tiles to show the user accurate info
def dictionary_value_changer_capital(tile_info_dictionary, capital, civ_number):
    #Make the corresponding number in the dictionary indicate that this tile is the capital by changing that key's corresponding list values. Not using regular dictionary value changer because capitals have special dictionary changes
    tile_info_dictionary[capital][1] = False
    tile_info_dictionary[capital][2] = True
    tile_info_dictionary[capital][7] = civ_number

#Define a function that changes tile values to indicate the user owns them
def user_territory_dictionary_indicator(tile_info_dictionary, user_tiles):
    #Start a for loop that runs for all the tile territories that the user will own
    for tiles in user_tiles:
        #Make the corresponding value indicate the user owns this tile and make it visible to the user
        tile_info_dictionary[tiles][8] = True
        tile_info_dictionary[tiles][0] = False

##########################################
#USER MAP FUNCTION & STARTING AREA FUNCTION
##########################################

#Define a function that gives the civ their starting area
def starting_area(tile_info_dictionary, civ_number, capital_tile):
    #Determine all the area the user gets a result of their capital placement
    territory1 = capital_tile - 10
    territory2 = capital_tile - 1
    territory3 = capital_tile + 1
    territory4 = capital_tile + 10

    #Store all the areas that will be the civ's in a list
    territories = [territory1, territory2, territory3, territory4]

    #Run the intended areas through a function that checks if the area is on the map
    territories = area_expansion_check(tile_info_dictionary, territories, capital_tile)

    #Change dictionary values using a particular function to indicate captured but not capital territories
    dictionary_value_changer(tile_info_dictionary, territories, civ_number)

    territories.insert(0, capital_tile)

    #Return the checked list of user territories
    return territories

#Define a function that determines which area the user's capital starts with
def user_capital(tile_info_dictionary, chosen_civ_number):
    #Use RNG to determine the user's civ
    capital = random.randint(1,100)

    #Hold a changed dictionary in the same variable since dictionaries seem to hold some sort of perma-global
    dictionary_value_changer_capital(tile_info_dictionary, capital, chosen_civ_number)

    #Return the user's capital to the original variable
    return capital

##########################################
#CPU EQUIVALENT FUNCTIONS FOR MAP AND CIV TYPE
##########################################

#Define a function that determines which civs the cpus are
def cpu_civ_determiner(civ_number):
    #Create an if statement that determines which civs the other two cpus are, with an else statement for the last number
    if civ_number == 1:
        #If 1 is taken, the other 2 are civs for the cpu
        cpu_civs = [2,3]
    elif civ_number == 2:
        #If 2 is taken, the other 2 are civs for the cpu
        cpu_civs = [1,3]
    else:
        #If 3 is taken, the other 2 are civs for the cpu
        cpu_civs = [1,2]

    #Return the list of civ cpus
    return cpu_civs

#Define a function that determines if the cpu capitals are too close to taken territories (different because this checks corners, regular cpu function only determines currently captured tiles)
def cpu_capital_checker(tile_info_dictionary, cpu_capital):
    #Establish a set of variables to help determine if the capital is too close to other territories
    cpu_capital_up_left_check = cpu_capital - 11
    cpu_capital_up_check = cpu_capital - 10
    cpu_capital_up_right_check = cpu_capital - 9
    cpu_capital_left = cpu_capital - 1
    cpu_capital_right = cpu_capital + 1
    cpu_capital_bot_left_check = cpu_capital + 9
    cpu_capital_bot_check = cpu_capital + 10
    cpu_capital_bot_right_check = cpu_capital + 11

    #Hold the territories to be checked in a list so a loop can be used
    cpu_territories_to_check = [cpu_capital, cpu_capital_up_left_check, cpu_capital_up_check, cpu_capital_up_right_check, cpu_capital_left, cpu_capital_right, cpu_capital_bot_left_check, cpu_capital_bot_check, cpu_capital_bot_right_check]

    #Hold the length of the current list of territories to check
    territory_check_length = len(cpu_territories_to_check)

    #Check whether the territories to check are on or near other civs lands
    cpu_territories_to_check = area_expansion_check(tile_info_dictionary, cpu_territories_to_check, cpu_capital)

    #Determine the length of the list after it goes through the expansion check
    territory_check_length2 = len(cpu_territories_to_check)

    #If the two numbers have different values, change the capital
    if territory_check_length != territory_check_length2:
        #Indicate the capital needs to be changed
        capital_changing_flag = True
    #Otherwise, the capital is in a good location
    else:
        #Establish a flag indicating the capital doesn't need to be changed
        capital_changing_flag = False

    #Return the capital flag to the original variable
    return capital_changing_flag

#Define a function that determines where the cpu starts
def cpu_capital_determiner(tile_info_dictionary, cpu_civ_number):
    #Establish a flag so the following loop begins
    capital_change = True

    #Begin a while loop that continues while the cpu capital is invalid
    while capital_change == True:

        #Use RNG to determine the user's civ
        capital = random.randint(1,100)

        #Determine if the capital needs to be changed or not
        capital_change = cpu_capital_checker(tile_info_dictionary, capital)

    #Change the capital's dictionary values
    dictionary_value_changer_capital(tile_info_dictionary, capital, cpu_civ_number)

    #Return the capital to the original variable
    return capital

###########################################
#STAT DISTRIBUTOR FUNCTION
###########################################

#Define a function that distributes stats based on each civ
def civ_stat_distributor(civ_number):
    #Begin an if statement to determine which starting stats each civ gets
    if civ_number == 1:
        #India starts at average science, production and high population
        science = 30
        production = 40
        population = 40

        #India's rate of increase for science and production is average
        science_ROI = 8
        production_ROI = 6

    #Begin an else if statement for Rome
    elif civ_number == 2:
        #Rome starts at high science, production and average population
        science = 40
        production = 60
        population = 26

        #Rome's rate of increase for science and production is low
        science_ROI = 5
        production_ROI = 4

    #Otherwise, use is America
    elif civ_number == 3:
        #America starts at poor science, production and average population
        science = 20
        production = 20
        population = 26

        #America's rate of increase for science and production is high
        science_ROI = 12
        production_ROI = 9

    #Make the resource value 0, assuming all civs start with no farmed resources
    resource = 0

    #Make the capital health 270, since each civ starts from the same amount
    capital_health = 270

    #Make the unit damage static across all civs
    unit_dmg = 20

    #Hold the civ's stats in a list of values
    civ_stats = [science, production, population, science_ROI, production_ROI, resource, capital_health, unit_dmg]

    #Return the list of stats to the original variable
    return civ_stats

###########################################
#SCIENCE FUNCTIONS
###########################################

#Define a function that prints which technologies the user can do and the era they're in
def tech_era_display(era):
    #Begin an if statement that will determine which era and technologies to display
    if era == 'stone':
        #Make the display message indicate the stone era
        era_display = '''STONE ERA
The available technologies in this era are Primitive Tools and Agriculture, which both increase your resource intake'''

    #Begin an else if statement if the user is in the metal era
    elif era == 'metal':
        #Make the display message indicate the metal era
        era_display = '''METAL ERA
The available technologies in this era are Weaponry, which increases your unit damage per unit and Metallurgy, which increases your capital health'''

    #Begin an else if statement if the user is in the medieval era
    elif era == 'medieval':
        #Make the display message indicate the medieval era
        era_display = '''MEDIEVAL ERA
The available technologies in this era are Feudalism, which increases your unit damage per unit and Religion, which increases your resource intake'''

    #Begin an else if statement if the user is in the Renaissance
    elif era == 'renaissance':
        #Make the display message indicate the Renaissance
        era_display = '''RENAISSANCE
The available technologies in this era are the Printing Press, which increases your capital health and the Hand Cannon, which increases your unit damage per unit'''

    #Begin an else if statement if the user is in the modern era
    elif era == 'modern':
        #Make the display message indicate the modern era
        era_display = '''MODERN ERA
The available technologies in this era are the Computer, which increases your resource intake and Military Aircraft, which increases your unit damage per unit'''

    #Otherwise, the user is in the post-modern era
    else:
        #Make the display message indicate the post-modern era
        era_display = '''POST-MODERN ERA
The available technologies in this era are AI, which you must start with, and allows you to begin building the first component for the spacecraft and Astronomy, which allows you to complete the spacecraft. COMPLETING ASTRONOMY WINS YOU THE GAME!'''

    #Display the pertinent about the era
    print(era_display)

    #Print space for clarity
    space()

######################################################################################
#NOTE: Each era input and checker is separate to allow for easier separation of era and tech per civ. Also gives the ability to use the same character multiple times, since the era and the specific tech letter are required for the important if statements. If one function that's a big if statement to determine the string in the input was used, and then a separate function to determine that user's input was used, then checking the entrance couldn't be done easily, since letting the user re-enter the input causes more issues with re-checking the entrance than this approach.
######################################################################################

    ###########################################
    #STONE ERA FUNCTIONS
    ###########################################

#Define a function that lets the user enter the technologies for the stone era
def stone_era_input():
    #Let the user enter the corresponding technology
    stone_tech = input('Enter "P" if you want to research Primitive Tools, "A" to research Agriculture, and "S" to print the science technology tree:\n')

    #Print space for clarity
    space()

    #Return the user's stone era tech choice to the original variable
    return stone_tech

#Define a function that checks the stone era inputs
def stone_era_check(tech_choice):
    #Begin a while loop that continues while the user's entrances are incorrect
    while tech_choice != 'P' and tech_choice != 'p' and tech_choice != 'A' and tech_choice != 'a' and tech_choice != 'S' and tech_choice != 's':
        #Notify user entrance is incorrect
        print('Please enter a valid letter for the stone era technologies')

        #Print space for clarity
        space()

        #Let the user re-enter their choice for the stone era
        tech_choice = stone_era_input()

    #Return the user's corrected choice of technology to the original variable
    return tech_choice

    ###########################################
    #METAL ERA FUNCTIONS
    ###########################################

#Define a function that lets the user enter the technologies for the metal era
def metal_era_input():
    #Let the user enter the corresponding technology
    metal_tech = input('Enter "W" if you want to research Weaponry , "M" to research Metallurgy, and "S" to print the science technology tree:\n')

    #Print space for clarity
    space()

    #Return the user's metal era tech choice to the original variable
    return metal_tech

#Define a function that checks the metal era inputs
def metal_era_check(tech_choice):
    #Begin a while loop that continues while the user's entrances are incorrect
    while tech_choice != 'W' and tech_choice != 'w' and tech_choice != 'M' and tech_choice != 'm' and tech_choice != 'S' and tech_choice != 's':
        #Notify user entrance is incorrect
        print('Please enter a valid letter for the metal era technologies')

        #Print space for clarity
        space()

        #Let the user re-enter their choice for the metal era
        tech_choice = metal_era_input()

    #Return the user's corrected choice of technology to the original variable
    return tech_choice

    ###########################################
    #MEDIEVAL ERA FUNCTIONS
    ###########################################

#Define a function that lets the user enter the technologies for the medieval era
def medieval_era_input():
    #Let the user enter the corresponding technology
    medieval_tech = input('Enter "F" if you want to research Feudalism , "R" to research Religion, and "S" to print the science technology tree:\n')

    #Print space for clarity
    space()

    #Return the user's medieval era tech choice to the original variable
    return medieval_tech

#Define a function that checks the medieval era inputs
def medieval_era_check(tech_choice):
    #Begin a while loop that continues while the user's entrances are incorrect
    while tech_choice != 'F' and tech_choice != 'f' and tech_choice != 'R' and tech_choice != 'r' and tech_choice != 'S' and tech_choice != 's':
        #Notify user entrance is incorrect
        print('Please enter a valid letter for the medieval era technologies')

        #Print space for clarity
        space()

        #Let the user re-enter their choice for the medieval era
        tech_choice = medieval_era_input()

    #Return the user's corrected choice of technology to the original variable
    return tech_choice

    ###########################################
    #RENAISSANCE FUNCTIONS
    ###########################################

#Define a function that lets the user enter the technologies for the renaissance
def renaissance_input():
    #Let the user enter the corresponding technology
    renaissance_tech = input('Enter "P" if you want to research Printing Press , "H" to research Hand Cannon, and "S" to print the science technology tree:\n')

    #Print space for clarity
    space()

    #Return the user's renaissance tech choice to the original variable
    return renaissance_tech

#Define a function that checks the renaissance inputs
def renaissance_check(tech_choice):
    #Begin a while loop that continues while the user's entrances are incorrect
    while tech_choice != 'P' and tech_choice != 'p' and tech_choice != 'H' and tech_choice != 'h' and tech_choice != 'S' and tech_choice != 's':
        #Notify user entrance is incorrect
        print('Please enter a valid letter for the renaissance technologies')

        #Print space for clarity
        space()

        #Let the user re-enter their choice for the renaissance
        tech_choice = renaissance_input()

    #Return the user's corrected choice of technology to the original variable
    return tech_choice

    ###########################################
    #MODERN ERA FUNCTIONS
    ###########################################

#Define a function that lets the user enter the technologies for the modern era
def modern_era_input():
    #Let the user enter the corresponding technology
    modern_era_tech = input('Enter "C" if you want to research Computers, "M" to research Military Aircrafts, and "S" to print the science technology tree:\n')

    #Print space for clarity
    space()

    #Return the user's modern era tech choice to the original variable
    return modern_era_tech

#Define a function that checks the modern era inputs
def modern_era_check(tech_choice):
    #Begin a while loop that continues while the user's entrances are incorrect
    while tech_choice != 'C' and tech_choice != 'c' and tech_choice != 'M' and tech_choice != 'm' and tech_choice != 'S' and tech_choice != 's':
        #Notify user entrance is incorrect
        print('Please enter a valid letter for the modern era technologies')

        #Print space for clarity
        space()

        #Let the user re-enter their choice for the modern era
        tech_choice = modern_era_input()

    #Return the user's corrected choice of technology to the original variable
    return tech_choice

###########################################
#DISPLAYING SCIENCE FUNCTIONS
###########################################

#Define a function that will display the tech tree
def tech_tree_display():
    #Display the tech tree to the user
    print('''Tech Tree

        STONE ERA                       METAL  ERA                    MEDIEVAL ERA                    RENAISSANCE                   MODERN  ERA                     POST-MODERN ERA
     Primitive Tools                     Weaponry                       Feudalism                    Printing Press                   Computer                            AI
Increases resource intake         Increases unit damage           Increases unit damage         Increases capital health      Increases resource intake       Required to begin spaceship
                          ----->                          ----->                         ----->                         ----->                         ----->
       Agriculture                      Metallurgy                      Religion                      Hand Cannon                 Military Aircrafts                   Astronomy
Increases resource intake        Increases capital health       Increases resource intake        Increases unit damage          Increases unit damage        Required to complete spaceship''')

    #Print space for clarity
    space()

#Define a function that determines if the user wanted the tech tree displayed
def displaying_tech_tree(user_input, era):
    #Determine if the user wanted to see the tech tree as their choice
    while user_input == "S":
        #Display the tech tree
        tech_tree_display()

        #Let the user re-enter their tech
        user_input = tech_determiner(era)

        #Capitalize the user's choice
        user_input = choice_capitalizer(user_input)

    #Return the user's useful input to the original variable
    return user_input

#Define a function that displays the info about the postmodern era, since they have no choice for the order of research
def postmodern_era_display():
    #Print a message notifying the user they're in the postmodern era
    print('You cannot make a choice for the two technologies in the postmodern era, you must start with AI and will then research Astronomy.')

    #Print a space for clarity
    space()

###########################################
#SCIENCE FUNCTIONS CONT'D
###########################################

#Define a function that determines which technology the user can pick at the current moment
def tech_determiner(era):
    #Begin an if statement that determines which era the user is in
    if era == 'stone':
        #Run the user through the corresponding era input and checker
        tech_choice = stone_era_input()

        #Verify the user's choice of tech
        tech_choice = stone_era_check(tech_choice)

    #Begin an else if statement for the metal era
    elif era == 'metal':
        #Run the user through the corresponding era input and checker
        tech_choice = metal_era_input()

        #Verify the user's choice of tech
        tech_choice = metal_era_check(tech_choice)

    #Begin an else if statement for the medieval era
    elif era == 'medieval':
        #Run the user through the corresponding era input and checker
        tech_choice = medieval_era_input()

        #Verify the user's choice of tech
        tech_choice = medieval_era_check(tech_choice)

    #Begin an else if statement for the renaissance
    elif era == 'renaissance':
        #Run the user through the corresponding era input and checker
        tech_choice = renaissance_input()

        #Verify the user's choice of tech
        tech_choice = renaissance_check(tech_choice)

    #Otherwise, the user is in the modern era
    elif era == 'modern':
        #Run the user through the corresponding era input and checker
        tech_choice = modern_era_input()

        #Verify the user's choice of tech
        tech_choice = modern_era_check(tech_choice)

    #Otherwise, user is in the endgame
    else:
        #Display info about the postmodern era
        postmodern_era_display()

        #The tech choice has to start with AI
        tech_choice = 'AI'

    #Return the tech choice to the original variable
    return tech_choice

#Define a function that determines the value of the tech, depending on the era it's from
def tech_cost_determiner(era):
    #Begin an if statement that determines the cost of the tech
    if era == 'stone':
        #If the civ is in the stone era, make the tech cost 150 research
        tech_cost = 150
    #Begin a set of else if statement if the civ is in either metal, medieval, renaissance, or modern era
    elif era == 'metal':
        #If the civ is in the metal era, make the tech cost 326 research
        tech_cost = 325
    elif era == 'medieval':
        #If the civ is in the medieval era, make the tech cost 500 research
        tech_cost = 500
    elif era == 'renaissance':
        #If the civ is in the renaissance era, make the tech cost 675 research
        tech_cost = 675
    elif era == 'modern':
        #If the civ is in the modern era, make the tech cost 150 research
        tech_cost = 850
    #Otherwise, civ is in the post-modern era, making the tech cost higher
    else:
        #If the civ is in the post-modern era, make the tech cost 1025 research
        tech_cost = 1025

    #Return the cost of the technology to the original variable
    return tech_cost

#Define a function that determines the number of turns researching a tech would take depending on the civ
def tech_turn_determiner(civ_stats, tech_cost):
    #Pull the science and population numbers from the list of civ stats
    science_points  = civ_stats[0]
    population = civ_stats[2]

    #Floor divide population to make the value more usable with the tech costs. this value just happened to allow for gameplay efforts to be even
    population = population // 6

    #Using the 2 previous values, determine the number of research points
    research_points = population + science_points

    #Using division again, determine the number of turns required for the civ to fully research a given tech
    turns_to_research = tech_cost / research_points

    #Round the number of turns to research so turn timers aren't too skewed
    turns_to_research = round(turns_to_research)

    #Return the number of turns to research
    return turns_to_research

#Define a function that changes the civs stats depending on the techs they have
def tech_civ_stats(tech, civ_stats, era):
    #Establish a set of variables that will be changed depending on the researched technology
    resource_multiplier = 1
    unit_dmg_increase = 0
    capital_health_increase = 0

    #Begin an if statement that determines which era the civ is in
    if era == 'stone':
        #Begin nested if statement to determine the effect the specific tech the user is researching has
        if tech == 'P' or tech == 'A':
            #Increase the resource multiplier
            resource_multiplier += 0.5
    #Begin else if statement if the civ was in the metal era
    elif era == 'metal':
        #Begin nested if statement to determine the effect the specific tech the user is researching has
        if tech == 'W':
            #Increase the amount of damage the units do
            unit_dmg_increase += 5
        #Otherwise, the user is researching the other tech
        else:
            #Increase the capital's health
            capital_health_increase += 150
    #Begin else if statement if the civ was in the medieval era
    elif era == 'medieval':
        #Begin nested if statement to determine the effect the specific tech the user is researching has
        if tech == 'F':
            #Increase the amount of damage the units do
            unit_dmg_increase += 5
        #Otherwise, the user is researching the other tech
        else:
            #Increase the resource multiplier
            resource_multiplier += 0.5
    #Begin else if statement if the civ was in the renaissance
    elif era == 'renaissance':
        #Begin nested if statement to determine the effect the specific tech the user is researching has
        if tech == 'P':
            #Increase the capital's health
            capital_health_increase += 150
        #Otherwise, the user is researching the other tech
        else:
            #Increase the amount of damage the units do
            unit_dmg_increase += 5
    #Begin else if statement if the civ was in the renaissance
    elif era == 'modern':
        #Begin nested if statement to determine the effect the specific tech the user is researching has
        if tech == 'C':
            #Increase the resource multiplier
            resource_multiplier += 0.5
        #Otherwise, the user is researching the other tech
        else:
            #Increase the amount of damage the units do
            unit_dmg_increase += 5

    #Otherwise, user is in endgame of science, run a function indicating that
    else:
        pass
    #Find and change values in the civ_stats list depending on the researched tech
    civ_stats[5] = civ_stats[5] * resource_multiplier
    civ_stats[6] += capital_health_increase
    civ_stats[7] += unit_dmg_increase


    #Return the new list of stats to the original variable
    return civ_stats

#Define a function that changes forces the civ to change the tech they're working on if they already researched one of them
def other_tech_switch(era, tech):
    #Begin an if statement that determines what is the other tech that the user must research
    if era == 'stone':
        #Begin nested if statement to determine the effect the specific tech the user is researching has
        if tech == 'P':
            #Change the technology to research
            tech = 'A'
        #Otherwise, change it to the other one
        else:
            #Change tech to research
            tech = 'P'
    #Begin else if statement if the civ was in the metal era
    elif era == 'metal':
        #Begin nested if statement to determine the effect the specific tech the user is researching has
        if tech == 'W':
            #Change the technology to research
            tech = 'M'
        #Otherwise, change it to the other one
        else:
            #Change tech to research
            tech = 'W'

    #Begin else if statement if the civ was in the medieval era
    elif era == 'medieval':
        #Begin nested if statement to determine the effect the specific tech the civ is researching has
        if tech == 'F':
            #Change the technology to research
            tech = 'R'
        #Otherwise, the civ is researching the other tech
        else:
            #Change the technology to research
            tech = 'F'

    #Begin else if statement if the civ was in the renaissance
    elif era == 'renaissance':
        #Begin nested if statement to determine the effect the specific tech the civ is researching has
        if tech == 'P':
            #Change the technology to research
            tech = 'H'
        #Otherwise, the civ is researching the other tech
        else:
            #Change the technology to research
            tech = 'P'

    #Begin else if statement if the civ was in the renaissance
    elif era == 'modern':
        #Begin nested if statement to determine the effect the specific tech the civ is researching has
        if tech == 'C':
            #Change the technology to research
            tech = 'M'
        #Otherwise, the civ is researching the other tech
        else:
            #Change the technology to research
            tech = 'C'

    #Otherwise, civ is in endgame of science, run a function indicating that
    else:
        #Begin nested if statement to determine the effect the specific tech the civ is researching has
        if tech == 'AI':
            #Change the technology to research
            tech = 'Astronomy'

    #Return the new tech the civ has to research
    return tech

#Define a function that determines the new era a civ will enter
def era_switcher(era):
    #Begin an if statement that determines what is the other tech that the user must research
    if era == 'stone':
        #Change the era the civ is in
        era = 'metal'
    elif era == 'metal':
        #Change the era the civ is in
        era = 'medieval'

    #Begin else if statement if the civ was in the medieval era
    elif era == 'medieval':
        #Change the era the civ is in
        era = 'renaissance'

    #Begin else if statement if the civ was in the renaissance
    elif era == 'renaissance':
            #Change the era the civ is in
            era = 'modern'

    #Begin else if statement if the civ was in the modern era
    elif era == 'modern':
        #Change the era the civ is in
        era = 'postmodern'

    #Return the era to the original variable
    return era

#Define a function that will create a variable to determine whether the civ is finished an era or not
def tech_era_determiner(tech_researched):
    #Determine the number of items researched
    number_techs = len(tech_researched)

    #Determine the number of techs left in the current era
    era_determiner = number_techs % 2

    #Return the era determiner to the original variable
    return era_determiner

#Define a function that notifies the user they are going to research the other tech
def other_tech_switch_notifier():
    #Print a statement that notifies them they're going to research the other tech
    print('You have researched one technology in this era, you will now research the other')

    #Print space for clarity
    space()

#Define a function, primarily made of several other functions that fully filters the user's choices
def fully_filtered_user_tech_choice(user_era):

    #Display the current era the user is in
    tech_era_display(user_era)

    #Determine which tech the user wants to research
    user_tech = tech_determiner(user_era)

    #Begin if statement in case the user's tech is in the post modern era (capitalization isn't needed)
    if user_tech != 'AI' and user_tech != 'Astronomy':

        #Capitalize the user's tech choice using
        user_tech = choice_capitalizer(user_tech)

    #Determine if the user wants to go display the tech tree
    user_tech = displaying_tech_tree(user_tech, user_era)

    #Return the user's fully filtered tech choice to the original variable
    return user_tech

#Define a function that gives the full version of a technology
def tech_name_expander(tech, era):

    #Begin an if statement for each era
    if era == 'stone':
        #Begin nested if statement to produce the tech intended to print
        if tech == 'P':
            #Establish the tech to print
            tech_to_print = 'Primitive Tools'
        #Otherwise, change it to the other one
        else:
            #Establish the tech to print
            tech_to_print = 'Agriculture'

    #Begin else if statement if the civ was in the metal era
    elif era == 'metal':
        #Begin nested if statement to produce the tech intended to print
        if tech == 'W':
            #Establish the tech to print
            tech_to_print = 'Weaponry'
        #Otherwise, change it to the other one
        else:
            #Establish the tech to print
            tech_to_print = 'Metallurgy'

    #Begin else if statement if the civ was in the medieval era
    elif era == 'medieval':
        #Begin nested if statement to produce the tech intended to print
        if tech == 'F':
            #Establish the tech to print
            tech_to_print = 'Feudalism'
        #Otherwise, change it to the other one
        else:
            #Establish the tech to print
            tech_to_print = 'Religion'

    #Begin else if statement if the civ was in the renaissance
    elif era == 'renaissance':
        #Begin nested if statement to produce the tech intended to print
        if tech == 'P':
            #Establish the tech to print
            tech_to_print = 'Printing Press'
        #Otherwise, change it to the other one
        else:
            #Establish the tech to print
            tech_to_print = 'Hand Cannon'

    #Begin else if statement if the civ was in the renaissance
    elif era == 'modern':
        #Begin nested if statement to produce the tech intended to print
        if tech == 'C':
            #Establish the tech to print
            tech_to_print = 'Computers'
        #Otherwise, change it to the other one
        else:
            #Establish the tech to print
            tech_to_print = 'Military Aircrafts'

    #Otherwise, civ is in endgame of science
    else:
        #In the last era, the tech to print is just the tech anyway
        tech_to_print = tech

    #Return the tech to print
    return tech_to_print

#Define a function that determines the turns left to do something
def turns_left_process(turn_process_finished, turn):
    #Subtract the two values to determine the turns left
    turns_left = turn_process_finished - turn

    #Return the number of turns left
    return turns_left

#Define a function that displays the number of turns left for researching a technology
def turns_left_to_research_display(tech_to_print, turns_left):
    #Establish string forms of the turns left variables
    turns_left = str(turns_left)

    #Hold the important info in a string variable to display
    turns_to_research_display = 'You are researching ' + tech_to_print + ' and you will finish in ' + turns_left + ' turns. (Press any key to continue.)\n'

    #Let the user input whatever, more so to let them see the map in between turns
    input(turns_to_research_display)

    #Print space for clarity
    space()

###########################################
#CPU SCIENCE FUNCTIONS
###########################################

#Define a function that determines which tech the cpu will research
def cpu_tech_choice(era):
    #Hold the result of a RNG to determine which tech the cpu will choose
    cpu_choice = random.randint(1,2)

    #Begin an if statement that determines which tech the cpu researches
    if era == 'stone':
        #Begin nested if statement for the era-specific tech choice the cpu has
        if cpu_choice == 1:
            #The cpu chooses the corresponding tech
            cpu_tech = 'P'
        #Otherwise, cpu researches other tech
        else:
            #The cpu chooses the corresponding tech
            cpu_tech = 'A'

    #Begin an else if statement for the metal era
    elif era == 'metal':
        #Begin nested if statement for the era-specific tech choice the cpu has
        if cpu_choice == 1:
            #The cpu chooses the corresponding tech
            cpu_tech = 'W'
        #Otherwise, cpu researches other tech
        else:
            #The cpu chooses the corresponding tech
            cpu_tech = 'M'

    #Begin an else if statement for the metal era
    elif era == 'medieval':
        #Begin nested if statement for the era-specific tech choice the cpu has
        if cpu_choice == 1:
            #The cpu chooses the corresponding tech
            cpu_tech = 'F'
        #Otherwise, cpu researches other tech
        else:
            #The cpu chooses the corresponding tech
            cpu_tech = 'R'

    #Begin an else if statement for the metal era
    elif era == 'renaissance':
        #Begin nested if statement for the era-specific tech choice the cpu has
        if cpu_choice == 1:
            #The cpu chooses the corresponding tech
            cpu_tech = 'P'
        #Otherwise, cpu researches other tech
        else:
            #The cpu chooses the corresponding tech
            cpu_tech = 'H'

    #Begin an else if statement for the metal era
    elif era == 'modern':
        #Begin nested if statement for the era-specific tech choice the cpu has
        if cpu_choice == 1:
            #The cpu chooses the corresponding tech
            cpu_tech = 'C'
        #Otherwise, cpu researches other tech
        else:
            #The cpu chooses the corresponding tech
            cpu_tech = 'M'

    #Otherwise, the cpu is in the post-modern era and doesn't have a choice
    else:
        #The cpu has to start with AI
        cpu_tech = 'AI'

    #Return the tech to the original variable
    return cpu_tech

###########################################
#USER PRODUCTION FUNCTIONS
###########################################

#Define a function that allows the user to enter what they want to produce
def user_production_choice():
    #Determine the user's choice of production
    production_choice = input('Enter what you would like your city to produce ("s" for a structure, "S" for a special structure, "U" for a unit, or "G" to bring up the tile guide.)\n')

    #Print space for clarity
    space()

    #Return the user's choice of production to the original variable
    return production_choice

#Define a function that checks the possible entrances for the production
def user_production_check_general(user_production):

    #While the user keeps entering incorrect
    while user_production != 's' and user_production != 'S' and user_production != 'u' and user_production != 'U' and user_production != 'g' and user_production != 'G':
        #Notify user their input is incorrect
        print('Please enter a valid production.')

        #space for clarity
        space()

        #Allow user to re-enter their production choice
        user_production = user_production_choice()

    #Return the chosen production to the user's original choice
    return user_production

#Define a function that runs through civs tiles to determine the tiles the structure can be built on
def structure_buildable_tiles(tile_info_dictionary, captured_territories, civ_number):
#Establish a variable that holds an empty list
    possible_structure_tiles = []
    #Begin a for loop that goes through all captured territories
    for tiles in captured_territories:

        #Begin an if statement going through the values in the dictionary for each tile key
        if tile_info_dictionary[tiles][1] == True and tile_info_dictionary[tiles][3] == False and tile_info_dictionary[tiles][7] == civ_number:

            #Add the possible tiles to build on to the list of tiles
            possible_structure_tiles.append(tiles)

    #Return the list of possible tiles to build on
    return possible_structure_tiles

#Define a function that determines whether a structure can be built
def structure_build_check(tile_info_dictionary, captured_territories, civ_number):

    #Run all the values through the structure_buildable_tiles() function to determine all the possible_structure_tiles the user can have
    possible_structure_tiles = structure_buildable_tiles(tile_info_dictionary, captured_territories, civ_number)

    #If there are no possible tiles to build on change the flag to false
    if possible_structure_tiles == []:
        #Change flag to false
        structure_possibility = False
    #Otherwise, there are values to build on so change the flag to true
    else:
        #Change flag to true
        structure_possibility = True

    #Return the flag for structure building
    return structure_possibility

#Define a function that checks whether a civ can produce special structures
def special_check(civ_number, era):
    #Begin an if statement to determine if the civ is in a valid era to start building special structures
    #India can build from medieval era onwards, Rome from the metal era onwards, america from modern era onwards
    if (civ_number == 1 and (era == 'stone' or era == 'metal')) or (civ_number == 2 and era == 'stone') or (civ_number == 3 and (era != 'modern' or era != 'postmodern')):
        #Establish a flag indicating that a special structure can't be built
        special_possibility = False

    #Otherwise, make the flag false
    else:
        #Establish a flag that indicates a structure can be built
        special_possibility = True

    #Return the flag for the special structure's possibility
    return special_possibility

#Define a function that checks the user's entrance from a gameplay perspective
def user_production_check_specific(user_production, structure_possibility, special_possibility):
    #Begin an if statement that determines if it's possible to place a structure in the first place and whether it's possible to build the special structure they're trying to build
    while (user_production == 'S' and special_possibility == False) or ((user_production == 's' or user_production == 'S') and structure_possibility == False):
        #Notify the user they can't produce a structure
        print('You have no available tiles to build a structure on, or you are not at the right era to produce a special structure.')

        #Print space for clarity
        space()

        #Allow user to re-enter a production
        user_production = user_production_choice()

        #Check the user's entrance with a basic checker
        user_production = user_production_check_general(user_production)

        #No need to put the entrance through other checks, since the user's buildability status can't change mid selection

    #Return the corrected choice of user_production
    return user_production

#Define a function that determines the cost of a production
def production_cost_determiner(era, production):
    #Begin an if statement for each era
    if era == 'stone':
        #Begin nested if statement to produce the cost of the selected product
        if production == 's':
            #Establish the cost of the product in this era
            production_cost = 100
        #Otherwise, change it to the other one
        else:
            #Establish the cost of the product in this era
            production_cost = 130

    #Begin else if statement if the civ was in the metal era
    elif era == 'metal':
        #Begin nested if statement to produce the cost of the selected product
        if production == 's':
            #Establish the cost of the product in this era
            production_cost = 200
        #Begin else if statement if the civ wants to build a special structure
        elif production == 'S':
        #Establish cost of this item
            production_cost = 300
        #Otherwise, change it to the other one
        else:
            #Establish the cost of the product in this era
            production_cost = 250

    #Begin else if statement if the civ was in the medieval era
    elif era == 'medieval':
        #Begin nested if statement to produce the cost of the selected product
        if production == 's':
            #Establish the cost of the product in this era
            production_cost = 300
        #Begin else if statement if the civ wants to build a special structure
        elif production == 'S':
        #Establish cost of this item
            production_cost = 400
        #Otherwise, change it to the other one
        else:
            #Establish the cost of the product in this era
            production_cost = 370

    #Begin else if statement if the civ was in the renaissance
    elif era == 'renaissance':
        #Begin nested if statement to produce the cost of the selected product
        if production == 's':
            #Establish the cost of the product in this era
            production_cost = 400
        #Begin else if statement if the civ wants to build a special structure
        elif production == 'S':
        #Establish cost of this item
            production_cost = 500
        #Otherwise, change it to the other one
        else:
            #Establish the cost of the product in this era
            production_cost = 490

    #Begin else if statement if the civ was in the renaissance
    elif era == 'modern':
        #Begin nested if statement to produce the cost of the selected product
        if production == 's':
            #Establish the cost of the product in this era
            production_cost = 500
        #Begin else if statement if the civ wants to build a special structure
        elif production == 'S':
        #Establish cost of this item
            production_cost = 600
        #Otherwise, change it to the other one
        else:
            #Establish the cost of the product in this era
            production_cost = 610

    #Otherwise, civ is in endgame of science
    else:
        #Begin nested if statement to produce the cost of the selected product
        if production == 's':
            #Establish the cost of the product in this era
            production_cost = 600
        #Begin else if statement if the civ wants to build a special structure
        elif production == 'S':
        #Establish cost of this item
            production_cost = 700
        #Otherwise, change it to the other one
        else:
            #Establish the cost of the product in this era
            production_cost = 730

    #Return the cost of the production to the original variable
    return production_cost

#Define a function that determines the turn by which the product is done
def turn_product_finishes_determiner(civ_stats, product_cost):
    #Index the production of the civ by going through its list of stats
    production = civ_stats[1]

    #Divide the cost by the production amount to determine total turns
    turns_to_produce = product_cost / production

    #Round the number of turns so it makes more sense
    turns_to_produce = round(turns_to_produce)

    #Return the number of turns to produce the product to the original variable
    return turns_to_produce

#Define a function that adds a structure to a civ's list of structures
def structure_displayer(tile_info_dictionary, captured_tiles, civ_number, product):
    #Run the information through a function that determines the possible tiles to build on
    possible_structure_tiles = structure_buildable_tiles(tile_info_dictionary, captured_tiles, civ_number)

    #Take the first item from the index of possible structure tiles
    structure_tile = possible_structure_tiles[0]

    #Change the structure status of the corresponding tile value in the dictionary
    tile_info_dictionary[structure_tile][3] = True

    #Also change the other value if a special structure is present
    if product == 'S':
        #Change the structure status of the corresponding tile value in the dictionary
        tile_info_dictionary[structure_tile][9] = True

    #Return the structure tile to the original variable
    return structure_tile

#Define a function that will actually add the structure tile to the civs set of owned structures
def structure_builder(structure_tile, civs_structure_tiles, civ_stats, user_production):
    #Add the tile to a civ's set structure list
    civs_structure_tiles.append(structure_tile)

    #Hold the resource amount of the civ in a variable
    resource = civ_stats[5]

    #Change the resource value of the civ's corresponding stats
    resource += 3

    #If the user is producing a special structure, increase the resource value even more
    if user_production == 'S':
        #Increase the resources even more so
        resource += 2

    #Change the value of the resource in the stats list
    civ_stats[5] = resource

#Define a function that indicates a unit should be placed at a civ's capital
def unit_initiator(tile_info_dictionary, captured_tiles, civ_number, civ_unit_tiles):
    #Index the first item in the list of captured tiles to determine the civ's capital
    capital = captured_tiles[0]

    #Change the corresponding tile's unit value in the tile dictionary
    tile_info_dictionary[capital][4] = True

    #Also change the ownership of that unit in the tile key's value
    tile_info_dictionary[capital][5] = civ_number

    #Add the capital to the list indicating unit locations
    civ_unit_tiles.append(capital)

#Define a function that determines the full name of a user's production`
def product_name_expander(product):
    #Begin an if statement to determine which product to return
    if product == 's':
        #The product is a structre
        product_name = 'Structure'
    #Begin an else if statement if the product is a special structure
    elif product == 'S':
        #The product is a special structure
        product_name = 'Special Structure'
    #Otherwise, the product is a unit
    else:
        #The product is a unit
        product_name = 'Unit'

    #Return the name of the product to the original variable
    return product_name

#Define a function that displays the time to produce and the specfic name of a product
def turns_left_to_produce_display(turns_left, product):
    #Change the class of the turns left to print in a string
    turns_left = str(turns_left)

    #Hold the information for the product
    turns_left_to_produce = 'You are making a ' + product + ' and will finish it in ' + turns_left + ' turns. (Press any key to continue.)\n'

    #Let the user input whatever, more so to let them see the map in between turns
    input(turns_left_to_produce)

    #Print a space for clarity
    space()

#Define a function that displays a tile guide to the map
def tile_guide_display(user_production, structure_possibility, special_possibility):
    #Establish a variable to hold the tile guide in
    tile_guide = '''
    C - Your capital (regardless of selected civ)
    c - Your territory (regardless of selected civ)
    u - your unit (regardless of selected civ)
    r - unfarmed resource
    R - farmed resource
    S - farmed resource by a special building
    J - Roman capital
    j - Roman territory
    l - Roman unit
    G - Indian capital
    g - Indian territory
    i - Indian unit
    W - American capital
    w - American territory
    a - american unit
    x - an undiscovered tile

    In each tile, the information is shown in order of Ownership, Resource Status, and Unit Presence, for example, a captured tile owned by you, with a special building, and your unit looks like
    =====
    |   |
    |cSu|
    |   |
    ====='''

    #Begin a while loop that continues while the user keeps entering entrances indicating they want to see tile_guide
    while user_production == 'g' or user_production == 'G':
        #Display the tile guide
        print(tile_guide)

        #Let the user re-enter their production choice
        user_production = user_production_choice()

        #Verify the user's choice generally
        user_production = user_production_check_general(user_production)

        #Verify the user's choice on a per civ basis (specifically)
        user_production = user_production_check_specific(user_production, structure_possibility, special_possibility)

    #Return the verified and complete production choice
    return user_production

###########################################
#CPU PRODUCTION FUNCTIONS
###########################################

#Define a function that indicates which production the cpu will make
def cpu_production_decider(tile_info_dictionary, captured_territories, civ_number, era):
    #Hold a random number to determine which production the civ will produce
    cpu_production = random.randint(1,5)

    #Hold a flag of the civ's ability to build a structure
    structure_buildability = structure_build_check(tile_info_dictionary, captured_territories, civ_number)

    #Hold a flag of the civ's ability to build a special structure
    special_buildability = special_check(civ_number, era)

    #Begin an if statement to determine if the civ can build a structure at all
    if structure_buildability == False:
        #The civ can only produce units
        cpu_production = 'U'

    #otherwise, determine odds
    else:
        #Establish the odds of the civ building just a structure or a unit
        if civ_number == 1:
            #Determine the odds of producing a unit or a structure if the civ is india (about 50/50)
            if cpu_production == 2 or cpu_production == 5:
                #Make the production a unit
                cpu_production = 'U'
            #Otherwise, india produces a structure
            else:
                #Make the production a structure
                cpu_production = 's'

        #Begin else if statement if the civ is rome
        elif civ_number == 2:
            #Determine the odds of producing a unit or a structure if the civ is rome (about 20/80)
            if cpu_production == 2:
                #Make the production a unit
                cpu_production = 'U'
            #Otherwise, india produces a structure
            else:
                #Make the production a structure
                cpu_production = 's'

        #Otherwise, the civ is america
        else:
            #Determine the odds of producing a unit or a structure if the civ is america (about 80/20)
            if cpu_production == 5:
                #Make the production a unit
                cpu_production = 's'
            #Otherwise, india produces a unit
            else:
                #Make the production a unit
                cpu_production = 'U'
    #If the civ can produce a special structure and is going to produce a structure, make them produce a special structure
    if special_buildability == True and cpu_production == 's':
        #Change the production to a special structure
        cpu_production = 'S'

    #Return the production to the original variable
    return cpu_production

###########################################
#UNIT FUNCTIONS
###########################################

#Define a function that takes a user's unit moving input
def unit_move_choice(unit_position):
    #Convert the position to a string to allow for the input function
    unit_position_print = str(unit_position)
    #Let the user enter their unit instruction
    unit_info = input('Enter the direction, then the number of spots you want the unit at tile ' + unit_position_print + ' to move ("U" moves up, "D" moves down, "L" moves left, and "R" moves right. S, with nothing following it indicates no movement. E.g. "U2" moves that unit up 2 spaces)\n')

    #Input space for clarity
    space()

    #Return the unit instruction to the original variable
    return unit_info

#Define a function that determines if the number of spaces is fair, considering the corresponding civ's era
def space_number_check(era, space):
    #Determine which era the civ is in
    if era == 'stone' or era == 'metal':
        #Change a flag's status to indicate that they are entering a valid or invalid number of spaces
        if space > 2 or space < 0:
            #Make the flag true
            invalid_space_flag = True
        #Otherwise, the number of spaces is valid
        else:
            #Make the flag false
            invalid_space_flag = False

    #Begin else if statement for the middle 2 eras
    elif era == 'medieval' or era == 'renaissance':
        #Change a flag's status to indicate that they are entering a valid or invalid number of spaces
        if space > 3 or space < 0:
            #Make the flag true
            invalid_space_flag = True
        #Otherwise, the number of spaces is valid
        else:
            #Make the flag false
            invalid_space_flag = False
    #Otherwise, the civ is in the last two eras
    else:
        #Change a flag's status to indicate that they are entering a valid or invalid number of spaces
        if space > 4 or space < 0:
            #Make the flag true
            invalid_space_flag = True
        #Otherwise, the number of spaces is valid
        else:
            #Make the flag false
            invalid_space_flag = False

    #Return the flag to the original variable
    return invalid_space_flag

#Define a function that determines if the direction is allowed or not
def unit_move_direction_check(direction, unit_position):
    #Determine if the direction is valid at all
    if direction != 'U' and direction != 'u' and direction != 'D' and direction != 'd' and direction != 'L' and direction != 'l' and direction != 'R' and direction != 'r' and direction != 'S' and direction != 's':
        #Establish the invalid direction flag as true  since it's invalid
        invalid_direction_flag = True
    #Otherwise, the direction is at least allowed
    else:
        #Establish the invalid direction flag as false since it's invalid
        invalid_direction_flag = False

    #Return the flag to the original variable
    return invalid_direction_flag

#Define a function that determines if the direction is allowed, from a gameplay perspective
def unit_move_map_border_check(unit_position, end_location, order):
    #Take the direction from the order
    direction = order[0]
    #Establish variables to check whether the ending location of the unit makes sense with the unit order (border checking essentially)
    row_switch_check = end_location % 10
    row_switch_check_start = unit_position % 10

    #Begin an if statement to determine if the ending location is valid
    if (end_location < 1 or end_location > 100) or ((direction == 'L' or direction == 'l') and (((row_switch_check > row_switch_check_start) or (row_switch_check == 0)) and (row_switch_check_start != 0))) or ((direction == 'R' or direction == 'r') and (((row_switch_check < row_switch_check_start) or (row_switch_check_start == 0)) and (row_switch_check_start != 1))):
        #Establish a flag that indicates the location is invalid
        invalid_movement_gameplay_flag = True
    #Otherwise, the movement should be fine
    else:
        #Make the flag false to indicate no issues
        invalid_movement_gameplay_flag = False

    #Return the flag's status
    return invalid_movement_gameplay_flag

#Define a function that checks the entrance using an IndexError catcher
def order_indexer_check(order, unit_position):
    #Begin secondary while loop that continues while the nested try except is true
    #This while loop is only written this way (particularly the while True: fashion of while statement) due to assignment restrictions
    while True:
        #Begin try except statement
        try:
            #Index the choice for the direction and the number of spaces
            direction = order[0]

            #Only search for the second item if the direction isn't indicating the unit to stay
            if direction != 'S' and direction != 's':
                spaces = order[1]

            #Break the loop
            break
        #Begin except statement for index errors
        except IndexError:
            #Display a statement that explains the user's error
            print('Please enter at least two items in the set of orders, unless the unit stays in place (then just enter "S").')

            #Print space for clarity
            space()

            #Let the user re-enter their movement
            order = unit_move_choice(unit_position)

    #Determine if the user is staying put or not
    if direction == 'S' or direction == 's':
        #If the user is, only the direction can be put in the list
        order = [direction]
    #Otherwise, let the order be made up of direction and number of spaces
    else:
        #Make the order made up of direction and number of spaces
        order = [direction, spaces]

    #Return the order to the original variable
    return order

#Define a function that checks whether the unit is colliding with their own civs unit, or their capital, or a capital of a country they aren't at war with
def collision_check(tile_info_dictionary, unit_position, end_location, civ_number, war_info):
    #Begin an if statement that checks the values of the tile in the dictionary
    if ((unit_position != end_location) and (tile_info_dictionary[end_location][4] == True and tile_info_dictionary[end_location][5] == civ_number)) or (tile_info_dictionary[end_location][2] == True and tile_info_dictionary[end_location][7] == civ_number) or (war_info == [] and tile_info_dictionary[end_location][2] == True):
        #Make a flag indicating that the unit will collide with either their own capital, or their own unit
        collision_check_flag  = True
    #Otherwise, the unit has no collision issues
    else:
        #Make a flag indicating that
        collision_check_flag = False

    #Return the flag to the original variable
    return collision_check_flag

#Define a function that checks a user's entrance
def unit_move_choice_check(era, orders, unit_position, tile_info_dictionary, civ_number):
    #Check the order length
    orders = order_indexer_check(orders, unit_position)

    #Index the orders for the first instance, which should be the direction
    direction = orders[0]

    #Determine if the direction is to stop or not
    if direction != 'S' and direction != 's':
        #Index the orders for the second instance, which should be the number of spaces
        spaces = orders[1]

        #Determine whether the number of spaces is a valid entrance
        spaces_flag = spaces.isdigit()

        #if the spaces value is not a number, the number_spaces_flag() function gives an error, so avoid this entirely (and skip the other function since user's input is already wrong)
        if spaces_flag == True:
            #Change the value of the order to an integer for following function
            spaces = int(spaces)

            #Determine whether the number of spaces is valid from the point of the civ's era
            number_spaces_flag = space_number_check(era, spaces)

            #Determine whether the direction is invalid or not
            direction_flag = unit_move_direction_check(direction, unit_position)
        #Otherwise, change the flags to False since the loop will already be triggered
        else:
            number_spaces_flag = False
            direction_flag = False

        #Check the direction using a while loop
        #Have to keep this in this function so that the direction, number of spaces, and type of spaces entrance can be infinitely checked
        while number_spaces_flag == True or direction_flag == True or spaces_flag == False:
            #Notify user this is an incorrect entrance
            print('Please enter a valid order.')

            #Print space for clarity
            space()

            #Let the user re-enter their order
            orders = unit_move_choice(unit_position)

            #Check the order length
            orders = order_indexer_check(orders, unit_position)

            #Index the orders for the first instance, which should be the direction
            direction = orders[0]

            #Determine if the direction is to stop or not
            if direction != 'S' and direction != 's':

                #Index the orders for the second instance, which should be the number of spaces
                spaces = orders[1]

                #Determine whether the number of spaces is a valid entrance
                spaces_flag = spaces.isdigit()

                #if the spaces value is not a number, the number_spaces_flag() function gives an error, so avoid this entirely (and skip the other function since user's input is already wrong)
                if spaces_flag == True:
                    #Change the value of the order to an integer for following function
                    spaces = int(spaces)

                    #Determine whether the number of spaces is valid from the point of the civ's era
                    number_spaces_flag = space_number_check(era, spaces)

                    #Determine whether the direction is invalid or not
                    direction_flag = unit_move_direction_check(direction, unit_position)

                #Otherwise, change the flags to False since the loop will already be triggered
                else:
                    number_spaces_flag = False
                    direction_flag = False



            #Otherwise, make all the flag's false
            else:
                #Make all the flags false so that the loop stops
                number_spaces_flag = False
                direction_flag = False

    #Pop the direction, Capitalize the direction order, then return it to the same position in the orders list
    direction = orders.pop(0)
    direction =  choice_capitalizer(direction)
    orders.insert(0, direction)

    #If the user did not stop, they must have moved a number of spaces
    if direction != 'S':
        #Determine the number and pop it
        spaces = orders.pop(1)
        #Convert it to an integer
        spaces = int(spaces)
        #Insert the space back to its position in the orders list
        orders.insert(1, spaces)

    #Return the checked orders to the original variable
    return orders

#Define a function that determines if the civ entered another civ's territory
def unit_territory_war_check(unit_location_list, tile_info_dictionary):
    #Assume no war happens
    war_info = []

    #Begin a for loop for each unit in the unit_location_list
    for unit in unit_location_list:
        #Determine the owner of the unit
        unit_owner = tile_info_dictionary[unit][5]
        #Determine the owner of the tile
        tile_owner = tile_info_dictionary[unit][7]

        #Determine if the civ is trespassing on another civ's territory
        if unit_owner != tile_owner and tile_owner != 0:
            #Update the war info list to notify who is declaring war on who
            war_info = [unit_owner, tile_owner]

    #Return the info indicating war
    return war_info

#Define a function that determines if the civ is already at war
def war_check(war_info, location_to_be, unit_position, tile_info_dictionary):

    #Determine the owner of the unit in the current position
    unit_owner = tile_info_dictionary[unit_position][5]

    #Determine the owner of the tile
    tile_owner = tile_info_dictionary[location_to_be][7]

    #Determine if the civ is trespassing on another civ's territory
    if unit_owner != tile_owner and tile_owner != 0:
        #Hold whether war would happen in a variable
        war_info_check = [unit_owner, tile_owner]
    #Otherwise, keep the check empty
    else:
        war_info_check = []

    #Determine whether this if statement needs to be run through at all
    if war_info != []:

        #Determine if stepping into the territory will put the user at war with a different civ
        if war_info_check != [] and war_info != war_info_check:
            #Indicate that the civ is trying to do two wars
            two_war_check_flag = True
        #Otherwise, the flag is false`
        else:
            #Indicate that the civ's war attempt is fine
            two_war_check_flag = False

    #Otherwise, the flag is false
    else:
        #Indicate that the civ's war attempt is fine
        two_war_check_flag = False


    #Return the flag to the original variable
    return two_war_check_flag

#Define a function that moves a unit
def unit_mover(order, civ_number, unit_location):
    #Take the direction from the order
    direction = order[0]

    #Begin an if statement that determines if the unit moves or not
    if direction != 'S':
        #Take the number of spaces from the order
        spaces = order[1]

        #Begin an if statement depending on which orders the unit has
        if direction == 'U':
            #Multiply the number of spaces so that the unit moves an accurate number of spaces
            spaces = spaces * -10

        #Begin an else if statement if the direction is down
        elif direction == 'D':
            #Multiply the number of spaces so that the unit moves an accurate number of spaces
            spaces = spaces * 10

        #Begin an else if statement if the direction is left
        elif direction == 'L':
            #Multiply the number of spaces so that the unit moves an accurate number of spaces
            spaces = spaces * -1

        #If the direction is right, the spaces don't have to change at all

        #Change the position of the unit
        new_location = unit_location + spaces
    #Otherwise, the unit's position doesn't change
    else:
        #Don't change the unit_position
        new_location = unit_location

    #Return the location to the original variable
    return new_location

#Define a function that specifically checks a units final position
def unit_move_choice_check_specific(era, orders, unit_position, end_position, tile_info_dictionary, civ_number, war_info):
    #Take the direction from the orders
    direction = orders[0]

    #If the choice is to stay, skip all of this pretty much
    if direction != 'S':
        #Select the number of spaces from the orders
        spaces = orders[1]

        #Determine whether the number of units is valid from the map perspective
        map_movement_flag = unit_move_map_border_check(unit_position, end_position, orders)

        #Determine if the map_movement_flag is already true, since if so, the tile info dictionary can't be searched with something below 0 or above 100
        if map_movement_flag != True:
            #Determine whether the civ is trying to wage two wars
            two_war_check_flag = war_check(war_info, end_position, unit_position, tile_info_dictionary)
        #Otherwise, just make assign a value to the flag so that the while loop doesn't result in an error
        else:
            #Make the flag false
            two_war_check_flag = False

    #Otherwise, make the map movement flag false
    else:
        #Change the flags' status'
        map_movement_flag = False
        two_war_check_flag = False
        #Determine whether the unit will collide with its own units
        collision_flag = collision_check(tile_info_dictionary, unit_position, end_position, civ_number, war_info)


    #Determine if the map_movement_flag is already true, since if so, the tile info dictionary can't be searched with something below 0 or above 100
    if map_movement_flag != True:
        #Determine whether the unit will collide with its own units
        collision_flag = collision_check(tile_info_dictionary, unit_position, end_position, civ_number, war_info)
    #Otherwise, just make assign a value to the flag so that the while loop doesn't result in an error
    else:
        #Make the flag false
        collision_flag = False

    #Begin a while loop that runs for both flags
    while map_movement_flag == True or collision_flag == True or two_war_check_flag == True:
        #Notify the user their entrance is invalid
        print('Please enter a valid number. You are either going too far on the map, colliding with one of your own units/capital, attacking a capital before waging war, or trying to wage two wars.')

        #Print space for clarity
        space()

        #Determine the unit's orders again
        orders = unit_move_choice(unit_position)

        #Check the unit's orders again
        orders = unit_move_choice_check(era, orders, unit_position, tile_info_dictionary, civ_number)

        #Take the direction from the order
        direction = orders[0]

        #If the user inputs stopping as its order, stop the loop
        if direction != 'S' and direction != 's':

            #Select the number of spaces from the orders
            spaces = orders[1]

            #Determine the new end position
            end_position = unit_mover(orders, civ_number, unit_position)

            #Determine whether the number of units is valid from the map perspective
            map_movement_flag = unit_move_map_border_check(unit_position, end_position, orders)

            #Determine if the map_movement_flag is already true, since if so, the tile info dictionary can't be searched with something below 0 or above 100
            if map_movement_flag != True:
                #Determine whether the civ is trying to wage two wars
                two_war_check_flag = war_check(war_info, end_position, unit_position, tile_info_dictionary)
            #Otherwise, just make assign a value to the flag so that the while loop doesn't result in an error
            else:
                #Make the flag false
                two_war_check_flag = False

        #Otherwise, stop the loop
        else:
            #Change the flags so that the loop stops
            map_movement_flag = False
            two_war_check_flag = False
            #Determine whether the unit will collide with its own units
            collision_flag = collision_check(tile_info_dictionary, unit_position, end_position, civ_number, war_info)

        #Determine if the map_movement_flag is already true, since if so, the tile info dictionary can't be searched with something below 0 or above 100
        if map_movement_flag != True:
            #Determine whether the unit will collide with its own units
            collision_flag = collision_check(tile_info_dictionary, unit_position, end_position, civ_number, war_info)
        #Otherwise, just make assign a value to the flag so that the while loop doesn't result in an error
        else:
            #Make the flag false
            collision_flag = False

    #Return the order to the original variable
    return orders

#Define a function that changes the dictionary values of the units locations
def dictionary_unit_clearer(tile_info_dictionary, unit_location, civ_number):
    #Change the corresponding values in the tile_info_dictionary to indicate that the unit is gone
    tile_info_dictionary[unit_location][4] = False
    tile_info_dictionary[unit_location][5] = 0

#Define a function for what happens when 2 units collide
def unit_collision_case(possible_unit_tiles, stat_dictionary, tile_info_dictionary, civ_number, current_unit_tile):
    #Establish a tiebreaker variable
    tie_breaker = random.randint(1,2)

    #Determine if there is a unit already present
    if tile_info_dictionary[possible_unit_tiles][4] == True:

        #Determine if the tile is also a capital
        if tile_info_dictionary[possible_unit_tiles][2] != True:
            #Take the civ's number
            enemy_civ_number = tile_info_dictionary[possible_unit_tiles][5]

            #Take the damage that the civ does
            enemy_unit_dmg = stat_dictionary[enemy_civ_number][7]

            #Determine the allied unit's damage
            allied_unit_dmg = stat_dictionary[civ_number][7]

            #Determine the winner of the fight
            if enemy_unit_dmg > allied_unit_dmg:
                #Change the tile info to indicate the winner
                tile_info_dictionary[possible_unit_tiles][5] = enemy_civ_number

            #Begin an else if statement if the allied unit did more damage
            elif enemy_unit_dmg < allied_unit_dmg:
                #Change the tile info to indicate the winner
                tile_info_dictionary[possible_unit_tiles][5] = civ_number

            #Otherwise, the fight is a tie, so the winner is determined randomly
            else:
                #Begin another if statement to determine who wins
                if tie_breaker == 1:
                    #In this case, the allied unit loses
                    tile_info_dictionary[possible_unit_tiles][5] = enemy_civ_number

                #Otherwise, the allied unit wins
                else:
                    #Change the tile info to indicate the winner
                    tile_info_dictionary[possible_unit_tiles][5] = civ_number


        #Otherwise, switch the tiles regularly
        else:
            #Change the dictionary info to indicate the unit successfully moved
            tile_info_dictionary[current_unit_tile][4] = True
            tile_info_dictionary[current_unit_tile][5] = civ_number

    #Otherwise, switch the tiles regularly
    else:
        #Change the dictionary info to indicate the unit successfully moved
        tile_info_dictionary[possible_unit_tiles][4] = True
        tile_info_dictionary[possible_unit_tiles][5] = civ_number

#Define a function for the unit's movement when they attack a capital
def capital_siege_determiner(tile_info_dictionary, territory_civ_numbers_dict, war_info, end_location):
    #Determine the number of the warmonger and the defender
    warmonger = war_info[0]
    defender = war_info[1]

    #Establish a variable to determine the position of the opposing capital
    capital = territory_civ_numbers_dict[defender][0]

    #Assume the civ doesn't hit the capital
    capital_hit_flag = False

    #Determine if the unit is moving at the capital
    if end_location == capital:
        #If so, hit the capital
        capital_hit_flag = True

    #Return the validity of the capital hit
    return capital_hit_flag

#Define a function that hits the capital
def capital_siege(tile_info_dictionary, war_info, stat_civ_numbers_dict, capital_hit_flag):
    #Determine the number of the warmonger and the defender
    warmonger = war_info[0]
    defender = war_info[1]

    #Determine the corresponding capital health and unit damage values
    capital_health = stat_civ_numbers_dict[defender][6]
    unit_dmg = stat_civ_numbers_dict[warmonger][7]

    #Begin an if statement that runs if the unit hits the capital
    if capital_hit_flag == True:
        #Determine the new capital health amount
        capital_health -= unit_dmg

    #Move the capital health back to its original variable
    stat_civ_numbers_dict[defender][6] = capital_health

#Define a function that resets the unit positions back from their positions if they hit the capital
def capital_position_reset(capital_hit_flag, end_location, start_location):
    #Determine if the unit hit the capital at all
    if capital_hit_flag == True:
        #Make the ending location become the starting location, so that the unit can't stay in the capital
        end_location = start_location

    #Return the new ending location to the original variable
    return end_location

#Define a function that determines the field of vision of the user after a unit moves
def tiles_to_make_visibile(ending_location, territory_civ_numbers_dict, tile_info_dictionary):

    #All the tiles in the unit's vicinity should be visible
    up_visible = ending_location - 10
    down_visible = ending_location + 10
    left_visible = ending_location - 1
    right_visible = ending_location + 1

    #Make an empty list to fill with tiles that have units in them
    unit_filled_tiles = []

    #Establish an empty list for now, that can be made more full depending on what the user sees
    controlled_tiles_to_make_visible = []

    #Establish a list for the tiles to be made visible
    tiles_to_be_visible = [ending_location, up_visible, down_visible, left_visible, right_visible]

    #Establish a variable to index a list
    index = 0

    #Make a tupled version of tiles_to_be_visible to iterate
    tupled_tiles_to_be_visible = tuple(tiles_to_be_visible)

    ####################################################################################
    #This is essentially the same as the area_expansion_check() function but
    #the difference in tile_info_dictionary usage allows it to be specifically used for
    #visibility determinations
    ####################################################################################

    #Begin a for loop for each tile  in the tuple
    for tiles in tupled_tiles_to_be_visible:
        #Establish two variables to determine if the tile to view is on the wrong side to view
        side_test = ending_location % 10
        side_test2 = tiles % 10

        #Establish an if statement that determines if the tile is off the map or not, if it is, delete it from the list
        if (tiles < 1 or tiles > 100) or (side_test == 0 and side_test2 == 1) or (side_test == 1 and side_test2 == 0):
            del(tiles_to_be_visible[index])
        #Otherwise, increase the index by 1 so it keeps up
        else:
            #Increase index
            index += 1

    #Begin a for loop to determine if the user sees another civ
    for tiles in tiles_to_be_visible:

        #Determine if the units see a captured tile
        if tile_info_dictionary[tiles][6] == True:
            #Hold the owners civ_number
            civ_number = tile_info_dictionary[tiles][7]

            #Determine a list of controlled_tiles_to_make_visible
            controlled_tiles_to_make_visible += territory_civ_numbers_dict[civ_number]

    #Add the two lists together
    tiles_to_be_visible += controlled_tiles_to_make_visible

    #Change the visibility of all the tiles to make visible now
    for tiles in tiles_to_be_visible:

        #Change all the tiles to be visible
        tile_info_dictionary[tiles][0] = False

#Define a function that assigns a move order to each unit in the civs unit list
def unit_move_receiver(civ_unit_tiles, era, tile_info_dictionary, civ_number, stat_dictionary, territory_civ_numbers_dict, war_info):
    #Establish an empty list for the following loop
    new_unit_locations = []

    #Begin a for loop that goes through each item in the tiles to determine the new location  of each unit
    for unit in civ_unit_tiles:
        #Run the user through the unit choice receiver function
        orders = unit_move_choice(unit)

        #Run the user through a checking function that verifies whether their movement is valid
        orders = unit_move_choice_check(era, orders, unit, tile_info_dictionary, civ_number)

        #Determine the possible new location, now that the order is partially allowed
        new_location = unit_mover(orders, civ_number, unit)

        #Run the user through a checking function that checks the order based on its end_location validity
        orders = unit_move_choice_check_specific(era, orders, unit, new_location, tile_info_dictionary, civ_number, war_info)

        #Determine the new location, now that the order is partially allowed
        new_location = unit_mover(orders, civ_number, unit)

        #Determine if war moves need to be made
        if war_info != []:
            #Determine if the unit hits the capital
            capital_hit_flag = capital_siege_determiner(tile_info_dictionary, territory_civ_numbers_dict, war_info, new_location)

            #Remove capital health if the unit hits the capital
            capital_siege(tile_info_dictionary, war_info, stat_dictionary, capital_hit_flag)

            #Make the location back to its original one if the unit hit the capital
            new_location = capital_position_reset(capital_hit_flag, new_location, unit)

        #Change the dictionary values to indicate the unit has moved
        dictionary_unit_clearer(tile_info_dictionary, unit, civ_number)

        #Determine if the unit collides with another unit
        unit_collision_case(new_location, stat_dictionary, tile_info_dictionary, civ_number, unit)

        #Make all pertinent tiles visible
        tiles_to_make_visibile(new_location, territory_civ_numbers_dict, tile_info_dictionary)

        #Add this location to the list of new locations
        new_unit_locations.append(new_location)

    #Return the new locations to the original variable
    return new_unit_locations

#Define a function that updates the unit list depending on the dictionary
def unit_list_updater(civ_number, unit_location_list, tile_info_dictionary):
    #Begin a for loop that runs through all the unit locations
    for tile in unit_location_list:
        #Determine if the tile unit is owned by someone else now (likely through combat)
        if tile_info_dictionary[tile][5] != civ_number:
            #Remove that instance, since the unit likely died
            unit_location_list.remove(tile)

#Define a function that determines which civ name to display
def civ_name_print_determiner(civ_number, user_civ_number):
    #Begin an if statement to determine which civ to return the name of
    if civ_number == user_civ_number:
        #Make the name to display "You"
        display_name = "You"
    #Begin else if statement to determine when to represent India
    elif civ_number == 1:
        #Make the name to display "India"
        display_name = "India"
    #Begin else if statement to determine when to represent Rome
    elif civ_number == 2:
        #Make the name to display "Rome"
        display_name = "Rome"
    #Otherwise, the civ should be America
    else:
        #Make the name to display "America"
        display_name = "America"

    #Return the display name to the original variable
    return display_name

#Define a function that prints a war occurence
def war_notification(warmonger_name, defender_name):
    #Print a statement for both civs
    print(warmonger_name + ' declared war on ' + defender_name + '!')

    #Print space for clarity
    space()

#Define a function that  prints the end of a war
def war_end_notification(warmonger_flag, warmonger_name, defender_name):
    #Begin an if statement to determine which unit won or lost
    if warmonger_flag == True:
        #Print a statement clarifying the result of the war
        print(warmonger_name + ' attacked ' + defender_name + ' and won! No tiles are controlled by ' + defender_name + ' anymore.')
    #Otherwise, the defender won
    else:
        #Print a statement clarifying the result of the war
        print(defender_name + ' defended against ' + warmonger_name + ' and won! For now, no units are owned by ' + warmonger_name + ' anymore.')

    #Print space for clarity
    space()

#Define a function that determines a war winner
def war_winner(territory_civ_numbers_dict, unit_civ_numbers_dict, war_info, stat_civ_numbers_dict, tile_info_dictionary):
    #Determine the warmonger and the defender
    warmonger = war_info[0]
    defender = war_info[1]

    #Determine the defender's capital health
    capital_health = stat_civ_numbers_dict[defender][6]

    #Determine the warmonger's unit locations
    warmonger_unit_list = unit_civ_numbers_dict[warmonger]

    #Establish the return variable as 'n', assuming the civs don't win or lose, so boolean statements aren't triggered
    warmonger_winner = 'n'

    #If capital_health <= 0, the warmonger wins
    if capital_health <= 0:
        #Determine the defender's tiles
        defender_tile_list = territory_civ_numbers_dict[defender]

        #Determine the defender's units
        defender_unit_list = unit_civ_numbers_dict[defender]

        #Clear all the the ownership from the defender's tiles
        for tiles in defender_tile_list:
            tile_info_dictionary[tiles][2] = False
            tile_info_dictionary[tiles][3] = False
            tile_info_dictionary[tiles][6] = False
            tile_info_dictionary[tiles][7] = 0
            tile_info_dictionary[tiles][8] = False
            tile_info_dictionary[tiles][9] = False

        #Clear all ownership and existence of the civ's units
        for units in defender_unit_list:
            tile_info_dictionary[units][4] = False
            tile_info_dictionary[units][5] = 0

        #Clear all the defender's units and tiles
        defender_unit_list = []
        defender_tile_list = []

        #Update the dictionaries
        unit_civ_numbers_dict[defender] = defender_unit_list
        territory_civ_numbers_dict[defender] = defender_tile_list

        #Indicate defender lost
        warmonger_winner = True
    #Begin else if statement to determine if the defender won
    elif warmonger_unit_list == []:
        #Indicate defender won
        warmonger_winner = False

    #Return the result to the original variable
    return warmonger_winner

###########################################
#CPU UNIT FUNCTIONS
###########################################
#Define a function that determines the cpu choice of movement
def cpu_individual_unit_movement():
    #Establish RNG to determine direction
    direction = random.randint(1,5)

    #Establish an empty list to store direction and number of spaces in
    order = []

    #If the direction = 1, the order should just be to stay, so indicate that
    if direction == 1:
        #Make order stay
        order = 'S'

    #Otherwise, randomize number of spaces as well
    else:
        #Establish RNG to determine number of spaces
        spaces = random.randint(1,4)

        #Continue if statement for possible directions
        if direction == 2:
            #Make order up
            order.append('U')
        #Begin a set of else if statements for all the other directions
        elif direction == 3:
            #Make order right
            order.append('R')

        elif direction == 4:
            #Make order down
            order.append('D')

        #Otherwise, the direction is down since the number is 5
        else:
            #Make order left
            order.append('L')

        #Add the number of spaces to the orders
        order.append(spaces)

    #Return the order to the original variable
    return order

#Define a function that does an overall check of cpu unit movements
def cpu_unit_movement_choice_check(cpu_era, cpu_unit_start, cpu_unit_end, tile_info_dictionary, cpu_civ_number, cpu_order, cpu_war_info):
    #If the order is to stay, the number of spaces can't be taken
    if cpu_order != 'S':
        #Take the spaces from the cpu_order
        cpu_space = cpu_order[1]

    #Determine if all the flags even need to be determined
    if cpu_order != 'S':
        #Determine this flag first
        movement_unit_flag = unit_move_map_border_check(cpu_unit_start, cpu_unit_end, cpu_order)
        #If the above value is false, checking the next two values gives an index error, so make an if statement to bypass these two
        if movement_unit_flag != True:
            #Run all pertinent variables through 2 checking functions to determine if any of the flags are raised
            space_number_flag = space_number_check(cpu_era, cpu_space)
            direction_flag = unit_move_map_border_check(cpu_unit_start, cpu_unit_end, cpu_order)
        #Otherwise, make the two flags false anyways since the following while loop will be triggered anyways
        else:
            #Make both flags false
            space_number_flag = False
            direction_flag = False
            friendly_collision_flag = False
    #Otherwise, make the flags false anyways
    else:
        #Make all of the above flags false, since they can't be raised
        space_number_flag = False
        direction_flag = False
        movement_unit_flag = False
    #Begin an if statement to determine whether this flag needs to even be determined
    if movement_unit_flag != True:
        #Run through this function to determine if the uni collides with its own units/capital
        friendly_collision_flag = collision_check(tile_info_dictionary, cpu_unit_start, cpu_unit_end, cpu_civ_number, cpu_war_info)

    #If any of the flags are true, the movement is invalid, so make a flag indicating that
    if space_number_flag == True or direction_flag == True or friendly_collision_flag == True or movement_unit_flag == True:
        #Make a flag to indicate the movements are invalid
        movement_invalid_flag = True
    #Otherwise, the movement has no issues
    else:
        #Make a flag to indicate the movements are invalid
        movement_invalid_flag = False

    #Return the movement flag to the original variable
    return movement_invalid_flag

#Define a function that moves each cpu unit
def cpu_unit_movement(cpu_unit_locations, cpu_era, tile_info_dictionary, cpu_civ_number, cpu_stat_dictionary, territory_civ_numbers_dict, cpu_war_info):
    #Establish an empty list for the new unit locations
    new_cpu_unit_locations = []

    #Begin a for loop that runs for each unit in the cpu's roster
    for unit in cpu_unit_locations:

        #Take the randomly selected unit order
        cpu_order = cpu_individual_unit_movement()

        #Determine the new location of the unit after the order
        cpu_new_location = unit_mover(cpu_order, cpu_civ_number, unit)

        #Put the order through appropriate checks and balances
        movement_invalidity_flag =  cpu_unit_movement_choice_check(cpu_era, unit, cpu_new_location, tile_info_dictionary, cpu_civ_number, cpu_order, cpu_war_info)

        #Change the order if it's invalid
        while movement_invalidity_flag == True:

            #Take the randomly selected unit order
            cpu_order = cpu_individual_unit_movement()

            #Determine the new location of the unit after the order
            cpu_new_location = unit_mover(cpu_order, cpu_civ_number, unit)

            #Put the order through appropriate checks and balances
            movement_invalidity_flag =  cpu_unit_movement_choice_check(cpu_era, unit, cpu_new_location, tile_info_dictionary, cpu_civ_number, cpu_order, cpu_war_info)

        #Determine if war moves need to be made
        if cpu_war_info != []:

            #Determine if the unit hits the capital
            cpu_capital_hit_flag = capital_siege_determiner(tile_info_dictionary, territory_civ_numbers_dict, cpu_war_info, cpu_new_location)

            #Remove capital health if the unit hits the capital
            capital_siege(tile_info_dictionary, cpu_war_info, cpu_stat_dictionary, cpu_capital_hit_flag)

            #Make the location back to its original one if the unit hit the capital
            new_location = capital_position_reset(cpu_capital_hit_flag, cpu_new_location, unit)

        #Change the dictionary values to indicate the unit has moved
        dictionary_unit_clearer(tile_info_dictionary, unit, cpu_civ_number)

        #Determine if the unit collides with another unit
        unit_collision_case(cpu_new_location, cpu_stat_dictionary, tile_info_dictionary, cpu_civ_number, unit)

        #Add the checked new location to the original variable
        new_cpu_unit_locations.append(cpu_new_location)

    #Return the new list of locations
    return new_cpu_unit_locations

###########################################
#ROI & EXPANSION FUNCTIONS
###########################################

#Define a function that increases a civ's stats depending on their ROI
def periodic_ROI(civ_stats):
    #Establish the two indexers to produce values
    stat_index = 0
    ROI_index = 3

    #Begin a for loop that continues for the same range as the number of stats in the list
    for stat_changes in range(3):
        #Hold both values from the stats list
        stats = civ_stats[stat_index]
        ROI = civ_stats[ROI_index]

        #Change the stat
        stats += ROI

        #Change the corresponding list value
        civ_stats[stat_index] = stats

        #Increase both indexers by 1 so it goes through all the values and ROIs
        stat_index += 1
        ROI_index += 1

#Define a function that determines the number of tiles a civ can expand into
def civ_tile_expansion_check(captured_tiles, tile_info_dictionary):
    #Establish an empty list of possible territories to expand into
    tiles_to_expand_into = []

    #Begin a for loop that runs for each captured tile
    for tile in captured_tiles:
        #Establish variables for possible tiles the tile can expand into
        upper_tile = tile + 10
        lower_tile = tile - 10
        left_tile = tile - 1
        right_tile = tile + 1

        #Possible tiles to expand to
        tiles_in_vicinity = [upper_tile, lower_tile, left_tile, right_tile]

        #Run the tiles through area check to determine the valid tiles to expand into
        tiles_in_vicinity = area_expansion_check(tile_info_dictionary, tiles_in_vicinity, tile)

        #Hold all the tiles in the tiles_to_expand_into variable
        tiles_to_expand_into += tiles_in_vicinity

    #Return the tiles_to_expand_into variable to the original variable
    return tiles_to_expand_into

#Define a function that picks a tile from a list of tiles to expand into
def civ_tile_expander(civ_number, user_civ_number, captured_tiles, tile_info_dictionary, turn):
    #Establish a variable to determine if this turn is a turn to expand on
    expanding_turn_status = turn % 3
    #Determine if the turn is a viable turn to expand on
    if expanding_turn_status == 0:

        #Determine the possible tiles to expand into
        tiles_to_expand_into = civ_tile_expansion_check(captured_tiles, tile_info_dictionary)

        #Hold the length of the possible tiles to expand into
        number_tiles_to_expand = len(tiles_to_expand_into)

        #Determine if the number of tiles to expand into is greater than 0
        if number_tiles_to_expand != 0:

            #Reduce the number of tiles by 1 so that if it reaches the maximum length of the list, it doesn't bring up an index error
            number_tiles_to_expand -= 1

            #Determine a random number from the list to index
            tile_to_expand_index = random.randint(0,number_tiles_to_expand)

            #Determine the tile to expand into
            tile_to_expand = tiles_to_expand_into[tile_to_expand_index]

            #Add the tile expanded into to the list of captured tiles
            captured_tiles.append(tile_to_expand)

            #Change the tile_to_expand class to a list so it's iterable
            tile_to_expand = [tile_to_expand]

            #Change the dictionary value for the tile to expand into
            dictionary_value_changer(tile_info_dictionary, tile_to_expand, civ_number)

            #Determine if the civ is the user's civ
            if civ_number == user_civ_number:

                #Change the tile keys so that the user can see them if it's their expansion
                user_territory_dictionary_indicator(tile_info_dictionary, tile_to_expand)

###########################################
#WINNER FUNCTION
###########################################

#Define a function that displays the result of the game
def game_winner(user_win):
    #Begin an if statement to determine which end message to display
    if user_win == True:
        #Display the final message
        final_message = '''
!!!!!!!!!!! VICTORY !!!!!!!!!!!
You have proven yourself as the ruler of a great nation, showing the masses that your rule is superior by permanently etching yourself in history. Congratulations!'''
    #Otherwise the user lost
    else:
        final_message = '''
DEFEAT
You have battled amongst history's greatest rulers, and unfortunately, the challenge was too great. History is written by the victors, and will likely not be kind to your rule; that is, unless you compete once again, and prove yourself the greatest ruler of them all?'''

    #Display the final message to the user
    print(final_message)

    #Print space for clarity
    space()

###########################################
#INTRO DESCRIPTION FUNCTION
###########################################

#Define a function that displays the intro paragraph
def intro_paragraph_print():
    #Print a statement indicating the intro to the user
    print('''You start here! Every third turn, your civilization's reach extends randomly from one of your already captured tiles, stopping only at the border of the map, or if you come into contact with another civ's territory. When starting, you determine which production your civ produces, (unit, structure or special structure) and which technology it researches (you can bring up a tree of technologies whenever the game asks you to pick a technology to research.). Each of these take a certain number of turns before you can make a new product or research a new technology.''')

    #Print space for clarity
    space()

###########################################
#MAIN BODY
###########################################

#Run the user through the receiving function and hold their answer
user_command = menu_receive()

#Check the user's menu command
user_command = menu_check(user_command)

#Run the user through a function to determine which menu selection they chose, and store that selection
quitting_flag = menu(user_command)

#Begin while loop that continues while the user didn't quit
while quitting_flag == False:

    ###########################################
    #GLOBAL VARIABLES
    ###########################################

    #List of all units on the map
    map_unit_list = [
    [1,2,3,4,5,6,7,8,9,10],
    [11,12,13,14,15,16,17,18,19,20],
    [21,22,23,24,25,26,27,28,29,30],
    [31,32,33,34,35,36,37,38,39,40],
    [41,42,43,44,45,46,47,48,49,50],
    [51,52,53,54,55,56,57,58,59,60],
    [61,62,63,64,65,66,67,68,69,70],
    [71,72,73,74,75,76,77,78,79,80],
    [81,82,83,84,85,86,87,88,89,90],
    [91,92,93,94,95,96,97,98,99,100]
    ]

    #Create a flag that will eventually determine if the user or the cpu has won, but for now, since neither has won, both are false
    user_win = False
    cpu1_win = False
    cpu2_win = False

    #Create a turn counter
    turn = 1

    #Create a set of variables as false for now, but eventually determine whether a civ needs to research a science, produce something or move a unit
    science_task = False
    production_task = False
    unit_orders = False
    cpu1_science_task = False
    cpu1_production_task = False
    cpu1_unit_orders = False
    cpu2_science_task = False
    cpu2_production_task = False
    cpu2_unit_orders = False

    #Create a set of lists that hold the civs unit locations (none for now)
    user_unit_locations = []
    cpu1_unit_locations = []
    cpu2_unit_locations = []

    #Create a set of lists that hold structure locations (none for now)
    user_structure_locations = []
    cpu1_structure_locations = []
    cpu2_structure_locations = []

    #Set every civs status to the stone era for now
    user_era = 'stone'
    cpu1_era = 'stone'
    cpu2_era = 'stone'

    #Set each civs set of researched technologies as empty from the start
    user_tech_researched = []
    cpu1_tech_researched = []
    cpu2_tech_researched = []

    #Hold war info lists as empty for now so that
    user_war_info = []
    cpu1_war_info = []
    cpu2_war_info = []

    #Establish the turn through which various processes happen as 0 so the corresponding nested if statement isn't triggered
    turn_tech_researched_user = 0
    turn_product_finished = 0
    turn_tech_researched_cpu1 = 0
    turn_product_finished_cpu1 = 0
    turn_tech_researched_cpu2 = 0
    turn_product_finished_cpu2 = 0

    #Run the map through the map_value_generator() function and receive the dictionary with all pertinent values on the map
    map_unit_info_dictionary = map_value_generator(map_unit_list)

    #Receive the user's civ in a variable
    user_civ = user_civ_receiver()

    #Check the user's choice of civ
    user_civ = user_civ_choice_check(user_civ)

    #Run the user's civ through the capitalizer
    user_civ = choice_capitalizer(user_civ)

    #Run user's civ through the number translator for dictionary use
    chosen_civ_number = user_civ_number(user_civ)

    #Determine where the user starts by running their info through the capital function
    capital = user_capital(map_unit_info_dictionary, chosen_civ_number)

    #Determine all the user's starting area by running them through the starting area function
    user_controlled_territories = starting_area(map_unit_info_dictionary, chosen_civ_number, capital)

    #Run the user's tiles through another dictionary changer to indicate that all this territory is theirs not the cpus
    user_territory_dictionary_indicator(map_unit_info_dictionary, user_controlled_territories)

    #Determine which civs the cpus are
    cpu_civ_list = cpu_civ_determiner(chosen_civ_number)

    #Separate the items in the list taken from the previous function
    cpu1_civ_number = cpu_civ_list[0]
    cpu2_civ_number = cpu_civ_list[1]

    #Determine cpu1's capital and starting area
    cpu1_capital = cpu_capital_determiner(map_unit_info_dictionary, cpu1_civ_number)
    cpu1_controlled_territories = starting_area(map_unit_info_dictionary, cpu1_civ_number, cpu1_capital)

    #Determine cpu2's capital and starting area
    cpu2_capital = cpu_capital_determiner(map_unit_info_dictionary, cpu2_civ_number)
    cpu2_controlled_territories = starting_area(map_unit_info_dictionary, cpu2_civ_number, cpu2_capital)

    #Determine what the map will look like after given updated info
    updated_map = map_updater(map_unit_info_dictionary, chosen_civ_number)

    #Print the updated map to display to the user
    print(updated_map)

    #Print space for clarity
    space()

    #Display an intro paragraph for the user
    intro_paragraph_print()

    #Receive the user, then both civs list of stats
    user_stats = civ_stat_distributor(chosen_civ_number)
    cpu1_stats = civ_stat_distributor(cpu1_civ_number)
    cpu2_stats = civ_stat_distributor(cpu2_civ_number)

    #Make a dictionary of civ_number and stat values of each civ for unit damage  calculations
    stat_civ_numbers_dict = {chosen_civ_number:user_stats, cpu1_civ_number:cpu1_stats, cpu2_civ_number:cpu2_stats}

    #Make a dictionary of civ_number and terrirory values for each civ
    territory_civ_numbers_dict = {chosen_civ_number:user_controlled_territories, cpu1_civ_number:cpu1_controlled_territories, cpu2_civ_number:cpu2_controlled_territories}

    #Make a dictionary of civ_number and unit values for each civ
    unit_civ_numbers_dict =  {chosen_civ_number:user_unit_locations, cpu1_civ_number:cpu1_unit_locations, cpu2_civ_number:cpu2_unit_locations}

    #Begin a while loop that continues while the user and the cpus don't win
    while user_win == False and cpu1_win == False and cpu2_win == False:

        ###########################################
        #MAP UPDATER
        ###########################################

        #Hold the updated map in a variable to print it
        updated_map = map_updater(map_unit_info_dictionary, chosen_civ_number)

        #Print the updated map for the new turn
        print(updated_map)

        #Print a space for clarity
        space()

        ###########################################
        #TURN DISPLAY
        ###########################################

        #Establish a variable that determines the status of the following turn
        following_turn_status = turn + 1

        #Hold a string version of the turn to print it every turn
        turn_print = str(turn)

        #Print the turn
        print('Turn ' + turn_print)

        ###################################################################################
        #USER TURN
        ###################################################################################

        #Begin an if statement to determine if the user loses from war or not
        if user_controlled_territories != []:

            ###########################################
            #UNIT ORDERS
            ###########################################

            #Begin an if statement that determines if the user needs to give orders to a unit or not
            if unit_orders == True:
                #Run the user through the move receiver to determine each of their new locations
                user_unit_locations = unit_move_receiver(user_unit_locations, user_era, map_unit_info_dictionary, chosen_civ_number, stat_civ_numbers_dict, territory_civ_numbers_dict, user_war_info)

                #Establish a variable that will determine if the civ went to war this turn
                user_war_info_check = user_war_info

                #Determine if any unit was lost in battle
                unit_list_updater(chosen_civ_number, user_unit_locations, map_unit_info_dictionary)
                unit_list_updater(cpu1_civ_number, cpu1_unit_locations, map_unit_info_dictionary)
                unit_list_updater(cpu2_civ_number, cpu2_unit_locations, map_unit_info_dictionary)

                #Update the unit location of the corresponding civ
                unit_civ_numbers_dict[chosen_civ_number] = user_unit_locations

                #Only check war status if the user isn't at war already
                if user_war_info == []:
                    #Determine if the user is at war with anyone
                    user_war_info = unit_territory_war_check(user_unit_locations, map_unit_info_dictionary)

                #If the user is at war, run them through a separate set of functions
                if user_war_info != []:
                    #Determine if the civ went to war this turn by checking if the list was empty prior to this turn
                    if user_war_info_check == []:
                        #Determine the warmonger
                        warmonger = user_war_info[0]
                        defender = user_war_info[1]

                        #Determine the name of both civs
                        warmonger_name = civ_name_print_determiner(warmonger, chosen_civ_number)
                        defender_name = civ_name_print_determiner(defender, chosen_civ_number)

                        #Display a message indicating who declared war
                        war_notification(warmonger_name, defender_name)

                    #Most unit movements are the same, except when attacking the capital,which is handled in the unit_move_receiver function so most of war is figured out, so the following is a function to determine if a winner is found
                    warmonger_flag = war_winner(territory_civ_numbers_dict, unit_civ_numbers_dict, user_war_info, stat_civ_numbers_dict, map_unit_info_dictionary)

                    #Determine if any unit was lost in war
                    unit_list_updater(chosen_civ_number, user_unit_locations, map_unit_info_dictionary)
                    unit_list_updater(cpu1_civ_number, cpu1_unit_locations, map_unit_info_dictionary)
                    unit_list_updater(cpu2_civ_number, cpu2_unit_locations, map_unit_info_dictionary)

                    #Determine if the flag is a boolean value
                    if warmonger_flag == True or warmonger_flag == False:
                        #Display the result of the war
                        war_end_notification(warmonger_flag, warmonger_name, defender_name)

                        #Change the status of the war info to indicate war is over
                        user_war_info = []

                        #Update the territory locations
                        cpu1_controlled_territories = territory_civ_numbers_dict[cpu1_civ_number]
                        cpu2_controlled_territories = territory_civ_numbers_dict[cpu2_civ_number]

                #Determine if the user needs to input unit orders next turn
                if user_unit_locations == []:

                    #Change the status of the unit_orders flag
                    unit_orders = False

                #Determine if either of the other civs lost all their units
                if cpu1_unit_locations == []:

                    #Change the status of the corresponding unit_orders flag
                    cpu1_unit_orders = False

                if cpu2_unit_locations == []:

                    #Change the status of the corresponding unit_orders flag
                    cpu2_unit_orders = False

                #Determine if the user won this turn (both other civs have no territory)
                if cpu1_controlled_territories == [] and cpu2_controlled_territories == []:
                    #If neither other civ controls territories, the user won
                    user_win = True
                    #Make both other user tasks true so nothing else happens this turn
                    production_task = True
                    science_task = True



            ###########################################
            #PRODUCTION TASK
            ###########################################

            #Begin an if statement that determines if the user needs to produce an item or not
            if production_task == False:
                #Begin another if statement the user just finished a production
                if turn_product_finished == turn:
                    #Begin another if statement to determine if the product was a structure, special structure or a unit
                    if user_production == 's' or user_production == 'S':
                        #Change the number of structures of the user's structure locations
                        structure_builder(user_structure_tile, user_structure_locations, user_stats, user_production)


                #Determine the user's production
                user_production = user_production_choice()

                #Determine if the user's choice is valid or not
                user_production = user_production_check_general(user_production)

                #Determine the possibility of a structure being built
                user_structure_possibility = structure_build_check(map_unit_info_dictionary, user_controlled_territories, chosen_civ_number)

                #Determine the possibility of building a special structure on any tile
                user_special_possibility = special_check(chosen_civ_number, user_era)

                #Determine the user's checked production, after determining the flags
                user_production = user_production_check_specific(user_production, user_structure_possibility, user_special_possibility)

                #Determine if the user wants to see a tile guide display
                user_production = tile_guide_display(user_production, user_structure_possibility, user_special_possibility)

                #Begin an if statement to determine if the choice needs to be capitalized
                if user_production == 'u':

                    #Capitalize the user's choice to allow for a global production variable
                    user_production = choice_capitalizer(user_production)

                #Determine the cost of the production, given its type and the era the user is in
                user_production_cost = production_cost_determiner(user_era, user_production)

                #Determine the number of turns it would take to produce
                turns_to_produce = turn_product_finishes_determiner(user_stats, user_production_cost)

                #Determine the turn by which the production will complete
                turn_product_finished = turn + turns_to_produce

                #Change the status of the production flag so next loop it skips past this if statement directly to the else
                production_task = True

            #Begin an if statement to determine if the user's production will finish next turn or not, or if the user finished this turn, (possible if the user's production is high enough)
            if following_turn_status == turn_product_finished:

                #Change the status of the flag so that next loop, a new product can be made
                production_task = False

                #Begin an if statement to determine if the user selected a structure as a product
                if user_production == 's' or user_production == 'S':
                    #Change the dictionary values and list values of the tiles in which the structure is built
                    user_structure_tile = structure_displayer(map_unit_info_dictionary, user_controlled_territories, chosen_civ_number, user_production)
                #Otherwise, the user produced a unit, so initate the unit in an appropriate position
                else:
                    #Establish the unit's starting position (civ's capital)
                    unit_initiator(map_unit_info_dictionary, user_controlled_territories, chosen_civ_number, user_unit_locations)

                    #Update the corresponding unit tiles in the dictionary
                    unit_civ_numbers_dict[chosen_civ_number] = user_unit_locations

                    #Change status of unit orders
                    unit_orders = True

            #Expand the name of the user's production
            product_to_print = product_name_expander(user_production)

            #Determine the number of turns left to produce the product`
            turns_left_product_print = turns_left_process(turn_product_finished, turn)

            #Display the info for the turns left for the product
            turns_left_to_produce_display(turns_left_product_print, product_to_print)

            ###########################################
            #SCIENCE TASK
            ###########################################

            #Begin another if statement to determine whether the user is in the process of researching something or not
            if science_task == False:

                #Make an if statement for selecting a science for the first turn since it's easier
                if turn == 1:
                        #Determine the user's choice of tech, prior to loop to make structure easier
                        user_tech = fully_filtered_user_tech_choice(user_era)


                #If the user has the appropriate criteria to win the game, change the flag
                if user_tech == 'Astronomy' and turn_tech_researched_user == turn:
                    #Change the flag of the win, since the user can launch the rocket this turn
                    user_win = True

                #Otherwise, if the user hasn't finished, research goes back to normal
                else:

                    #If the user's research finished this turn, change the pertinent info
                    if turn_tech_researched_user == turn:

                        #The research is finished, so change the user's stats
                        user_stats = tech_civ_stats(user_tech, user_stats, user_era)

                        #Determine the point at the era the user is in
                        era_determiner = tech_era_determiner(user_tech_researched)

                        #Begin if statement to determine if the user just finished an era, or one is about to start
                        if era_determiner == 1:
                            #Notify the user they're going to research the other tech in that era
                            other_tech_switch_notifier()

                            #Determine the other tech the user needs to research
                            user_tech = other_tech_switch(user_era, user_tech)

                        #Otherwise, the user has entered a new era, so switch the era up
                        else:
                            #Make the user era increase
                            user_era = era_switcher(user_era)

                            #Since era is switched, allow user to enter a choice of tech in the new era
                            user_tech = fully_filtered_user_tech_choice(user_era)

                    #Determine the cost of the tech the user wants to research
                    user_tech_cost = tech_cost_determiner(user_era)

                    #Determine how many turns it would take for the user to fully research the tech given the cost of the specific tech
                    user_tech_turn_cost = tech_turn_determiner(user_stats, user_tech_cost)

                    #Determine the turn by which the tech will be built
                    turn_tech_researched_user = turn + user_tech_turn_cost

                    #Change the flag for the science task so it doesn't repeat
                    science_task = True

            #Begin if statement to determine if the user is about to finish research for the next loop
            if following_turn_status == turn_tech_researched_user:
                #Change the status of the science task since the user will research
                science_task = False

                #Prematurely add the tech to the researched techs
                user_tech_researched.append(user_tech)

            #Extend the name of the technology the user chose so it can be printed
            tech_to_print = tech_name_expander(user_tech, user_era)

            #Determine the turns left to research
            turns_left_research_print = turns_left_process(turn_tech_researched_user, turn)

            #Display the info for the user
            turns_left_to_research_display(tech_to_print, turns_left_research_print)

        #Otherwise, the user controls no territories and has lost the game
        else:
            #Make both cpu flags true so to indicate the user's civilization collapsed
            cpu1_win = True
            cpu2_win = True

        ###################################################################################
        #CPU1 TURN
        ###################################################################################
        #Begin an if statement to determine if cpu1 is still in the game
        if cpu1_controlled_territories != []:
            ###########################################
            #CPU1 UNIT ORDERS
            ###########################################

            #Begin an if statement that determines if the civ needs to give orders to a unit or not
            if cpu1_unit_orders == True:
                #Run the civ through the movement function to determine each of their new locations
                cpu1_unit_locations = cpu_unit_movement(cpu1_unit_locations, cpu1_era, map_unit_info_dictionary, cpu1_civ_number, stat_civ_numbers_dict, territory_civ_numbers_dict, cpu1_war_info)

                #Establish a variable that will determine if the civ went to war this turn
                cpu1_war_info_check = cpu1_war_info

                #Determine if any unit was lost in battle
                unit_list_updater(chosen_civ_number, user_unit_locations, map_unit_info_dictionary)
                unit_list_updater(cpu1_civ_number, cpu1_unit_locations, map_unit_info_dictionary)
                unit_list_updater(cpu2_civ_number, cpu2_unit_locations, map_unit_info_dictionary)

                #Update the unit location of the corresponding civ
                unit_civ_numbers_dict[cpu1_civ_number] = cpu1_unit_locations

                #Only check war status if the civ isn't at war already
                if cpu1_war_info == []:
                    #Determine if the civ is at war with anyone
                    cpu1_war_info = unit_territory_war_check(cpu1_unit_locations, map_unit_info_dictionary)

                #If the civ is at war, run them through a separate set of functions
                if cpu1_war_info != []:
                    #Determine if the civ went to war this turn by checking if the list was empty prior to this turn
                    if cpu1_war_info_check == []:
                        #Determine the warmonger
                        cpu1_warmonger = cpu1_war_info[0]
                        cpu1_defender = cpu1_war_info[1]

                        #Determine the name of both civs
                        cpu1_warmonger_name = civ_name_print_determiner(cpu1_warmonger, chosen_civ_number)
                        cpu1_defender_name = civ_name_print_determiner(cpu1_defender, chosen_civ_number)

                        #Display a message indicating who declared war
                        war_notification(cpu1_warmonger_name, cpu1_defender_name)

                    #Most unit movements are the same, except when attacking the capital,which is handled in the unit_move_receiver function so most of war is figured out, so the following is a function to determine if a winner is found
                    warmonger_flag = war_winner(territory_civ_numbers_dict, unit_civ_numbers_dict, cpu1_war_info, stat_civ_numbers_dict, map_unit_info_dictionary)

                    #Determine if any unit was lost in war
                    unit_list_updater(chosen_civ_number, user_unit_locations, map_unit_info_dictionary)
                    unit_list_updater(cpu1_civ_number, cpu1_unit_locations, map_unit_info_dictionary)
                    unit_list_updater(cpu2_civ_number, cpu2_unit_locations, map_unit_info_dictionary)


                    #Determine if the flag is a boolean value
                    if warmonger_flag == True or warmonger_flag == False:
                        #Display the result of the war
                        war_end_notification(warmonger_flag, cpu1_warmonger_name, cpu1_defender_name)

                        #Change the status of the war info to indicate war is over
                        cpu1_war_info = []

                        #Update the territory locations
                        user_controlled_territories = territory_civ_numbers_dict[chosen_civ_number]
                        cpu2_controlled_territories = territory_civ_numbers_dict[cpu2_civ_number]

                #Determine if the user needs to input unit orders next turn
                if user_unit_locations == []:

                    #Change the status of the unit_orders flag
                    unit_orders = False

                #Determine if either of the other civs lost all their units
                if cpu1_unit_locations == []:

                    #Change the status of the corresponding unit_orders flag
                    cpu1_unit_orders = False

                if cpu2_unit_locations == []:

                    #Change the status of the corresponding unit_orders flag
                    cpu2_unit_orders = False

            ###########################################
            #CPU1 PRODUCTION
            ###########################################

            #Begin an if statement that determines if the cpu needs to produce an item or not
            if cpu1_production_task == False:
                #Begin another if statement the cpu just finished a production
                if turn_product_finished_cpu1 == turn:
                    #Begin another if statement to determine if the product was a structure or a special structure
                    if cpu1_production == 's' or cpu1_production == 'S':
                        #Change the number of structures of the cpu's structure locations
                        structure_builder(cpu1_structure_tile, cpu1_structure_locations, cpu1_stats, cpu1_production)

                #Determine the cpu's production
                cpu1_production = cpu_production_decider(map_unit_info_dictionary, cpu1_controlled_territories, cpu1_civ_number, cpu1_era)

                #Determine the cost of the production, given its type and the era the cpu is in
                cpu1_production_cost = production_cost_determiner(cpu1_era, cpu1_production)

                #Determine the number of turns it would take to produce the product
                turns_to_produce_cpu1 = turn_product_finishes_determiner(cpu1_stats, cpu1_production_cost)

                #Determine the turn by which the product should be produced
                turn_product_finished_cpu1 = turn + turns_to_produce_cpu1

                #Change the flag of the production task
                cpu1_production_task = True

            #Determine if the production finishes next turn
            if following_turn_status == turn_product_finished_cpu1:
                #Change the status of the production task flag
                cpu1_production_task = False

                #Determine if the cpu built a structure or a unit
                if cpu1_production == 's' or cpu1_production == 'S':
                    #Change the dictionary values and determine which tile to build a structure on
                    cpu1_structure_tile = structure_displayer(map_unit_info_dictionary, cpu1_controlled_territories, cpu1_civ_number, cpu1_production)
                #Otherwise the cpu built a unit
                else:
                    #Establish the unit's starting position (civ's capital)
                    unit_initiator(map_unit_info_dictionary, cpu1_controlled_territories, cpu1_civ_number, cpu1_unit_locations)

                    #Update the corresponding unit tiles in the dictionary
                    unit_civ_numbers_dict[cpu1_civ_number] = cpu1_unit_locations

                    #Change the need for the civ to dictate orders to its units
                    cpu1_unit_orders = True


            ###########################################
            #CPU1 SCIENCE
            ###########################################

            #Begin an if statement that determines if this cpu is researching a science or not
            if cpu1_science_task == False:

                #Make an if statement for selecting a science for the first turn since it's easier
                if turn == 1:
                        #Determine this cpu's tech choice
                        cpu1_tech = cpu_tech_choice(cpu1_era)

                #If the cpu has the appropriate criteria to win the game, change the flag
                if cpu1_tech == 'Astronomy' and turn_tech_researched_cpu1 == turn:
                    #Change the flag of the win, since the cpu can launch the rocket this turn
                    cpu1_win = True

                #Otherwise, if the cpu hasn't finished, research goes back to normal
                else:

                    #If the cpu's research finished this turn, change the pertinent info
                    if turn_tech_researched_cpu1 == turn:

                        #The research is finished, so change the cpu's stats
                        cpu1_stats = tech_civ_stats(cpu1_tech, cpu1_stats, cpu1_era)

                        #Determine the point at the era the cpu is in
                        era_determiner_cpu1 = tech_era_determiner(cpu1_tech_researched)

                        #Begin if statement to determine if the cpu just finished an era, or one is about to start
                        if era_determiner_cpu1 == 1:

                            #Determine the other tech the cpu needs to research
                            cpu1_tech = other_tech_switch(cpu1_era, cpu1_tech)

                        #Otherwise, the cpu has entered a new era, so switch the era up
                        else:
                            #Make the cpu era increase
                            cpu1_era = era_switcher(cpu1_era)

                            #Determine this cpu's tech choice
                            cpu1_tech = cpu_tech_choice(cpu1_era)

                #Determine the cost of the tech
                cpu1_tech_cost = tech_cost_determiner(cpu1_era)

                #Determine the number of turns the tech will take to research
                turns_to_research_cpu1 = tech_turn_determiner(cpu1_stats, cpu1_tech_cost)

                #Determine the turn by which the tech will be researched
                turn_tech_researched_cpu1 = turns_to_research_cpu1 + turn

                #Change the status of the science task flag
                cpu1_science_task = True

            #Determine if the research will finish on this turn
            if following_turn_status == turns_to_research_cpu1:
                #Change the status of the task flag so that the cpu can change research choices
                cpu1_science_task = False

                #Prematurely add the tech to the list of researched tech
                cpu1_tech_researched.append(cpu1_tech)

        ###################################################################################
        #CPU2 TURN
        ###################################################################################
        #Begin an if statement to determine if cpu2 is still in the game
        if cpu2_controlled_territories != []:

            ###########################################
            #CPU2 UNIT ORDERS
            ###########################################

            #Begin an if statement that determines if the civ needs to give orders to a unit or not
            if cpu2_unit_orders == True:
                #Run the civ through the movement function to determine each of their new locations
                cpu2_unit_locations = cpu_unit_movement(cpu2_unit_locations, cpu2_era, map_unit_info_dictionary, cpu2_civ_number, stat_civ_numbers_dict, territory_civ_numbers_dict, cpu2_war_info)

                #Establish a variable that will determine if the civ went to war this turn
                cpu2_war_info_check = cpu2_war_info

                #Determine if any unit was lost in battle
                unit_list_updater(chosen_civ_number, user_unit_locations, map_unit_info_dictionary)
                unit_list_updater(cpu1_civ_number, cpu1_unit_locations, map_unit_info_dictionary)
                unit_list_updater(cpu2_civ_number, cpu2_unit_locations, map_unit_info_dictionary)

                #Update the unit location of the corresponding civ
                unit_civ_numbers_dict[cpu2_civ_number] = cpu2_unit_locations

                #Only check war status if the civ isn't at war already
                if cpu2_war_info == []:
                    #Determine if the civ is at war with anyone
                    cpu2_war_info = unit_territory_war_check(cpu2_unit_locations, map_unit_info_dictionary)

                #If the civ is at war, run them through a separate set of functions
                if cpu2_war_info != []:
                    #Determine if the civ went to war this turn by checking if the list was empty prior to this turn
                    if cpu2_war_info_check == []:
                        #Determine the warmonger
                        cpu2_warmonger = cpu2_war_info[0]
                        cpu2_defender = cpu2_war_info[1]

                        #Determine the name of both civs
                        cpu2_warmonger_name = civ_name_print_determiner(cpu2_warmonger, chosen_civ_number)
                        cpu2_defender_name = civ_name_print_determiner(cpu2_defender, chosen_civ_number)

                        #Display a message indicating who declared war
                        war_notification(cpu2_warmonger_name, cpu2_defender_name)

                    #Most unit movements are the same, except when attacking the capital,which is handled in the unit_move_receiver function so most of war is figured out, so the following is a function to determine if a winner is found
                    warmonger_flag = war_winner(territory_civ_numbers_dict, unit_civ_numbers_dict, cpu2_war_info, stat_civ_numbers_dict, map_unit_info_dictionary)

                    #Determine if any unit was lost in war
                    unit_list_updater(chosen_civ_number, user_unit_locations, map_unit_info_dictionary)
                    unit_list_updater(cpu1_civ_number, cpu1_unit_locations, map_unit_info_dictionary)
                    unit_list_updater(cpu2_civ_number, cpu2_unit_locations, map_unit_info_dictionary)


                    #Determine if the flag is a boolean value
                    if warmonger_flag == True or warmonger_flag == False:
                        #Display the result of the war
                        war_end_notification(warmonger_flag, cpu2_warmonger_name, cpu2_defender_name)

                        #Change the status of the war info to indicate war is over
                        cpu2_war_info = []

                        #Update the territory locations
                        user_controlled_territories = territory_civ_numbers_dict[chosen_civ_number]
                        cpu1_controlled_territories = territory_civ_numbers_dict[cpu1_civ_number]

                #Determine if the user needs to input unit orders next turn
                if user_unit_locations == []:

                    #Change the status of the unit_orders flag
                    unit_orders = False

                #Determine if either of the other civs lost all their units
                if cpu1_unit_locations == []:

                    #Change the status of the corresponding unit_orders flag
                    cpu1_unit_orders = False

                if cpu2_unit_locations == []:

                    #Change the status of the corresponding unit_orders flag
                    cpu2_unit_orders = False

            ###########################################
            #CPU2 PRODUCTION
            ###########################################


            #Begin an if statement that determines if the cpu needs to produce an item or not
            if cpu2_production_task == False:
                #Begin another if statement the cpu just finished a production
                if turn_product_finished_cpu2 == turn:
                    #Begin another if statement to determine if the product was a structure or a special structure
                    if cpu2_production == 's' or cpu2_production == 'S':
                        #Change the number of structures of the cpu's structure locations
                        structure_builder(cpu2_structure_tile, cpu2_structure_locations, cpu2_stats, cpu2_production)

                #Determine the cpu's production
                cpu2_production = cpu_production_decider(map_unit_info_dictionary, cpu2_controlled_territories, cpu2_civ_number, cpu2_era)

                #Determine the cost of the production, given its type and the era the cpu is in
                cpu2_production_cost = production_cost_determiner(cpu2_era, cpu2_production)

                #Determine the number of turns it would take to produce the product
                turns_to_produce_cpu2 = turn_product_finishes_determiner(cpu2_stats, cpu2_production_cost)

                #Determine the turn by which the product should be produced
                turn_product_finished_cpu2 = turn + turns_to_produce_cpu2

                #Change the flag of the production task
                cpu2_production_task = True

            #Determine if the production finishes next turn
            if following_turn_status == turn_product_finished_cpu2:
                #Change the status of the production task flag
                cpu2_production_task = False

                #Determine if the cpu built a structure or a unit
                if cpu2_production == 's' or cpu2_production == 'S':
                    #Change the dictionary values and determine which tile to build a structure on
                    cpu2_structure_tile = structure_displayer(map_unit_info_dictionary, cpu2_controlled_territories, cpu2_civ_number, cpu2_production)
                #Otherwise the cpu built a unit
                else:
                    #Establish the unit's starting position (civ's capital)
                    unit_initiator(map_unit_info_dictionary, cpu2_controlled_territories, cpu2_civ_number, cpu2_unit_locations)

                    #Update the corresponding unit tiles in the dictionary
                    unit_civ_numbers_dict[cpu2_civ_number] = cpu2_unit_locations


                    #Change the need for the civ to dictate orders to its units
                    cpu2_unit_orders = True


            ###########################################
            #CPU2 SCIENCE
            ###########################################

            #Begin an if statement that determines if this cpu is researching a science or not
            if cpu2_science_task == False:

                #Make an if statement for selecting a science for the first turn since it's easier
                if turn == 1:
                        #Determine this cpu's tech choice
                        cpu2_tech = cpu_tech_choice(cpu2_era)

                #If the cpu has the appropriate criteria to win the game, change the flag
                if cpu2_tech == 'Astronomy' and turn_tech_researched_cpu2 == turn:
                    #Change the flag of the win, since the cpu can launch the rocket this turn
                    cpu2_win = True

                #Otherwise, if the cpu hasn't finished, research goes back to normal
                else:

                    #If the cpu's research finished this turn, change the pertinent info
                    if turn_tech_researched_cpu2 == turn:

                        #The research is finished, so change the cpu's stats
                        cpu2_stats = tech_civ_stats(cpu2_tech, cpu2_stats, cpu2_era)

                        #Determine the point at the era the cpu is in
                        era_determiner_cpu2 = tech_era_determiner(cpu2_tech_researched)

                        #Begin if statement to determine if the cpu just finished an era, or one is about to start
                        if era_determiner_cpu2 == 1:

                            #Determine the other tech the cpu needs to research
                            cpu2_tech = other_tech_switch(cpu2_era, cpu2_tech)

                        #Otherwise, the cpu has entered a new era, so switch the era up
                        else:
                            #Make the cpu era increase
                            cpu2_era = era_switcher(cpu2_era)

                            #Determine this cpu's tech choice
                            cpu2_tech = cpu_tech_choice(cpu2_era)

                #Determine the cost of the tech
                cpu2_tech_cost = tech_cost_determiner(cpu2_era)

                #Determine the number of turns the tech will take to research
                turns_to_research_cpu2 = tech_turn_determiner(cpu2_stats, cpu2_tech_cost)

                #Determine the turn by which the tech will be researched
                turn_tech_researched_cpu2 = turns_to_research_cpu2 + turn

                #Change the status of the science task flag
                cpu2_science_task = True

            #Determine if the research will finish on this turn
            if following_turn_status == turns_to_research_cpu2:
                #Change the status of the task flag so that the cpu can change research choices
                cpu2_science_task = False

                #Prematurely add the tech to the list of researched tech
                cpu2_tech_researched.append(cpu2_tech)


        ###########################################
        #BASIC TURN PROCESSES
        ###########################################

        #Make if statements to only expand the territories and increase stats if the corresponding civs have some territory
        if user_controlled_territories != []:

            #If the turn is appropriate, expand the user's reach
            civ_tile_expander(chosen_civ_number, chosen_civ_number, user_controlled_territories, map_unit_info_dictionary, turn)

            #Increase the stats corresponding to the civ
            periodic_ROI(user_stats)


        if cpu1_controlled_territories != []:

            #Do the same for cpu1's territories
            civ_tile_expander(cpu1_civ_number, chosen_civ_number, cpu1_controlled_territories, map_unit_info_dictionary, turn)

            #Do the same for cpu1's stats
            periodic_ROI(cpu1_stats)


        if cpu2_controlled_territories != []:

            #Do the same for cpu2's territories
            civ_tile_expander(cpu2_civ_number, chosen_civ_number, cpu2_controlled_territories, map_unit_info_dictionary, turn)

            #Do the same for cpu1's stats
            periodic_ROI(cpu2_stats)

        #Increase the global number of turns by 1, since all actions are done
        turn += 1

        #Update the stat dictionary every turn so that it has the most updated values
        stat_civ_numbers_dict = {chosen_civ_number:user_stats, cpu1_civ_number:cpu1_stats, cpu2_civ_number:cpu2_stats}

        #Update the territory dictionary
        territory_civ_numbers_dict = {chosen_civ_number:user_controlled_territories, cpu1_civ_number:cpu1_controlled_territories, cpu2_civ_number:cpu2_controlled_territories}


    #Display a statement depending on the outcome of the game
    game_winner(user_win)

    #Run the user through the receiving function and hold their answer
    user_command = menu_receive()

    #Check the user's menu command
    user_command = menu_check(user_command)

    #Run the user through a function to determine which menu selection they chose, and store that selection
    quitting_flag = menu(user_command)


#Since the user quit if they are outside of the loop, print goodbye
print('Thank you for playing CIVILite, please play again!')
