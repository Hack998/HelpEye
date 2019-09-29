#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 09:59:29 2019

@author: samuel
"""

class Verificacion():
    def eval(self, o):
        if o.isdigit() == True:
                o = int(o)
                if o < 0:
                    print("El dato es negativo")
                    return False
                return True
        else:
            print("Ingrese numeros")
            return False
        