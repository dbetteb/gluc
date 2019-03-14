# !/usr/bin/env python3
# coding: utf-8

import pandas as pd
import numpy as np
from dataclasses import dataclass, field 
from typing import List
from dateutil.parser import parse
from misc import monthdic



def loadgluc(filename):
    df = pd.read_csv(filename)
    return df['Average30Days'].values

def loaddate(filename):
    df = pd.read_csv(filename)
    return [parse(date, dayfirst=True) for date in df['Date'].values]

def convertgluc(gluc, coeff = 1/28.7, intercept = 46.7/28.7):
    return coeff*gluc + intercept



@dataclass
class GlucConverter:
    '''Class for conversion'''
    name: str
    filename: str
    formula: List[float] = field(default_factory=lambda : [1/28.7, 46.7/28.7])

    
    def getgluc(self) -> List:
        self.gluc = loadgluc(self.filename)

    def getdate(self) -> List:
        self.date = loaddate(self.filename)

    def gethba1c(self) -> List:
        if hasattr(self, 'gluc') == True:
            self.hba1c = convertgluc(self.gluc, coeff = self.formula[0], intercept = self.formula[1])
            print(f"{self.name} GlucConverter formula is {self.formula[0]}*glyc+ {self.formula[1]}")
        else:
            print(f"{self.name} GlucConverter has no gluc")
