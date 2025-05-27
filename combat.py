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

    def take_damage(self, amount, accuracy, blocking):
        hit_or_not = random.randint(0, 100)
        critical_hit = random.randint(0, 100)

        if not hit_or_not > accuracy:

            if blocking:
                amount = round(amount/2)

            if critical_hit < 5:
                self.hp -= amount
                if self.hp < 0:
                    self.hp = 0


                return True, "Critical hit!"

            else:
                self.hp -= amount
                if self.hp < 0: self.hp = 0

                return True, None
        else:
            return True, f"{self.name} evaded the attack!"



    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        return False, f"{self.name} drank a health potion and regained {amount} hp!"


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


def bottom_box(action, attacker, receiver, message):
    box_length = 60
    print(f"┌{"─" * box_length}┐")
    if action:
        print(f"│ {attacker.name} attacked {receiver.name + ".".ljust(box_length - (len(attacker.name) + len(receiver.name) + 12))} │")
    if message: print(f"│ {message.ljust(box_length - 2)} │")
    print(f"└{"─" * box_length}┘")
    input()


def player_turn(player, enemy):
    while True:
        box_length = 10
        print(f"┌{"─" * box_length}┐")
        print(f"│ [A]ttack │")
        print(f"│ [H]eal   │")
        print(f"│ [B]lock  │")
        print(f"└{"─" * box_length}┘")
        user_input = input("> ")
        clear_terminal()

        if enemy.speed > player.speed:
            combat_character_ui(player, enemy)
            if user_input == "B":
                enemy_turn(player, enemy, blocking = True)
                clear_terminal()
                return False
            else:
                enemy_turn(player, enemy, blocking = False)
            clear_terminal()

            if player.hp < 0:
                return "yes"

        if user_input == "A":
            # change = 1
            # message = None
            #
            # while change != player.attack:
            #     combat_character_ui(player, enemy)
            #     message = enemy.take_damage(change, player.accuracy, blocking=False)
            #     change += 1
            #     clear_terminal()


            combat_character_ui(player, enemy)
            action, message = enemy.take_damage(player.attack, player.accuracy, blocking = False)
            clear_terminal()

            combat_character_ui(player, enemy)
            bottom_box(action, player, enemy, message)

            clear_terminal()
            combat_character_ui(player, enemy)

            return False
        if user_input == "B":
            return True

        elif user_input == "H":
            combat_character_ui(player, enemy)
            action, message = player.heal(5)

            clear_terminal()
            combat_character_ui(player, enemy)
            bottom_box(action, player, enemy, message)



            clear_terminal()
            combat_character_ui(player, enemy)

            return False
        else:
            clear_terminal()
            combat_character_ui(player, enemy)


def enemy_turn(player, enemy, blocking):

    if blocking:

        action, message = player.take_damage(enemy.attack, enemy.accuracy, blocking=True)
        message = f"{player.name} blocked!"
    else:
        action, message = player.take_damage(enemy.attack, enemy.accuracy, blocking=False)

    clear_terminal()
    combat_character_ui(player, enemy)
    bottom_box(action, enemy, player, message)


def combat(player, enemy):
    while True:

        combat_character_ui(player, enemy)
        blocking = player_turn(player, enemy)

        death = dead(player, enemy)
        if death == "yes":
            break

        if player.speed > enemy.speed:
            enemy_turn(player, enemy, blocking)

        death = dead(player, enemy)
        if death == "yes":
            break

        clear_terminal()


def dead(player, enemy):
    if enemy.hp <= 0 or player.hp <= 0:
        clear_terminal()
        combat_character_ui(player, enemy)

        if player.hp <= 0:

            message = f"You lost against {enemy.name}"


        else:
            message = f"You defeated {enemy.name}!"

        bottom_box(None, player, enemy, message)
        clear_terminal()

        return "yes"
    return "no"

while True:
    combat(knight, enemy_dict[random.choice(enemy_list)])
    knight.hp = 30


