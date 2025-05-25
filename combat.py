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

    def take_damage(self, amount, accuracy):
        hit_or_not = random.randint(0, 100)

        if not hit_or_not > accuracy:

            self.hp -= amount
            print(f"{self.name} took {amount} damage!")
        else:
            print(f"{self.name} evaded the attack!")

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.name} drank a health potion and regained {amount} hp!")


knight = Character("Player", "Knight", 30, 5, 80, 7)
goblin = Character("Enemy", "Goblin", 15, 3, 50, 9)


def display_hp(player, enemy):
    print(f"                      {enemy.name}: {enemy.hp}")
    print(f"{player.name}: {player.hp}\n")

def combat_character_info_ui(character_type, name, hp, max_hp):
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
        print(f"│HP {hp_bar.ljust(box_length + (len(hp_bar) - bars_amount))} {hp_info} │")
        print(f"└{"─" * (box_length + 10)}┘")
    else:
        print(f"{" " * (box_length + 10)}{name}")
        print(f"{" " * (box_length + 10)}┌{"─" * (box_length + 10)}┐")
        print(f"{" " * (box_length + 10)}│HP {hp_bar.ljust(box_length + (len(hp_bar) - bars_amount))} {hp_info.rjust(5)} │")
        print(f"{" " * (box_length + 10)}└{"─" * (box_length + 10)}┘")



def combat_character_ui(player, enemy):
    combat_character_info_ui(enemy.character_type, enemy.name, enemy.hp, enemy.max_hp)
    combat_character_info_ui(player.character_type, player.name, player.hp, player.max_hp)



def player_turn(player, enemy):
    while True:

        user_input = input("[A]ttack\n[H]eal\n> ")
        clear_terminal()

        if user_input == "A":
            combat_character_ui(player, enemy)

            print(f"{player.name} attacked {enemy.name}.")
            enemy.take_damage(player.attack, player.accuracy)
            input()

            clear_terminal()
            combat_character_ui(player, enemy)

            return
        elif user_input == "H":
            combat_character_ui(player, enemy)

            player.heal(5)
            input()

            clear_terminal()
            combat_character_ui(player, enemy)

            return

def enemy_turn(player, enemy):
    print(f"{enemy.name} attacked {player.name}.")
    player.take_damage(enemy.attack, enemy.accuracy)
    input()

def combat(player, enemy):
    while True:
        combat_character_ui(player, enemy)
        player_turn(player, enemy)

        if enemy.hp <= 0 or player.hp <= 0:
            clear_terminal()
            print(f"You defeated {enemy.name}!")
            input()
            break

        enemy_turn(player,enemy)

        if enemy.hp <= 0 or player.hp <= 0:
            clear_terminal()
            print(f"You defeated {enemy.name}!")
            input()
            break

        clear_terminal()

combat(knight, goblin)


