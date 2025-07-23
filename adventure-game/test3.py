import random, time

#---- data ---


class _room:
    def __init__(self, name, description, doors, enemies=None):
        self.name = name
        self.description = description
        self.doors = doors
        self.enemies = enemies if enemies else []


class _enemy:
    def __init__(self, name, hp, max_hp, ability, damage, speed, death_text, is_alive):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.ability = ability
        self.damage = damage
        self.speed = speed
        self.death_text = death_text
        self.is_alive = is_alive


class _player:
    def __init__(self, position, hp, max_hp, moves):
        self.moves = moves
        self.position = position
        self.hp = hp
        self.max_hp = max_hp

    def is_dead(self):
        return self.hp <= 0

player = _player(2, 50, 50, moves := [{"name": "Tackle",  "damage": 10},{"name": "Fireball",  "damage": 15}])


bat = _enemy("bat", 8, 8, "bite", 8, 15, "The bat falls to the ground, dead, bleeding and limp.", True)
skeleton = _enemy("skeleton", 12, 12, "scratch", 12, 10, "The bones fall to the ground, clattering against the stone floor.", True)
slime = _enemy("slime", 15, 15, "suck", 15, 5, "The slime stops moving, but is still jiggly", True)

cellar = _room("the cellar", descriptions := ["You are under the ground, its dark, and dank", "The dirt floor is cold and there is a foul stench"], 1111)
dungeon = _room("the dungeon", descriptions := ["The smell of dried blood and tears fill the air, \nthe screams of pain still echo on these stone walls", "The remains of a man are chained to the crude stone wall."], 1111)
tower = _room("the tower", descriptions := ["The winding stairs ascend higher than you are brave enough to climb,\n the wind is howling through the windows", "The tower seems to sway in the storm, nauseating you, the winds sound like screams."], 1111)

rooms = [cellar, dungeon, tower]
enemies = [slime, skeleton, bat]

# funktioner enligt pseudokod nedan
def print_letters(word):
    typing_speed = 100
    for letter in word:
        print(letter, end='', flush=True)
        time.sleep(random.random()*10.0/typing_speed)
    time.sleep(0.5)


def show_overworld_menu(room):
    #print(type(player_position))
    print_letters(f"\nYou are in {room.name}.")
    print_letters("\n1. Look around")
    print_letters("\n2. Enter battle")
    print_letters("\n3. Change player position")
    print_letters("\n4. Exit game")
    print_letters("\n")
    choice = int(getInput())
    return choice

def init_battle(): 
    return True, False

def print_status(p_hp, enemy):
    status1 = (f"\nYour HP: {p_hp} Enemy HP: {enemy.hp}\n")
    print_letters(status1)
    status2 = ('What do you want to do?\n')
    print_letters(status2)

def show_menu(moves):
    for i,m in enumerate(moves):
        print_letters(f"{i+1}. {m['name']}\n")
        time.sleep(0.5)
    print_letters(f"{len(moves)+1}. Escape\n")
    time.sleep(0.5)
    return int(getInput())

def player_turn(choice, moves, e_hp):
    if choice <= len(moves):
        dmg = moves[choice-1]["damage"]
        e_hp -= dmg
        p_turn = (f"You used {moves[choice-1]["name"]} -")
        print_letters(p_turn)
        print(f" for {dmg} damage")
        time.sleep(0.5)
        return e_hp, False
    else: 
        print_letters("You got away safely\n")
        return e_hp, True

def check_end(p_hp, escaped, enemy):
    if escaped:       return "Escaped"
    if enemy.hp <= 0:  
        print_letters(f"{enemy.death_text}")
        enemy.is_alive = False
        return "Win"
    if p_hp <= 0:     return "Lose"
    return "Continue" #det finns  ett problem i check_end

def enemy_turn(p_hp, enemy):
    p_hp -= enemy.damage
    e_turn = (f"Enemy used {enemy.ability} - ")
    print_letters(e_turn)
    print(f" dealing {enemy.damage} damage\n")
    time.sleep(0.3)
    print()
    #print(type(e_turn))
    return p_hp

def show_rooms_menu():
    print_letters(f"\n Where do you want to go?")
    print_letters(f"\n1. Go to {rooms[0].name}")
    print_letters(f"\n2. Go to {rooms[1].name}")
    print_letters(f"\n3. Go to {rooms[2].name}\n")
    choice = int(getInput())
    return choice - 1

def battle_loop(p_hp):
    in_battle, esc = init_battle()
    enemy = enemies[player.position]
    print_letters(f"\nThere is a {enemy.name} in here..")
    print_letters(f"\nThe {enemy.name} tries to make a {enemy.ability} attack!")
    print_letters(f"\nCan you resist the {enemy.ability}?")
    while in_battle:
        print_status(p_hp, enemy)
        choice = show_menu(player.moves)
        enemy.hp, esc = player_turn(choice, player.moves, enemy.hp)
        status = check_end(p_hp, esc, enemies[player.position])
        if status != "Continue": break
        p_hp = enemy_turn(p_hp, enemy)
        status = check_end(p_hp, esc, enemies[player.position])
        if status != "Continue": break
    print("\nBattle ended. You", status)
    return p_hp

def getInput():
    has_chosen = False
    while has_chosen == False:
        choice = input("> ")
        if str(choice) == "":
            print_letters("Make a Choice!\n")
        elif choice.isdigit() == False:
            print_letters("Choose a number!!\n")
        else:
            has_chosen = True
            return choice

def gameReset():

    return

def game_loop():

    running = True
    player_hp = player.max_hp
    descriptions = 0

    while running:

        current_room = rooms[player.position]
        choice = show_overworld_menu(current_room)

        if choice == 1:

            print_letters(f"\n{current_room.description[descriptions]}.\n")
            #print(" TEST descrptions: " + len(current_room.description))
            if descriptions < len(current_room.description) - 1:
                descriptions = descriptions + 1
            # Slumpchans att fiende dyker upp

            if random.random() < 0.3:
                if enemies[player.position].is_alive:
                    player_hp = battle_loop(player_hp)

            else:
                print_letters("\n....\n")

        elif choice == 2:
            if enemies[player.position].is_alive:
                print_letters("\nYou pick a fight!\n")
                player_hp = battle_loop(player_hp)
            else:
                print_letters("\n There's no enemy in this room.")

        elif choice == 3:
            player.position = show_rooms_menu()
            descriptions = 0


        elif choice == 4:
            print_letters("Spelet avslutas.\n")
            running = False

        else:
            print_letters("Illegal choice.")


if __name__ == "__main__":
    print(">>> " + rooms[2].name)
    print_letters("Welcome to the game! \n")
    game_loop()

    
