""""Assignment 1"""

# Leah Younga Park
# A01064793


import Character
import random
import Monster
import json


def roll_a_die(number_of_rolls: int, number_of_sides: int) -> int:
    """
    Simulate rolling a die and return the value.

    PARAM: number_of_roll, Positive non zero Integer
               number_of_side, Positive non zero Integer
     PRE CONDITION: Parameter must be a non zero positive integer
     POST CONDITION:Return a sum of number of roll and number of side.
     RETURN: Return a sum of two positive integers
        >>> import random
        >>> random.seed(1)
        >>> roll_a_die(3,8)
        7
        >>> roll_a_die(1,5)
        5
    """

    result = random.randint(number_of_rolls, number_of_rolls * number_of_sides)
    return result


def get_user_input(your_message: str) -> str:
    """
    Get a message from a user and return it

    PARAM: your_message, string
    PRE CONDITION: Parameter must be a string
    POST CONDITION: None
    RETURN: Returns a string contains user message
    """
    user_input = input(your_message)
    return user_input


def verify_user() -> str:
    """
    Verify the user is new user or old user and return their name

    PARAM: None
    PRE CONDITION: User input must be a valid name.
    POST CONDITION: Return user name as a string
    RETURN: Returns string
    """
    print("\n\nHi, Are you a new user? if yes, please type Y, if no, please type YOUR NAME")
    user_check = get_user_input("")
    user_continue = True

    while user_continue is True:
        if user_check.strip().upper() == "Y":
            return user_check

        else:
            return user_check


def generate_character() -> Character:
    """
    Generate new character for new user.

    PARAM: None
    PRE CONDITION: User must not have a character.
    POST CONDITION: Returns well formed character
    RETURN: Returns character that contains character information
    """
    name = get_user_input("What is your name?")
    print("Hello " + name + "!\nLet's start! Hope you are ready!")
    player_character = Character.Character(name, 0, 0)
    return player_character


def load_user(name: str) -> Character:
    """
    Load the saved file for old user

    PARAM: name, string
    PRE CONDITION: User must have saved character file
    POST CONDITION: Succesfully load json file
    RETURN: Returns character that contains character information
    """

    user_continue = True

    while user_continue is True:

        try:
            filename = name + ".json"
            with open(filename, 'r') as f_obj:
                user = json.load(f_obj)

        except FileNotFoundError:
            return generate_character()
        else:
            player_character = Character.Character(user["name"], user["x_coord"], user["y_coord"])
            player_character.set_hp(user["hp"])
            print("Welcome Back!", user["name"], "hope you are ready!!!!")
            return player_character


def save_new_character(player_character: Character) -> None:
    """
    Save Character as json file

    PARAM: player_character, Character
    PRE CONDITION: User must properly quit to save the character
    POST CONDITION: Save character as json file
    RETURN: None
    """

    filename = player_character.name + ".json"
    char_info = player_character.__dict__
    with open(filename, 'w') as f_obj:
        json.dump(char_info, f_obj)


def cha_map(player_character: Character) -> None:
    """
    Draw a map on a console

    PARAM: player_character, Character
    PRE CONDITION: None
    POST CONDITION: User can view their current location
    RETURN: None
      """
    x_coord = player_character.get_x()
    y_coord = player_character.get_y()
    print("\n\n\n\nMAP \nMy Mission: What is ", player_character.get_mission(), "\n\n\n\n")
    for row in range(3):
        for column in range(3):
            if row == x_coord and column == y_coord:
                print('[', "#", ']' "\t", end=" ")

            else:
                print('[ ', ' ]'"\t", end=" ")
        print("\n")
    print("# --> Your current location")


def get_direction() -> str:
    """
      Get a direction from User

      PARAM: None
      PRE CONDITION: User must provide location by typing N,S,W,E
      POST CONDITION: None
      RETURN: Returns string that contains user direction
    """
    user_input = get_user_input("\n\n\n================================\n"
                                "where do you want to go?\n I know this cave has 9 rooms."
                                "N(north: moves up),W(west: moves left),S(south: moves down),E(moves right)\n"
                                "q (quit) if you quit, your mission will be re-set it\n"
                                "If you are not sure about your location, we can check the map.\n"
                                "The instruction on my map says... \npress enter to check map\n"
                                "=================================\n\n\n\n\n")
    return user_input


