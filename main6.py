#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:02:45 2019

@author: samuel
"""

from lexer6 import Lexer
from parser6 import Parser

text_input = """
Inc(5 , 2);
Dec(5 , 2);
Inc(7 , 4);
"""

# IMPORT ;
# call ( 6 );
# Inclination( 7 );
# Inc( 5 , 2 );
# Dec( 7 , 2 );


lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
    
pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens)