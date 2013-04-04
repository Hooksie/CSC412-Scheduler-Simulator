'''
Created on Apr 1, 2013

@author: Matt
'''

from random import random
from math import log

class ExponentialDistribution(object):
    
    def __init__(self, rate):
        self.rate = rate
    
    def getNextRate(self):
        return -log(random()) / self.rate