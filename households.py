# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:37:20 2020

@author: Daniel
"""

"""
Haushalte
"""


import numpy as np


class Households:
    
    def __init__(self):
        self.workingday = 254
        self.income = 0
        self.guthaben = 0
        self.wages = 0
        self.daywage = 5
        self.job = False
    
    def income(self):
        self.income = 0
    
    def consume(self):
        self.consume = 
    
    def savings(self):
        self.savings = 0
        
    def sell_labour(self):
        return self.daywage

    def scan_labourmarket(self):
        labourmarket.labourprice >= self.minwage:
            sell_labour()
        return self.job = False





    #Return-Methoden 
    def getJob(self):
        return self.job
        
    def getIncome(self):
        return self.income
    
    def getWages(self):
        return self.wages
    
    def getDaywage(self):
        retun self.daywage
        
    def getGuthaben(self):
        return self.guthaben