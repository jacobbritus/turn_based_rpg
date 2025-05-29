import os
import random
from colorama import Fore


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


class Character:
    def __init__(self, character_type, name, hp, attack, accuracy, speed):
        self.character_type = character_type
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.accuracy = accuracy
        self.speed = speed

    def clamp_hp(self):
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        elif self.hp < 0:
            self.hp = 0

    def take_damage(self, amount, accuracy, blocking):
        hit_or_not = random.randint(0, 100)
        critical_hit = random.randint(0, 100)

        if not hit_or_not > accuracy:

            if blocking:
                amount = round(amount/2)

            if critical_hit < 5:
                self.hp -= amount
                self.clamp_hp()

                return "Critical hit!"

            else:
                self.hp -= amount
                self.clamp_hp()

                return None
        else:
            return f"{self.name} evaded the attack!"



    def heal(self, amount):
        self.hp += amount
        self.clamp_hp()
        return f"{self.name} drank a health potion and regained {amount} hp!"





knight = Character(character_type = "Player", name = "Knight", hp = 30, attack = 5, accuracy = 80, speed = 7)

enemy_dict = {
    "Goblin": Character(character_type="Enemy", name="Goblin", hp=15, attack=3, accuracy=70, speed=8),
    "Orc": Character(character_type="Enemy", name="Orc", hp=30, attack=7, accuracy=50, speed=3),
    "Skeleton": Character(character_type="Enemy", name="Skeleton", hp=20, attack=5, accuracy=60, speed=6),
    "Slime": Character(character_type="Enemy", name="Slime", hp=10, attack=2, accuracy=80, speed=2),
    "Bandit": Character(character_type="Enemy", name="Bandit", hp=18, attack=6, accuracy=75, speed=9),
    "Dark Mage": Character(character_type="Enemy", name="Dark Mage", hp=22, attack=9, accuracy=65, speed=5),
    "Troll": Character(character_type="Enemy", name="Troll", hp=40, attack=10, accuracy=45, speed=2),
    "Wolf": Character(character_type="Enemy", name="Wolf", hp=16, attack=4, accuracy=80, speed=10),
    "Vampire": Character(character_type="Enemy", name="Vampire", hp=25, attack=8, accuracy=70, speed=7),
    "Assassin": Character(character_type="Enemy", name="Assassin", hp=12, attack=10, accuracy=85, speed=12),
    "Giant Spider": Character(character_type="Enemy", name="Giant Spider", hp=22, attack=6, accuracy=60, speed=8),
    "Wraith": Character(character_type="Enemy", name="Wraith", hp=18, attack=7, accuracy=75, speed=9)
}

enemy_list = [enemy for enemy in enemy_dict]



def combat_character_ui_maker(character_type, name, hp, max_hp):
    box_length = 20

    hp_info = str(hp) + "/" + str(max_hp)

    #displayed tags


    percentage = (hp / max_hp * 100)
    bars_amount = round(box_length * (percentage / 100))

    if percentage > 75:
        bar_color = Fore.GREEN
    elif percentage > 25:
        bar_color = Fore.YELLOW
    else:
        bar_color = Fore.RED

    hp_bar = bar_color + "█"*bars_amount + Fore.RESET

    if character_type == "Player":
        print(name)
        print(f"┌{"─" * (box_length + 10)}┐")
        print(f"│HP {hp_bar.ljust(box_length + (len(hp_bar) - bars_amount))} {hp_info.rjust(5)} │")
        print(f"└{"─" * (box_length + 10)}┘")
    else:
        print(f"{" " * (box_length + 10)}{name}")
        print(f"{" " * (box_length + 10)}┌{"─" * (box_length + 10)}┐")
        print(f"{" " * (box_length + 10)}│HP {hp_bar.ljust(box_length + (len(hp_bar) - bars_amount))} {hp_info.rjust(5)} │")
        print(f"{" " * (box_length + 10)}└{"─" * (box_length + 10)}┘")