def move(player_character) -> list:
    """
    Move One location from Other location

    PARAM: player_character, Character
    PRE CONDITION: User must provide location by typing N,S,W,E
    POST CONDITION: User will move current location to another location.
    Return: Returns a list of two integer that contains user x and y coordinate
    """
    direction = get_direction()
    x_coord = player_character.get_x()
    y_coord = player_character.get_y()

    if direction.strip().lower() == 'w':
        if y_coord <= 0:
            print("sorry, you reached the end of the map, Let's go different direction.")

        else:
            y_coord -= 1
            player_character.set_y(y_coord)
            cha_map(player_character)
            next_move(player_character)
            return [x_coord, y_coord]

    elif direction.strip().lower() == "e":
        if y_coord >= 2:
            print("sorry, you reached the end of the map, Let's go different direction.")

        else:
            y_coord += 1
            player_character.set_y(y_coord)
            cha_map(player_character)

            return [x_coord, y_coord]

    elif direction.strip().lower() == 'n':
        if x_coord <= 0:
            print("sorry, you reached the end of the map, Let's go different direction.")
            cha_map(player_character)
        else:
            x_coord -= 1
            player_character.set_x(x_coord)
            cha_map(player_character)
            next_move(player_character)

            return [x_coord, y_coord]

    elif direction.strip().lower() == 's':
        if x_coord >= 2:
            print("sorry, you reached the end of the map, Let's go different direction.")
        else:
            x_coord = x_coord + 1
            player_character.set_x(x_coord)
            cha_map(player_character)
            next_move(player_character)

            return [x_coord, y_coord]

    elif direction == "":
        cha_map(player_character)

    elif direction.strip().lower() == 'q':
        player_character.set_quit(True)


def game() -> None:
    """
    Play a game

    Param: None
    PRE CONDITION: None
    POST CONDITION: User will play game until character dies or manually quit.
    Return:None
    """
    check = verify_user()
    if check.strip().lower() == 'y':
        player_character = generate_character()
    else:
        player_character = load_user(check)

    mission(player_character)
    cha_map(player_character)

    user_continue = True

    while user_continue is True:
        move(player_character)

        if player_character.get_hp() <= 0:
            print("DEAD...... Game Over")
            save_new_character(player_character)
            user_continue = False

        elif player_character.get_quit() is True:
            print("Thank you so much for playing my game!  Good Bye!")
            save_new_character(player_character)
            user_continue = False


def random_boolean() -> bool:
    """
    Generate random boolean

    Param:None
    PRE CONDITION: None
    POST CONDITION: None
    Return:Returns random boolean value
     >>> import random
    >>> random.seed(1)
    >>> random_boolean()
    False
    """
    ran_bool = bool(random.getrandbits(1))
    return ran_bool


def korean_translator(player_character: Character) -> None:
    """
    Get information of the first Korean letter

    PARAM: player_character, Character
    PRECONDITON: User must have their mission
    POST CONDITION: User acquire information of first Korean letter
    RETURNS:None
    """
    ran_bool = random_boolean()
    user_con = True
    while user_con is True:
        if ran_bool == 0:
            user_input = get_user_input("Wait! My translator gives me a signal ! the signal says 쿠, Do i need this\n"
                                        "information?? ...... y/n")

            if user_input.strip().lower() == 'y' and player_character.get_mission() == '쿠키':
                print("humm.. Interesting! It says 쿠 in Korean is Coo! ")
                player_character.set_mission_01(1)
                user_con = False
            elif user_input.strip().lower() == 'n':
                print("oh, this isn't what i need..")
                user_con = False

            elif player_character.get_mission() != '쿠키':
                print("Do I really need this?  I don't think my mission needs this information..")

            else:
                get_user_input("\n\n\nWait! My translator gives me a signal ! the signal says 쿠, Do i need this\n"
                               "information?? ...... y/n")

        if ran_bool == 1:
            user_input = get_user_input("Wait! My translator gives me a signal ! the signal says 캐, Do i need this\n"
                                        "information?? ...... y/n")
            if user_input.strip().lower() == 'y':
                print("humm.. Interesting! It says 캐 in Korean is Ca! ")
                player_character.set_mission_01(1)
                user_con = False
            elif user_input.strip().lower() == 'n':
                print("oh, This isn't what I need.. Let's move on..")
                user_con = False

            elif player_character.get_mission() != '캐나다':
                print("Do I really need this?  I don't think my mission needs this..")

            else:
                get_user_input("\n\n\nWait! My translator gives me a signal ! the signal says 캐, Do i need this\n"
                               "information?? ...... y/n")


