# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:27:50 2020

@author: Daniel
"""

"""
Modell
"""
import households
import banks
import state
import centralbank
import firma

class Model:
    def __init__(self, numberhh, numberbanks, numberfirma):
        self.numberhh = numberhh
        self.numberbanks = numberbanks
        self.numberfirma = numberfirma
        self.year = 0
    #Creating Agents
    def create_hh(self):
        """
        Erstellen von Haushalten aus der Klasse Household
        
        Returns
        Liste aller Haushalte in householdslist        
        None.

        """
        self.householdslist = list()
        print("Creating households ...", end="")
        for i in range(self.numberhh):
            self.householdslist.append(households.Households())
        print("Complete!")
    
    
    def create_banks(self):
        """
        Erstellen von Geschäftsbanken

        Returns
        -------
        None.

        """
        
        self.banklist = list()
        print("Creating business banks... ", end="")
        for i in range(self.numberbanks):
            self.banklist.append(banks.Banks())
        print("Complete!")
        
    def create_state(self):
        """
        Erstellen des Staates
        """
        
        self.state = state.State()
    
    def create_centralbank(self):
        """
        Erstellen von Centralbanks

        Returns
        -------
        None.

        """
        
        self.centralbank = centralbank.CentralBank()
        
    def create_firma(self):
        """
        Erstellen von Firmen, die Konsumgüter herstellen

        Returns
        -------
        None.

        """
        self.firmalist = list()
        print("Creating Firms of Type A...", end="")
        for i in range(self.numberfirma):
            self.firmalist.append(firma.FirmA())
        print("Complete!")
            
    #Creating Markets
    
    def labourmarket(self):
        self.householdslist.    
    