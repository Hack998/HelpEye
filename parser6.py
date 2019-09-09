#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:26:52 2019

@author: samuel
"""

from rply import ParserGenerator
from ast6 import Number, Inc, Dec, Inclination, Call, Import, Procedure


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'INC', 'DEC', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'COMMA', 'COMMENT', 'TEXT', 'INCLI', 
             'IMPORT', 'CALL', 'PROCEDURE', 'BEGIN', 'END']
        )
        self.comment = ""
        self.procedures = []
        self.token = 0
        self.arguments = []

    def parse(self):
        @self.pg.production('x : ')
        @self.pg.production('x : x program')
        @self.pg.production('program : program  y')
        def program(p):
            return
        
        @self.pg.production('program : ')
        def programE(p):
            return 
        
        # Incremento
        @self.pg.production('y : INC OPEN_PAREN NUMBER COMMA NUMBER CLOSE_PAREN SEMI_COLON')
        def IncP(p):
            left = Number(p[2].value)
            right = Number(p[4].value)
            if self.token == 1:
                return (self.procedures[len(self.procedures) - 1]).array.append(Inc(left, right))
            return print((Inc(left, right)).eval())
        
        # Decremento
        @self.pg.production('y : DEC OPEN_PAREN NUMBER COMMA NUMBER CLOSE_PAREN SEMI_COLON')
        def DecP(p):
            left = Number(p[2].value)
            right = Number(p[4].value)
            if self.token == 1:
                return (self.procedures[len(self.procedures) - 1]).array.append(Dec(left, right))
            return print((Dec(left, right)).eval())
        
        # Comentario
        @self.pg.production('y : COMMENT z')
        def CommentP(p):
            print("Comment: " + self.comment[1:len(self.comment)])
            self.comment = ""
            return 
         
        @self.pg.production('z : z TEXT')
        def CommentPI(p):
            self.comment += " " + str(p[1].value)
            return
         
        @self.pg.production('z : ')
        def CommentPE(p):
             return 
        
        # Inclinacion
        @self.pg.production('y : INCLI OPEN_PAREN NUMBER CLOSE_PAREN SEMI_COLON')
        def InclinationP(p):
            if self.token == 1:
                return (self.procedures[len(self.procedures) - 1]).array.append(Inclination(p[2].value))
            return (Inclination(p[2].value)).eval()
        
        # Import
        @self.pg.production('y : IMPORT TEXT SEMI_COLON')
        def ImportP(p):
            return (Import(p[1].value)).eval()
        
        # Call
        @self.pg.production('y : CALL TEXT SEMI_COLON')
        def CallNP(p):
            if self.token == 1:
                return (self.procedures[len(self.procedures) - 1]).array.append(Call(p[1].value))
            return (Call(p[1].value)).eval(self.procedures)
            
        
        @self.pg.production('y : CALL TEXT OPEN_PAREN args CLOSE_PAREN SEMI_COLON')
        def CallEP(p):
            if self.token == 1:
                (self.procedures[len(self.procedures) - 1]).array.append(Call(p[1].value, self.arguments))
                self.arguments = []
                return
            (Call(p[1].value, self.arguments)).eval(self.procedures)
            self.arguments = []
            return 
        
        # Procedure Begin
        @self.pg.production('y : PROCEDURE TEXT OPEN_PAREN args CLOSE_PAREN BEGIN')
        def prodNP(p):
            self.procedures.append(Procedure(p[1].value, self.arguments))
            self.token = 1;
            self.arguments = []
            return
        
        @self.pg.production('y : PROCEDURE TEXT OPEN_PAREN CLOSE_PAREN BEGIN')
        def prodP(p):
            self.procedures.append(Procedure(p[1].value))
            self.token = 1;
            return
        
        # Procedure End
        @self.pg.production('y : END SEMI_COLON')
        def prodEP(p):
            self.token = 0;
            return (self.procedures[len(self.procedures) - 1]).eval()
        
        # Argumentos
        @self.pg.production('args : NUMBER COMMA args')
        def argsC(p):
            self.arguments.append(int(p[0].value))
            return
        
        @self.pg.production('args : NUMBER')
        def args(p):
            self.arguments.append(int(p[0].value))
            return
        
        # Error
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()