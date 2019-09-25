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
    
#Declare Variable Class
class Variable():
    def __init__(self, name, value=None):
        self.name = name 
        self.value = value 
    
class Inclination():
    def __init__(self, value):
        self.value = value
    
    def eval(self):
        if int(self.value) >= 15:
            return "Peligro"
        return "Safe"

class Brightness():
    def __init__(self, value):
        self.value = value
    def eval(self):
        if int(self.value) >= 15:
            return print("Very bright")
        elif int(self.value) <= 0:
            return print("Very dark")
        else:
            return print("Safe")

class Move():
    def __init__(self, value):
        self.value = value
    def eval(self):
        if int(self.value) >= 15:
            return print("Peligro")
        return print("Safe")

class Vibration():
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

class For():
    def __init__(self, value):
        self.value = value
    def eval(self, procedures):
        while(self.value > 0):
            for x in procedures:
                try:
                    x.eval(procedures)
                except:
                    print(x.eval())
                    return
            else:
                print("El procedimiento no puede ser ciclado")
            self.value -= 1
        else:
            print("Ciclo terminado")

class FEnd():
    def __init__(self, value = None):
        self.value = value
    def eval(self):
        return print("Ciclos cerrados: " + self.value)
    
class Import():
    def __init__(self, rute):
        self.rute = rute
        
    def eval(self):
        return 
        
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