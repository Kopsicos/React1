# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:41:53 2019

@author: Lavan Balendran and Sasha Alexander Viktorovich Korol
"""


class Start:
    def __init__(self, health, special, attack, block, agility, player_name, character_list):
        self.health = health
        self.player_name = player_name
        self.health = health
        self.attack = attack
        self.special = special
        self.block = block
        self.agility = agility
        self.character_list = character_list
    
    def starting_screen(self):
        print("Choose your Character from the Selection: Copy their names down")
        print("Ishiguro?")
        print("Stats: AAAA")
        print("Risotto Nero?")
        print("Stats: AAAA")
        print("Forto?")
        print("Stats: AAAA")
        print("Piano?")
        print("Stats: AAAA")
        if self.player_name == "Ishiguro":
            print("You have chosen Ishiguro")    
        elif self.player_name == "Risotto Nero":
            print("You have chosen Risotto Nero")
        elif self.player_name == "Forto":
            print("You have chosen Forto")
        elif self.player_name == "Piano":
            print("You have chosen Piano")
        else:
            print("This is not a valid character")
     
    def menu(self):
        self.character_list = ["Ishiguro", "Risotto Nero", "Forto", "Piano"]
        self.character_list.remove(self.player_name)
        return self.character_list
        
class Attack(Start):
    def __init__(self, attack_choice, damage):
        self.attack_choice = attack_choice
        self.damage = damage
    
    def choose(self):
        print("Mini-black Holes")
        print("Increase Gravity")
        print("Change Gravity Direction")
        print("Levitation")
        self.attack_choice = input("Choose which attack you will use?")
                    
    def ishiguro_attacks(self):
        if self.attack == "Mini-black Holes":
            self.damage = 150
        if self.attack == "Increase Gravity":
            self.damage = 15
            self.agility = self.agility - 20
            self.block = self.block + 20
        if self.attack == "Change Gravity Direction":
            self.damage = 20
        if self.attack == "Levitation":
            self.damage = 5
            self.agility = self.agility - 10
            self.block = self.block - 10
            

class Health(Attack):
    def __init__(self, damage):
        self.damage = damage
    
    def start_health(self):
        full = self.health
        return full
    
    def damage(self):
        return self.health - self.damage  #Come back here later, code doesn't work, attacks itself
        
    def death(self):
        if self.health == 0:
            print("You have lost!")
        
        
        
        
        
        