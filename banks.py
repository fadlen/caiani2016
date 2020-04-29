# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:37:50 2020

@author: Daniel
"""

"""
Banken
"""

class Banks:
    """
    Klasse Banken
    """
    
    def __init__(self):
        self.account = 0
        self.girointerestrate = 0.01
        self.creditinterestrate = 0.05
    
    #def customers(self):
        #Ergebnisse aus dem depositmarket
        
    
    #Return-Methoden
    def getGirointeresrate(self):
        return self.girointerestrate
    
    def getCreditinterestrate(self):
        return self.creditinterestrate