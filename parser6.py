#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:26:52 2019

@author: samuel
"""

from rply import ParserGenerator
from ast6 import Number, Inc, Dec


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'INC', 'DEC', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'COMMA']
        )
        self.token = ''

    def parse(self):
        @self.pg.production('x : ')
        @self.pg.production('x : x program')
        @self.pg.production('program : program  y ')
        def program(p):
            return
        
        @self.pg.production('y : INC OPEN_PAREN NUMBER COMMA NUMBER CLOSE_PAREN SEMI_COLON')
        def program3(p):
            left = Number(p[2].value)
            right = Number(p[4].value)
            return print((Inc(left, right)).eval())
        
        @self.pg.production('y : DEC OPEN_PAREN NUMBER COMMA NUMBER CLOSE_PAREN SEMI_COLON')
        def program4(p):
            left = Number(p[2].value)
            right = Number(p[4].value)
            return print((Dec(left, right)).eval())
        
        @self.pg.production('program : ')
        def program1(p):
            return 

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()