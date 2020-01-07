# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:31:19 2019

@author: Lavan Balendran and Sasha Alexander Viktorovich Korol
"""

def after_effects(self, health, special, attack, block, agility): # Put this into a class
    #Ishiguro
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
    #Risotto Nero
    if self.attack == "Lightning Bolt":
        self.damage = "Insert Number here"
        self.agility = self.agility - 10
    if self.attack == "Induced Magnetism":
        self.damage = "Insert Number here"
        self.agility = self.agility - 15
    if self.attack == "Bright Flash":
        self.damage = "Insert Number here"
        self.agility = self.agility - 15
        self.block = self.block - 15
    #Forto
    if self.attack == "Compression":
        self.damage = "Insert Number here"
        self.agility = self.agility - 20
        self.block = self.block + 10  
    if self.attack == "Glue":
        self.damage = "Insert Number here"
    if self.attack == "Explosion":
        self.damage = "Insert Number here"
    #Piano   
    if self.attack == "Radiation":
        self.damage = "Insert Number here"
        self.special = self.special - 10
        self.attack = self.block - 5
    if self.attack == "Nuclear Decay":
        self.damage = "Insert Number here"
        self.attack = self.attack - 10
        self.agility = self.agility - 5
    if self.attack == "Neutrino Rain":
        self.damage = "Insert Number here"
        self.block = self.block - 10
        self.special = self.special - 10

