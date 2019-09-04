#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:16:26 2019

@author: samuel
"""

# Number
class Number():
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        return int(self.value)
    
# Operations
class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
class Inc(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()
    
class Dec(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()
    