# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 19:00:29 2019

@author: Lavan Balendran and Sasha Alexander Viktorovich Korol
"""

class character:
    def __init__(self,character_name1, health1, strength1, agility1, block1, special1, attack11, attack12, attack13, attack14):
        """
        Initializes the Character Class
        """
        self.character_name = character_name1
        self.health = health1
        self.strength = strength1
        self.agility = agility1
        self.block = block1
        self.special = special1
        self.attack1 = attack11
        self.attack2 = attack12
        self.attack3 = attack13
        self.attack4 = attack14

    def take_damage(self, opponent_attack):
        self.health = self.health - opponent_attack

# You don't need to copy the above, it's only so that I wouldn't get errors

class Mr_Park(character):
    def stats(self):
        """
        Initializes the Mr. Park Class
        """
        self.character_name = "Mr. Park"
        self.health = 600
        self.strength = 400
        self.agility = 400
        self.block = 400
        self.special = 400
        self.attack1 = int
        self.attack2 = int
        self.attack3 = int
        self.attack4 = int 
        
    def show_attacks(self):
        """
        Shows what attacks Mr. Park is capable of
        """
        print("Attacks:")
        print('1. Armed Drones: 15') 
        print('2. Wall-mounted Machine Guns: 5')
        print('3. Neurotoxin: 10')
        print('4. Spike Plates: 5')
        # Second stage attacks
        print("1. Plasma Cannon: AAA")
        print("2. Crush: AAA")
        print("3: Retractable Blade: AAA")
        print("4: Homing Missiles: AAA")
        # Third stage attacks
        print("1. Aimbot: AAA")
        print("2. Telekinesis: AAA")
        print("3: Critical Hit: AAA")
        print("4: Energy Projection: AAA")
        

    def show_stats(self):
        """
        Shows Mr. Park's stats
        """
        print("Name: Mr. Park") 
        print("Health: 600")
        print("Strength: 400")
        print("Agility: 400")
        print("Block: 400")
        print("Special: 400")
        print("Be careful! He's quite powerful")

    def second_stage(self):
        """
        Once Mr. Park reaches 2/3 of his health, he will become more powerful
        """
        if self.health <= 400:
            print("Mr. Park has just summoned a mech, things are going to get harder")
            self.strength = 500
            self.block = 500
    
    def third_stage(self): 
        """
        Once Mr. Park reaches 1/3 of his health, he will become even more powerful
        """
        if self.health <= 200:
            print("Mr. Park has just entered God-mode, you're finished")
            self.agility = 500
            self.special = 500
            
    def defeat(self):
        """
        Once Mr. Park is defeated, the player is congratulated for their victory
        """
        if self.health <= 0:
            print("Congratulations! You have emerged victorious against all odds")
        
        
        
        
        
        