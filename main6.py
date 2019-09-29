#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:02:45 2019

@author: samuel
"""

from lexer6 import Lexer
from parser6 import Parser
from gen6 import CodeGen

class Main():
    def eval(self, path):
        data = open(path,'r')
        
        text_input = data.read()

        lexer = Lexer().get_lexer()
        tokens = lexer.lex(text_input)

        codegen = CodeGen()

        module = codegen.module
        builder = codegen.builder
        printf = codegen.printf

        pg = Parser(module, builder, printf)
        pg.parse()
        parser = pg.get_parser()
        parser.parse(tokens)

        codegen.create_ir()
        codegen.save_ir("/home/samuel/Escritorio/Compi/Prueba/gcc/output.ll")
        return