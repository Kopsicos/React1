# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 22:14:24 2019

@author: Lavan Balendran and Sasha Alexander Viktorovich Korol
"""
# Figure out more about BSTs
# Don't forget to import all the helper files into your main file

# I need to correct this
class Tree(): "Remember to import everything into the main file"
    def __init__(self, value, left = None, right = None):
        self.right = right
        self.left = left
        self.value = value
        
    def insert(self, fighter1, fighter2, fighter3, fighter4):
        """
        Inserts the fighters into the Nodes
        """
        self.left = Tree(fighter1)
        self.right = Tree(fighter2)
        self.left = Tree(fighter3)
        self.right = Tree(fighter4)
    
    def tournament_rankings(self): # Traverse through the list without adding anything
        """
        Traverses the list upwards without adding anything in order to know who is fighting who
        """
        if self.left == None:
            return self.value
        else: 
            sum1 = self.value
            sum1 = sum1 + int(self.left.tournament_rankings())
            sum1 = sum1 + int(self.right.tournament_rankings())
        return sum1
        
    def move_up(self, fighter1): 
        if self.health == 0:
            self.health + self.damage
            return fighter1
        
            
        
        
        
