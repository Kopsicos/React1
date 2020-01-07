# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:46:44 2019

@author: Lavan Balendran and Sasha Alexander Viktorovich Korol
"""
# This is where we code for the Reward for each fight

class Reward:
    def __init__(self, health, special, attack, block, agility):
        """
        Most of this is placeholder, make sure to remember to to import things into each other
        """
        self.health = health
        self.attack = attack
        self.special = special
        self.block = block
        self.agility = agility
    
    def class_improvements(self):
        if self.health == 0: # The enemy's health is zero
            upgrade = input("Which stat would you like to upgrade!:") # Print stats
            if upgrade == "Health":
                print("You have upgraded your health by 100 points")
                return self.health + 100
            elif upgrade == "Special":
                print("You have upgraded your special by 100 points")
                return self.special + 100
            elif upgrade == "Attack":
                print("You have upgraded your attack by 100 points")
                return self.attack + 100
            elif upgrade == "Block":
                print("You have upgraded your block by 100 points")
                return self.block  + 100
            elif upgrade == "Agility":
                print("You have upgraded your agility by 100 points")
                return self.agility + 100
        
        
        
        
        
        
        
        
        
        
        
