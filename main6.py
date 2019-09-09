#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:02:45 2019

@author: samuel
"""

from lexer6 import Lexer
from parser6 import Parser

text_input = """
// Aumento
Inc (5,2);

// Disminucion
Dec (5,3);

// Pendiente no peligrosa
Inclination(8);

// Pendiente peligrosa
Inclination(30);

// Extracion
IMPORT /home/samuel/Escritorio;

// Funcion
Procedure var ( 8,9 ,6 )
begin

Inc (7,7);
Dec (8,8);
Call vart;

end;

// Funcion
Procedure vart ( )
begin

Inc (5,5);

end;

// Funcion
Procedure var ( )
begin

Inc (6,6);
Dec (5,5);
Call vart;

end;

// Llamada normal
Call var;

// Llamada con variable
Call var (8, 9 ,6);
"""

# IMPORT ;
# call ( 6 );
# Inclination( 7 );
# Inc( 5 , 2 );
# Dec( 7 , 2 );


lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

#for token in tokens:
#    print(token)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens)