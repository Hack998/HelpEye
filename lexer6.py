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
        # Semi Colon
        self.lexer.add('SEMI_COLON',r'\;')
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
        # Comment
        self.lexer.add('COMMENT', r'//')
        # Procedure
        self.lexer.add('PROCEDURE', r'Procedure')
        # Begin
        self.lexer.add('BEGIN', r'begin')
        # End
        self.lexer.add('END', r'end')
        # Text
        self.lexer.add('TEXT', '[a-zA-Z0-9/]*')
        
        
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()