def combat_character_ui(player, enemy):
    combat_character_ui_maker(enemy.character_type, enemy.name, enemy.hp, enemy.max_hp)
    combat_character_ui_maker(player.character_type, player.name, player.hp, player.max_hp)


def bottom_box(player, enemy, message_one, message_two):
    #remove action, if message 2 clear terminal and show the message
    box_length = 60

    print(f"┌{"─" * box_length}┐")
    print(f"│ {message_one.ljust(box_length - 2)} │")
    print(f"└{"─" * box_length}┘")
    input()

    if message_two:
        clear_terminal()
        combat_character_ui(player, enemy)
        print(f"┌{"─" * box_length}┐")
        print(f"│ {message_two.ljust(box_length - 2)} │")
        print(f"└{"─" * box_length}┘")
        input()



# it'll be easy to add menu options info with this:
def combat_menu_options(player, enemy):
    while True:
        box_length = 10
        print(f"┌{"─" * box_length}┐")
        print(f"│ [A]ttack │")
        print(f"│ [H]eal   │")
        print(f"│ [B]lock  │")
        print(f"└{"─" * box_length}┘")
        user_input = input("> ")

        if user_input in ["A", "H", "B"]:
            clear_terminal()
            return user_input
        else:

            update_screen(player, enemy)

def speed_check(player, enemy):
    if player.speed > enemy.speed:
        return "player"
    elif enemy.speed > player.speed:
        return "enemy"
    else:
        choices = ["enemy", "player"]
        random.shuffle(choices)
        return choices[0]


def player_turn(user_input, player, enemy):
        combat_character_ui(player, enemy)

        if user_input == "A":
            # enemy gets attacked, terminal clears and updated enemy's hp and bottom box message gets displayed.
            option_message = f"{player.name} attacked."

            message = enemy.take_damage(player.attack, player.accuracy, blocking = False)
            update_screen(player, enemy)
            bottom_box(player, enemy, option_message, message)

        if user_input == "B":
            pass

        elif user_input == "H":
            option_message = f"{player.name} used a healing potion."

            message = player.heal(5)

            update_screen(player, enemy)
            bottom_box(player, enemy, option_message, message)

        clear_terminal()


def enemy_turn(player, enemy, blocking):
    combat_character_ui(player, enemy)

    option_message = f"{enemy.name} attacked."

    if blocking:
        message = player.take_damage(enemy.attack, enemy.accuracy, blocking=True)

        #if attack wasn't evaded
        if not message: message = f"{player.name} blocked!"
    else:
        message = player.take_damage(enemy.attack, enemy.accuracy, blocking=False)

    update_screen(player, enemy)
    bottom_box(player, enemy, option_message, message)

    clear_terminal()

def combat2(player, enemy):
    while True:
        first_turn = speed_check(player, enemy)
        combat_character_ui(player, enemy)
        user_input = combat_menu_options(player, enemy)

        blocking = True if user_input == "B" else False

        if first_turn == "player":
            player_turn(user_input, player, enemy)
            if death_check(player, enemy): break
            enemy_turn(player, enemy, blocking)
        elif first_turn == "enemy":
            enemy_turn(player, enemy, blocking)
            if death_check(player, enemy): break
            player_turn(user_input, player, enemy)

        if death_check(player, enemy): break


def death_check(player, enemy):
    if enemy.hp <= 0 or player.hp <= 0:
        update_screen(player, enemy)


        message = f"You lost against {enemy.name}." if player.hp <= 0 else f"You defeated {enemy.name}."


        bottom_box(player, enemy, message, None)
        clear_terminal()

        return True
    return False


def update_screen(player, enemy):
    clear_terminal()
    combat_character_ui(player, enemy)


while True:
    combat2(knight, enemy_dict[random.choice(enemy_list)])
    knight.hp = knight.max_hp




