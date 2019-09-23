#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:02:45 2019

@author: samuel
"""

from lexer6 import Lexer
from parser6 import Parser


path = '/home/samuel/Escritorio/Compi/ProyectoPrueba/eye/input.txt'
data = open(path,'r')

text_input = data.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens)