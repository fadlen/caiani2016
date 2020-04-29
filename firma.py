# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:26:29 2020

@author: Daniel
"""

"""
Firm A (Konsumgüter)
"""

import consumeproduct

class FirmA:
    """
    Erstellen der Klasse Firma A
    """
    
    def __init__(self):
        self.account = 0
        self.labour = 1
        self.capitalgoods = 1
        self.numberconsumproduct = 0
        
    def create_consumproduct(self):
        consumeproduct.ConsumeProduct(self.labour, self.capitalproduct)
        
    def buy_labour(self):
        self.labour = 2
        
    def getLabour(self):
        return self.labour
    
    def getCapitalgoods(self):
        return self.capitalgoods