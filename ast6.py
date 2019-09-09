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
    
class Inclination():
    def __init__(self, value):
        self.value = value
    
    def eval(self):
        if int(self.value) >= 15:
            return print("Peligro")
        return print("Safe")

class Call():
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def eval(self, procedures):
        arr = procedures
        if self.value == None:
            i = -1
            for x in procedures:
                i += 1
                if x.name == self.name:
                    if arr[i].value == None:
                        arr1 = procedures[i]
                        for x in arr1.array:
                            try:
                                x.eval(procedures)
                            except:
                                print(x.eval())
                        return 
            print("El procedimiento llamado no existe")
        self.value.reverse()
        i = -1
        for x in procedures:
            i += 1
            if x.name == self.name:
                if len(self.value) == arr[i].len:
                    arr1 = procedures[i]
                    for x in arr1.array:
                        try:
                            x.eval(procedures)
                        except:
                            print(x.eval())
                    return 
        print("El procedimiento llamado no existe")
    
class Import():
    def __init__(self, rute):
        self.rute = rute
        
    def eval(self):
        return print(self.rute)
        
class Procedure():
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.array = []
        self.declaration = []
        if value != None:
            self.value.reverse()
            self.len = len(self.value)
        else:
            self.len = None
        
    def eval(self):
        return print(self.name + " con " + str(self.value))