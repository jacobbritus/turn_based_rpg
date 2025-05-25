import os
import random

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


class Character:
    def __init__(self, name, hp, attack, accuracy):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.accuracy = accuracy

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


knight = Character("Knight", 30, 5, 80)
goblin = Character("Goblin", 15, 3, 50)


def display_hp(player, enemy):
    print(f"                      {enemy.name}: {enemy.hp}")
    print(f"{player.name}: {player.hp}\n")

# while True:
#     display_hp(knight, goblin)
#
#     user_input = input("\n1. Attack\n2. Heal\n> ")
#
#     if user_input == "1":
#         goblin.take_damage(knight.attack)
#     elif user_input == "2":
#         knight.heal(5)
#
#     input()
#     knight.take_damage(goblin.attack)
#     input()
#
#     if goblin.hp <= 0 or knight.hp <= 0:
#         break
#
#     clear_terminal()


def player_turn(player, enemy):
    while True:

        user_input = input("[A]ttack\n[H]eal\n> ")
        clear_terminal()

        if user_input == "A":
            display_hp(knight, goblin)

            print(f"{player.name} attacked {enemy.name}.")
            enemy.take_damage(player.attack, player.accuracy)
            input()

            clear_terminal()
            display_hp(knight, goblin)

            return
        elif user_input == "H":
            display_hp(knight, goblin)

            player.heal(5)
            input()

            clear_terminal()
            display_hp(knight, goblin)

            return

def enemy_turn(player, enemy):
    print(f"{enemy.name} attacked {player.name}.")
    player.take_damage(enemy.attack, enemy.accuracy)
    input()

def combat(player, enemy):
    while True:
        display_hp(player, enemy)
        player_turn(player, enemy)
        enemy_turn(player,enemy)

        if enemy.hp <= 0 or player.hp <= 0:
            clear_terminal()
            print(f"You defeated {enemy.name}!")
            input()
            break

        clear_terminal()

combat(knight, goblin)