def korean_translator_secondword(player_character: Character) -> None:
    """
      Get information of the second Korean letter
      PARAM: player_character, Character
      PRECONDITON: User must have know the information of the first Korean letter
      POST CONDITION: User acquire information of the second Korean letter
      RETURNS:None
      """
    ran_bool = random_boolean()
    user_con = True

    while user_con is True:
        if ran_bool == 0:
            user_input = get_user_input("Wait! I found something on my translator ! It says 키, Do i need this\n"
                                        "information?? ...... y/n")

            if user_input.strip().lower() == 'y':
                print("humm.. Interesting! It says 키 in Korean is kie!/\n"
                      "Oh!! 쿠키 is COOKIE!!")
                player_character.set_mission_02(2)
                user_con = False
                mission_complete(player_character)

            elif user_input.strip().lower() == 'n':
                print("oh, this isn't what i need..")
                user_con = False

            elif player_character.get_mission() != '쿠키':
                print("Do I really need this?  I don't think my mission needs this..")
            else:
                get_user_input("\n\n\nWait! I found something on my translator ! It says 키, Do i need this\n"
                               "information?? ...... y/n")

        if ran_bool == 1:
            user_input = get_user_input("Wait! I found something on my translator ! It says 나다, Do i need this\n"
                                        "information?? ...... y/n")
            if user_input.strip().lower() == 'y':
                print("humm.. Interesting! It says 나다 in Korean is nada!/\n"
                      "Oh!! 캐나다 is CANADA!")
                player_character.set_mission_02(2)
                user_con = False
                mission_complete(player_character)

            elif player_character.get_mission() != '캐나다':
                print("Do I really need this?  I don't think my mission needs this..")

            elif user_input.strip().lower() == 'n':
                print("oh, this isn't what i need..")
                user_con = False

            else:
                get_user_input("\n\n\nWait! I found something on my translator ! It says 나다, Do i need this\n"
                               "information?? ...... y/n")


def next_move(player_character: Character) -> int:
    """
    Get a next_move possible events for Character

    PARAM: player_character, Character
    PRECONDITON: User must have type E,W,S,N to move one direction to another direction.
    POST CONDITION: Depends on random die roll, user encounters monster, find information of missions
                     or hp increase by 1
    RETURNS: Returns random integer
     """
    die_roll = roll_a_die(1, 10)

    if die_roll == 1:
        monster_appear_user_choice(player_character)
        return die_roll

    elif die_roll == 2:
        if player_character.get_mission_01() == 0:
            korean_translator(player_character)
        elif player_character.get_mission_01() == 1:
            korean_translator_secondword(player_character)
        return die_roll

    else:
        if player_character.get_hp() < 10:
            player_character.increment()
            print("My new HP:", player_character.get_hp())


def monster_appear_user_choice(player_character: Character) -> None:
    """
    Encounter Monster.

    Param: player_character
    PRECONDITON: None
    POST CONDITION: User decide wheater they will fight or run away from the monsters
    RETURNS: None

    """
    enemy_monster = Monster.Monster()
    user_input = get_user_input("\n\n\nMonster appeared!!!!!! \n It slowly walking towards me, "
                                "I don't know what to do. The monster seems hungry, and wants to eat me as "
                                "dinner. Oh.. What should I do?..  (F:Fight, R: Run Away)\n\n\n")
    user_contin = True

    while user_contin is True:
        if user_input.strip().upper() == "F":
            attack(player_character, enemy_monster)
            user_contin = False

        elif user_input.strip().upper() == "R":
            run_away(player_character)
            user_contin = False
        else:
            user_input = get_user_input("\n\n\nMonster appeared!!!!!! \n It slowly walking towards me, "
                                        "I don't know what to do. The monster seems hungry, and wants to eat me as "
                                        "dinner. Oh.. What should I do?..  (F:Fight, R: Run Away)\n\n\n")


def run_away(player_character: Character) -> None:
    """
    Run away from the Monster

    Param: player_character, Character
    PRECONDITON: User decided to run away from the monter by typing r
    POST CONDITION: User run away from the monster or Monster attacks user from the back
    RETURNS: None
    """
    roll_die = roll_a_die(1, 10)

    if roll_die == 1:
        back_attack(player_character)
    else:
        print("FLEEEEE~ HAHAHA you can't catch me. Let's move on. I am so curious. I really need to find out\n"
              "what those word mean ! ")


def back_attack(player_character: Character) -> None:
    """
    Monster attacks from the back while user is running away

    Param: player_character, character
    PRECONDITON: User roll a die, and the value is 1
    POST CONDITION: Monster attacks user from the back
    RETURN : NONE
    """
    damage = roll_a_die(1, 4)
    hp = player_character.get_hp() - int(damage)
    player_character.set_hp(hp)
    print("While I was running away from ugly Evil monster, monster attacked my back...!!!!! How come..\n"
          "My NEW HP :", player_character.get_hp())


