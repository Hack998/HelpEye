#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:46:33 2019

@author: samuel
"""

from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()
        
    def _add_tokens(self):
        # Parenthesis
        self.lexer.add('OPEN_PAREN',r'\(')
        self.lexer.add('CLOSE_PAREN',r'\)')
        # Comma
        self.lexer.add('COMMA', r'\,')
         # Comma
        self.lexer.add('POINT', r'\.')
        # Semi Colon
        self.lexer.add('SEMI_COLON',r'\;')
        #Equal simbol
        self.lexer.add('EQUAL', r'\=')
        #Declare
        self.lexer.add('DECLARE', r'DECLARE')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Ignore spaces
        self.lexer.ignore('\s+')
        # Funciones
        # Import
        self.lexer.add('IMPORT',r'IMPORT')
        # Call
        self.lexer.add('CALL',r'Call')
        # Inclination
        self.lexer.add('INCLI',r'Inclination')
        # Increase
        self.lexer.add('INC',r'Inc')
        # Decrease
        self.lexer.add('DEC',r'Dec')
        #Brightness
        self.lexer.add('BRIGHT',r'Brightness')
        #Vibration
        self.lexer.add('VIB',r'Vibration')
        #Move
        self.lexer.add('MOV',r'Move')
        # Comment
        self.lexer.add('COMMENT', r'//')
        #Times
        self.lexer.add('TIMES',r'Times')
        #For Cycle
        self.lexer.add('FOR',r'For')
        #End Cycle
        self.lexer.add('FEND',r'Fend')
        # Procedure
        self.lexer.add('PROCEDURE', r'Procedure')
        # Begin
        self.lexer.add('BEGIN', r'begin')
        # End
        self.lexer.add('END', r'end')
        # Main
        self.lexer.add('MAIN', r'Main')
        # Text
        self.lexer.add('TEXT', '[a-zA-Z0-9/]*')
        
        
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()