def attack(player_character: Character, enemy_monster: Monster) -> None:
    """
    Simulate fight between User and Monster

    Param:player_character, Character
          enemy_monster, Monster
    PRECONDITON: User decided to fight with Monster
    POST CONDITION: Fight goes until one side die.
    RETURN : NONE
    """
    match = True

    while match is True:
        char_attack = roll_a_die(1, 6)

        print("\n", player_character.get_name(), ":Fire Ball!!!!!!!!\nDAMAGE:", char_attack)
        hp = enemy_monster.get_hp()
        new_hp = hp - int(char_attack)
        enemy_monster.set_hp(new_hp)

        if enemy_monster.get_hp() <= 0:
            player_character.increment_kill()
            print("Agggggg..", enemy_monster.get_name(), "is DEAD... ",
                  "\nnumber of kill:", player_character.get_kill())
            match = False

        else:

            evil_monster_attack_me(player_character, enemy_monster)


def evil_monster_attack_me(player_character: Character, enemy_monster: Monster) -> None:
    """
    Monster attack back user

    Param:player_character, Character
          enemy_monster, Monster
    PRECONDITON: User attacked monster and monster is still alive
    POST CONDITION: Fight goes until one side die.
    RETURN : NONE
    """
    mon_attack = roll_a_die(1, 4)

    print("EVEIL MONSTER HP:", enemy_monster.get_hp(), "\n", enemy_monster.get_name(),
          ":HAHA, NICE TRY. It's MY turn hahahahhahahh", "\nEVIL MONSTER: ICE ARROW!!!!!!!!!!")
    hp = player_character.get_hp()
    new_hp = hp - int(mon_attack)
    player_character.set_hp(new_hp)
    print(enemy_monster.name, "DAMAGE:", mon_attack)

    if player_character.hp > 0:
        print("It's MY TURN. ARE YOU READY?")


def mission(player_character: Character) -> None:
    """
    Choose a mission of a day

    Param:player_character, Character
    PRECONDITON: User don't have any mission yet
    POST CONDITION: User have a mission that they need to work on
    RETURN : NONE
    """
    user_input = get_user_input("\nI am walking inside the cave. I stepped on something, oh.. I see two papers on the"
                                "floor.. I am going to pick up one, which one should i pick? (type 1 or 2)")
    user_continue = True

    while user_continue is True:

        if user_input == str(1):
            player_character.set_mission('쿠키')
            user_continue = False
            print("\nOn the Paper, it says 쿠키. ohh.. What is 쿠키?")

        elif user_input == str(2):
            player_character.set_mission('캐나다')
            user_continue = False
            print("\nOn the Paper, it says 캐나다. ohh.. What is 캐나다?")

        else:
            user_input = input("\nwhich one should i pick up? ")


def mission_complete(player_character: Character) -> None:
    """
    Complete a mission

    Param:player_character, Character
    PECONDITON: User collects all information of Korean word.
    POST CONDITION: User either quit for choose a new mission.
    RETURN : NONE
    """
    your_mission = player_character.get_mission_02()

    if your_mission == 2:
        print("good job! You made it!!!! Thank you so much for playing my Game, See you next_move Time!")
        player_character.set_quit(True)


def main():
    print("Welcome to my game!,\n\nBefore you play this game, I recommend you to change your console size. BIG "
          "BIG BIG\nThank you!!!! and Let's start!\n\n\n\n..... and I hope you don't speak Korean. If you are a\n"
          "Korean speaker, I am sorry. You WON''t find it fun.. ")

    print(" __  ____     __   _____          __  __ ______\n"
          "|  \/  \ \   / /  / ____|   /\   |  \/  |  ____|\n"
          "| \  / |\ \_/ /  | |  __   /  \  | \  / | |__   \n"
          "| |\/| | \   /   | | |_ | / /\ \ | |\/| |  __|  \n"
          "| |  | |  | |    | |__| |/ ____ \| |  | | |____ \n"
          "|_|  |_|  |_|     \_____/_/    \_\_|  |_|______|\n\nBY: Leah Younga Park, 박영아")
    # http://patorjk.com/software/taag/#p=display&f=Big&t=

    print("\n\nI know we all speak English, but How about Korean? Do you speak Korean? I don't believe so.\n"
          "You are walking inside a deep cave, there's 9 rooms in the cave. You saw a paper, you pick up a paper.\n"
          "a random Korean word is on the paper, you really want to know what it means. You are holding \n"
          "a translator, it doesn't give you any signal, but once You start to walk around, it might catch some\n"
          "signals or find something interesting. You are going to walk around the cave to find out\n "
          "what those words mean. At the same time a evil monster will show up and attack you... "
          "\n\nNow, Let's begin the game. ")
    game()


if __name__ == "__main__":
    import doctest

    main()
    doctest.testmod()
