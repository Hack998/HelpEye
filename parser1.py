#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:43:38 2019

@author: samuel
"""

from rply import ParserGenerator
from ast6 import Number, Inc, Dec, Inclination, Call, Procedure, Variable, Dow, Brightness, Vibration, Move, For, Temperature, Object, Sounds, Case, When

class Parserr():
    def __init__(self, module, builder, printf , name):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['DECLARE', 'EQUAL', 'NUMBER', 'INC', 'DEC', 'OPEN_PAREN',
             'CLOSE_PAREN', 'SEMI_COLON', 'COMMA', 'COMMENT', 'TEXT', 'INCLI',
             'CALL', 'PROCEDURE', 'BEGIN', 'END', 'BRIGHT', 'VIB', 'MOV',
             'FOR', 'FEND', 'TIMES', 'TEMP', 'OBJ', 'SOUND', 'CASE',
             'WHEN', 'THEN','ELSE', 'END_CASE','DOW', 'ENDDO']
        )
        self.module = module
        self.builder = builder
        self.printf = printf
        
        self.comment = ""
        self.case = ""
        self.dow = ""
        self.procedures = []
        self.token = 0
        self.arguments = []
        self.declarations = []
        self.fort = ""
        self.whenDec = []
        
        self.name = name

    def parse(self):
        @self.pg.production('x : ')
        @self.pg.production('x : x program')
        @self.pg.production('program : program  y')
        def program(p):
            return [self.declarations,self.procedures, self.name]
        
        @self.pg.production('program : ')
        def programE(p):
            return 
        
        # Declare
        @self.pg.production('y : DECLARE TEXT EQUAL NUMBER SEMI_COLON')
        def declare(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                if len(p[1].value) > 10:
                    raise SystemExit("Supera las 10 posiciones")
                    return
                if (p[1].value).islower() == True:
                    dCopy = self.declarations
                    for i in dCopy:
                        if(i.name == p[1].value): 
                            raise SystemExit("Ya existe una variable con ese nombre")
                            return
                    self.declarations.append(Variable(p[1].value, p[3].value))
                    self.token = 2
            elif self.token == 2:
                if len(p[1].value) > 10:
                    raise SystemExit("Supera las 10 posiciones")
                    return
                if (p[1].value).islower() == True:
                    dCopy = self.declarations
                    for i in dCopy:
                        if(i.name == p[1].value): 
                            raise SystemExit("Ya existe una variable con ese nombre")
                            return
                    self.declarations.append(Variable(p[1].value, p[3].value))
            elif self.token == -3:
                if len(p[1].value) > 10:
                    raise SystemExit("Supera las 10 posiciones")
                    return
                if (p[1].value).islower() == True:
                    dCopy = self.declarations
                    for i in dCopy:
                        if(i.name == p[1].value): 
                            raise SystemExit("Ya existe una variable con ese nombre")
                            return
                    (self.procedures[len(self.procedures) - 1]).declaration.append(Variable(p[1].value, p[3].value))
            elif self.token == 4:
                raise SystemExit("DECLARE esta fuera de un procedimiento")
                return
            elif self.token == 6:
                if self.fort.token == 3:
                    raise SystemExit("No se pueden hacer declaraciones en el For")
                    return
            
        @self.pg.production('y : DECLARE TEXT SEMI_COLON')
        def emptyDeclare(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                if len(p[1].value) > 10:
                    raise SystemExit("Supera las 10 posiciones")
                    return
                if (p[1].value).islower() == True:
                    dCopy = self.declarations
                    for i in dCopy:
                        if(i.name == p[1].value): 
                            raise SystemExit("Ya existe una variable con ese nombre")
                            return
                    self.declarations.append(Variable(p[1].value))
                    self.token = 2
            elif self.token == 2:
                if len(p[1].value) > 10:
                    raise SystemExit("Supera las 10 posiciones")
                    return
                if (p[1].value).islower() == True:
                    dCopy = self.declarations
                    for i in dCopy:
                        if(i.name == p[1].value): 
                            raise SystemExit("Ya existe una variable con ese nombre")
                            return
                    self.declarations.append(Variable(p[1].value))
            
            elif self.token == -3:
                if len(p[1].value) > 10:
                    raise SystemExit("Supera las 10 posiciones")
                    return
                if (p[1].value).islower() == True:
                    dCopy = (self.procedures[len(self.procedures) - 1]).declaration
                    for i in dCopy:
                        if(i.name == p[1].value): 
                            raise SystemExit("Ya existe una variable con ese nombre")
                            return
                    (self.procedures[len(self.procedures) - 1]).declaration.append(Variable(p[1].value))
            elif self.token == 4:
                raise SystemExit("DECLARE esta fuera de un procedimiento")
                return
            elif self.token == 6:
                if self.fort.token == 3:
                    raise SystemExit("No se pueden hacer declaraciones en el For")
                    return

        @self.pg.production('y : TEXT EQUAL NUMBER SEMI_COLON')
        def reDeclare(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                raise SystemExit("No se han declarado variables")
                return
            elif self.token == 2:
                raise SystemExit("DECLARE esta fuera de un procedimiento")
                return
            elif self.token == -3:
                (self.procedures[len(self.procedures) - 1]).array.append(Variable(p[0].value,p[2].value))
                self.token = 3
                return
            elif self.token == 3:
                (self.procedures[len(self.procedures) - 1]).array.append(Variable(p[0].value,p[2].value))
                return
            elif self.token == 4:
                raise SystemExit("DECLARE esta fuera de un procedimiento")
                return
            elif self.token == 6:
                (self.fort.cycle).append(Variable(p[0].value,p[2].value))
                return
            elif self.token == -6:
                (self.fort.cycle[len(self.fort.cycle) -1]).cycle.append(Variable(p[0].value,p[2].value))
                return
        
        # Case
        @self.pg.production('y : CASE')
        def case(p):
            if(self.token == 8):
                self.case.whenDec[len(self.case.whenDec) - 1].function.append(Case(self.token))
                self.token = -8
            else:
                if(self.token == 3 or self.token == -3):
                    self.case = Case(3)
                    self.token = 7
            return

        @self.pg.production('y : WHEN TEXT EQUAL NUMBER THEN')
        def caseWhen(p):
            if(self.token == -8):
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec.append(When(p[1].value, p[3].value))
            else:   
                self.case.whenDec.append(When(p[1].value, p[3].value))
                self.token = 8
            return

        @self.pg.production('y : ELSE')
        def caseElse(p): 
            if(self.token == -8):
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec.append(When(None, None))
            else:
                self.case.whenDec.append(When(None, None))
                self.token = 8
            return

        @self.pg.production('y : END_CASE SEMI_COLON')
        def caseEnd(p):
            if(self.case.cToken == 3):                
                self.procedures[len(self.procedures) - 1].array.append(self.case)
                self.token = 3

            elif(self.token == -8):
                self.token = 8

            print("END")
            return
        
        # Incremento
        @self.pg.production('y : INC OPEN_PAREN TEXT COMMA NUMBER CLOSE_PAREN SEMI_COLON')
        def IncP(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                raise SystemExit("No se han declarado variables")
                return
            elif self.token == 2:
                raise SystemExit("Inc() esta fuera de un procedimiento")
                return
            elif self.token == -3:
                left = p[2].value
                right = Number(p[4].value)
                self.token = 3
                self.name = self.name + "r"
                return (self.procedures[len(self.procedures) - 1]).array.append(Inc(self.builder, self.module,self.printf,left, right, self.name))
            elif self.token == 3:
                left = p[2].value
                right = Number(p[4].value)
                self.name = self.name + "r" 
                return (self.procedures[len(self.procedures) - 1]).array.append(Inc(self.builder, self.module,self.printf,left, right, self.name))
            elif self.token == 4:
                raise SystemExit("Inc() esta fuera de un procedimiento")
                return
            elif self.token == 6:
                left = p[2].value
                right = Number(p[4].value)
                self.name = self.name + "r" 
                return (self.fort.cycle).append(Inc(self.builder, self.module,self.printf,left, right, self.name))
            elif self.token == -6:
                left = p[2].value
                right = Number(p[4].value)
                self.name = self.name + "r" 
                return (self.fort.cycle[len(self.fort.cycle) -1]).cycle.append(Inc(self.builder, self.module,self.printf,left, right, self.name))
            elif self.token == 8:
                left = p[2].value
                right = Number(p[4].value)
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function.append(Inc(self.builder, self.module,self.printf,left, right, self.name))
            elif self.token == -8:
                left = p[2].value
                right = Number(p[4].value)
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                j = len(self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec) - 1
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function[i].whenDec[j].function.append(Inc(self.builder, self.module,self.printf,left, right, self.name))
            elif self.token == 9:
                left = p[2].value
                right = Number(p[4].value)
                self.name = self.name + "r"
                return (self.dow.function.append(Inc(self.builder, self.module,self.printf,left, right, self.name)))
            elif self.token == -9:
                left = p[2].value
                right = Number(p[4].value)
                self.name = self.name + "r"
                return (self.dow.function[len(self.dow.function)-1].function.append(Inc(self.builder, self.module,self.printf,left, right, self.name)))
            
        # Decremento
        @self.pg.production('y : DEC OPEN_PAREN TEXT COMMA NUMBER CLOSE_PAREN SEMI_COLON')
        def DecP(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                raise SystemExit("No se han declarado variables")
                return
            elif self.token == 2:
                raise SystemExit("Dec() esta fuera de un procedimiento")
                return
            elif self.token == -3:
                left = p[2].value
                right = Number(p[4].value)
                self.token = 3
                self.name = self.name + "r" 
                return (self.procedures[len(self.procedures) - 1]).array.append(Dec(self.builder, self.module,self.printf,left, right, self.name))
            elif self.token == 3:
                left = p[2].value
                right = Number(p[4].value)
                self.name = self.name + "r" 
                return (self.procedures[len(self.procedures) - 1]).array.append(Dec(self.builder, self.module,self.printf,left, right, self.name))
            elif self.token == 4:
                raise SystemExit("Dec() esta fuera de un procedimiento")
                return
            elif self.token == 6:
                left = p[2].value
                right = Number(p[4].value)
                self.name = self.name + "r" 
                return (self.fort.cycle).append(Dec(self.builder, self.module,self.printf,left, right, self.name))
            elif self.token == -6:
                left = p[2].value
                right = Number(p[4].value)
                self.name = self.name + "r" 
                return (self.fort.cycle[len(self.fort.cycle) -1]).cycle.append(Dec(self.builder, self.module,self.printf,left, right, self.name))
            elif self.token == 8:
                left = p[2].value
                right = Number(p[4].value)
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function.append(Dec(self.builder, self.module,self.printf,left, right, self.name))
            elif self.token == -8:
                left = p[2].value
                right = Number(p[4].value)
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                j = len(self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec) - 1
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function[i].whenDec[j].function.append(Dec(self.builder, self.module,self.printf,left, right, self.name))
            elif self.token == 9:
                left = Number(p[2].value)
                right = Number(p[4].value)
                self.name = self.name + "r"
                return (self.dow.function.append(Dec(self.builder, self.module,self.printf,left, right, self.name)))
            elif self.token == -9:
                left = Number(p[2].value)
                right = Number(p[4].value)
                self.name = self.name + "r"
                return (self.dow.function[len(self.dow.function)-1].function.append(Dec(self.builder, self.module,self.printf,left, right, self.name)))
            
        # Comentario
        @self.pg.production('y : COMMENT z')
        def CommentP(p):
            print("Comment: " + self.comment[1:len(self.comment)])
            self.comment = ""
            if self.token == 0:
                self.token = 1
            return 
         
        @self.pg.production('z : z TEXT')
        def CommentPI(p):
            self.comment += " " + str(p[1].value)
            return
         
        @self.pg.production('z : ')
        def CommentPE(p):
             return 
        
        # Inclinacion
        @self.pg.production('y : INCLI OPEN_PAREN TEXT CLOSE_PAREN SEMI_COLON')
        def InclinationP(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                raise SystemExit("No se han declarado variables")
                return
            elif self.token == 2:
                raise SystemExit("Inclination() esta fuera de un procedimiento")
                return
            elif self.token == -3:
                self.token = 3
                self.name = self.name + "r" 
                return (self.procedures[len(self.procedures) - 1]).array.append(Inclination(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 3:
                self.name = self.name + "r" 
                return (self.procedures[len(self.procedures) - 1]).array.append(Inclination(self.builder,self.module,self.printf,p[2].value,self.name))
            elif self.token == 4:
                raise SystemExit("Inclination() esta fuera de un procedimiento")
                return
            elif self.token == 6:
                self.name = self.name + "r" 
                return (self.fort.cycle).append(Inclination(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == -6:
                self.name = self.name + "r" 
                return (self.fort.cycle[len(self.fort.cycle) -1]).cycle.append(Inclination(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 8:
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function.append(Inclination(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == -8:
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                j = len(self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec) - 1
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function[i].whenDec[j].function.append(Inclination(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 9:
                self.name = self.name + "r"
                return (self.dow.function.append(Inclination(self.builder, self.module,self.printf,p[2].value,self.name)))
            elif self.token == -9:
                self.name = self.name + "r"
                return (self.dow.function[len(self.dow.function)-1].function.append(Inclination(self.builder, self.module,self.printf,p[2].value,self.name)))
            
        # Object
        @self.pg.production('y : OBJ OPEN_PAREN TEXT CLOSE_PAREN SEMI_COLON')
        def ObjectP(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                raise SystemExit("No se han declarado variables")
                return
            elif self.token == 2:
                raise SystemExit("Object() esta fuera de un procedimiento")
                return
            elif self.token == -3:
                self.token = 3
                self.name = self.name + "r" 
                return (self.procedures[len(self.procedures) - 1]).array.append(Object(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 3:
                self.name = self.name + "r" 
                return (self.procedures[len(self.procedures) - 1]).array.append(Object(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 4:
                raise SystemExit("Object() esta fuera de un procedimiento")
                return
            elif self.token == 6:
                self.name = self.name + "r" 
                return (self.fort.cycle).append(Object(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == -6:
                self.name = self.name + "r" 
                return (self.fort.cycle[len(self.fort.cycle) -1]).cycle.append(Object(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 8:
                self.name = self.name + "r"
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function.append(Object(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == -8:
                self.name = self.name + "r"
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                j = len(self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec) - 1
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function[i].whenDec[j].function.append(Object(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 9:
                self.name = self.name + "r"
                return (self.dow.function.append(Object(self.builder, self.module,self.printf,p[2].value,self.name)))
            elif self.token == -9:
                self.name = self.name + "r"
                return (self.dow.function[len(self.dow.function)-1].function.append(Object(self.builder, self.module,self.printf,p[2].value,self.name)))
        
        # Sounds
        @self.pg.production('y : SOUND OPEN_PAREN TEXT CLOSE_PAREN SEMI_COLON')
        def SoundsP(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                raise SystemExit("No se han declarado variables")
                return
            elif self.token == 2:
                raise SystemExit("Sounds() esta fuera de un procedimiento")
                return
            elif self.token == -3:
                self.token = 3
                self.name = self.name + "r" 
                return (self.procedures[len(self.procedures) - 1]).array.append(Sounds(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 3:
                self.name = self.name + "r" 
                return (self.procedures[len(self.procedures) - 1]).array.append(Sounds(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 4:
                raise SystemExit("Sounds() esta fuera de un procedimiento")
                return
            elif self.token == 6:
                self.name = self.name + "r" 
                return (self.fort.cycle).append(Sounds(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == -6:
                self.name = self.name + "r" 
                return (self.fort.cycle[len(self.fort.cycle) -1]).cycle.append(Sounds(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 8:
                self.name = self.name + "r"
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function.append(Sounds(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == -8:
                self.name = self.name + "r"
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                j = len(self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec) - 1
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function[i].whenDec[j].function.append(Sounds(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 9:
                self.name = self.name + "r"
                return (self.dow.function.append(Sounds(self.builder, self.module,self.printf,p[2].value,self.name)))
            elif self.token == -9:
                self.name = self.name + "r"
                return (self.dow.function[len(self.dow.function)-1].function.append(Sounds(self.builder, self.module,self.printf,p[2].value,self.name)))
            
        
        #Iluminacion
        @self.pg.production('y : BRIGHT OPEN_PAREN TEXT CLOSE_PAREN SEMI_COLON')
        def BrightnessP(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                raise SystemExit("No se han declarado variables")
                return
            elif self.token == 2:
                raise SystemExit("Brightness() esta fuera de un procedimiento")
                return
            elif self.token == -3:
                self.token = 3
                self.name = self.name + "r" 
                return (self.procedures[len(self.procedures) - 1]).array.append(Brightness(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 3:
                self.name = self.name + "r" 
                return (self.procedures[len(self.procedures) - 1]).array.append(Brightness(self.builder,self.module,self.printf,p[2].value,self.name))
            elif self.token == 4:
                raise SystemExit("Brightness() esta fuera de un procedimiento")
                return
            elif self.token == 6:
                self.name = self.name + "r" 
                return (self.fort.cycle).append(Brightness(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == -6:
                self.name = self.name + "r" 
                return (self.fort.cycle[len(self.fort.cycle) -1]).cycle.append(Brightness(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 8:
                self.name = self.name + "r"
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function.append(Brightness(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == -8:
                self.name = self.name + "r"
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                j = len(self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec) - 1
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function[i].whenDec[j].function.append(Brightness(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 9:
                self.name = self.name + "r"
                return (self.dow.function.append(Brightness(self.builder, self.module,self.printf,p[2].value,self.name)))
            elif self.token == -9:
                self.name = self.name + "r"
                return (self.dow.function[len(self.dow.function)-1].function.append(Brightness(self.builder, self.module,self.printf,p[2].value,self.name)))
            
        # Temperature
        @self.pg.production('y : TEMP OPEN_PAREN TEXT CLOSE_PAREN SEMI_COLON')
        def TemperatureP(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                raise SystemExit("No se han declarado variables")
                return
            elif self.token == 2:
                raise SystemExit("Temperature() esta fuera de un procedimiento")
                return
            elif self.token == -3:
                self.token = 3
                self.name = self.name + "r" 
                return (self.procedures[len(self.procedures) - 1]).array.append(Temperature(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 3:
                self.name = self.name + "r" 
                return (self.procedures[len(self.procedures) - 1]).array.append(Temperature(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 4:
                raise SystemExit("Temperature() esta fuera de un procedimiento")
                return
            elif self.token == 6:
                self.name = self.name + "r" 
                return (self.fort.cycle).append(Temperature(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == -6:
                self.name = self.name + "r" 
                return (self.fort.cycle[len(self.fort.cycle) -1]).cycle.append(Temperature(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 8:
                self.name = self.name + "r"
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function.append(Temperature(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == -8:
                self.name = self.name + "r"
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                j = len(self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec) - 1
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function[i].whenDec[j].function.append(Temperature(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 9:
                self.name = self.name + "r"
                return (self.dow.function.append(Temperature(self.builder, self.module,self.printf,p[2].value,self.name)))
            elif self.token == -9:
                self.name = self.name + "r"
                return (self.dow.function[len(self.dow.function)-1].function.append(Temperature(self.builder, self.module,self.printf,p[2].value,self.name)))
            
        #Vibracion
        @self.pg.production('y : VIB OPEN_PAREN TEXT CLOSE_PAREN SEMI_COLON')
        def VibrationP(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                raise SystemExit("No se han declarado variables")
                return
            elif self.token == 2:
                raise SystemExit("Vibration() esta fuera de un procedimiento")
                return
            elif self.token == -3:
                self.token = 3
                self.name = self.name + "r" 
                return (self.procedures[len(self.procedures) - 1]).array.append(Vibration(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 3:
                self.name = self.name + "r" 
                return (self.procedures[len(self.procedures) - 1]).array.append(Vibration(self.builder,self.module,self.printf,p[2].value,self.name))
            elif self.token == 4:
                raise SystemExit("Vibration() esta fuera de un procedimiento")
                return
            elif self.token == 6:
                self.name = self.name + "r" 
                return (self.fort.cycle).append(Vibration(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == -6:
                self.name = self.name + "r" 
                return (self.fort.cycle[len(self.fort.cycle) -1]).cycle.append(Vibration(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 8:
                self.name = self.name + "r"
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function.append(Vibration(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == -8:
                self.name = self.name + "r"
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                j = len(self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec) - 1
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function[i].whenDec[j].function.append(Vibration(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 9:
                self.name = self.name + "r"
                return (self.dow.function.append(Vibration(self.builder, self.module,self.printf,p[2].value,self.name)))
            elif self.token == -9:
                self.name = self.name + "r"
                return (self.dow.function[len(self.dow.function)-1].function.append(Vibration(self.builder, self.module,self.printf,p[2].value,self.name)))
            
        #Movimientos
        @self.pg.production('y : MOV OPEN_PAREN TEXT CLOSE_PAREN SEMI_COLON')
        def MoveP(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                raise SystemExit("No se han declarado variables")
                return
            elif self.token == 2:
                raise SystemExit("Move() esta fuera de un procedimiento")
                return
            elif self.token == -3:
                self.token = 3
                self.name = self.name + "r" 
                return (self.procedures[len(self.procedures) - 1]).array.append(Move(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 3:
                self.name = self.name + "r" 
                return (self.procedures[len(self.procedures) - 1]).array.append(Move(self.builder,self.module,self.printf,p[2].value,self.name))
            elif self.token == 4:
                raise SystemExit("Move() esta fuera de un procedimiento")
                return
            elif self.token == 6:
                self.name = self.name + "r" 
                return (self.fort.cycle).append(Move(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == -6:
                self.name = self.name + "r" 
                return (self.fort.cycle[len(self.fort.cycle) -1]).cycle.append(Move(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 8:
                self.name = self.name + "r"
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function.append(Move(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == -8:
                self.name = self.name + "r"
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                j = len(self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec) - 1
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function[i].whenDec[j].function.append(Move(self.builder, self.module,self.printf,p[2].value,self.name))
            elif self.token == 9:
                self.name = self.name + "r"
                return (self.dow.function.append(Move(self.builder, self.module,self.printf,p[2].value,self.name)))
            elif self.token == -9:
                self.name = self.name + "r"
                return (self.dow.function[len(self.dow.function)-1].function.append(Move(self.builder, self.module,self.printf,p[2].value,self.name)))
            
        # Call
        @self.pg.production('y : CALL TEXT SEMI_COLON')
        def CallNP(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                raise SystemExit("No se han declarado variables")
                return
            elif self.token == 2:
                raise SystemExit("Call esta fuera de un procedimiento")
                return
            elif self.token == -3:
                self.token = 3
                return (self.procedures[len(self.procedures) - 1]).array.append(Call(p[1].value))
            elif self.token == 3:
                return (self.procedures[len(self.procedures) - 1]).array.append(Call(p[1].value))
            elif self.token == 4:
                raise SystemExit("Call esta fuera de un procedimiento")
                return
            elif self.token == 6:
                return (self.fort.cycle).append(Call(p[1].value))
            elif self.token == -6:
                (self.fort.cycle[len(self.fort.cycle) -1]).cycle.append(Call(p[1].value))
                return
            elif self.token == 8:
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function.append(Call(p[1].value))
            elif self.token == -8:
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                j = len(self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec) - 1
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function[i].whenDec[j].function.append(Call(p[1].value))
            elif self.token == 9:
                return (self.dow.function.append(Call(p[1].value)))
            elif self.token == -9:
                return (self.dow.function[len(self.dow.function)-1].function.append(Call(p[1].value)))
            
        @self.pg.production('y : CALL TEXT OPEN_PAREN args CLOSE_PAREN SEMI_COLON')
        def CallEP(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                raise SystemExit("No se han declarado variables")
                return
            elif self.token == 2:
                raise SystemExit("Call() esta fuera de un procedimiento")
                return
            elif self.token == -3:
                self.token = 3
                (self.procedures[len(self.procedures) - 1]).array.append(Call(p[1].value, self.arguments))
                self.arguments = []
                return
            elif self.token == 3:
                (self.procedures[len(self.procedures) - 1]).array.append(Call(p[1].value, self.arguments))
                self.arguments = []
                return
            elif self.token == 4:
                raise SystemExit("Call() esta fuera de un procedimiento")
                return
            elif self.token == 6:
                (self.fort.cycle).append(Call(p[1].value, self.arguments))
                self.arguments = []
                return
            elif self.token == -6:
                (self.fort.cycle[len(self.fort.cycle) -1]).cycle.append(Call(p[1].value, self.arguments))
                self.arguments = []
                return
            elif self.token == 8:
                (self.case.whenDec[len(self.case.whenDec) - 1]).function.append(Call(p[1].value, self.argument))
                self.arguments = []
                return
            elif self.token == -8:
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                j = len(self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec) - 1
                (self.case.whenDec[len(self.case.whenDec) - 1]).function[i].whenDec[j].function.append(Call(p[1].value, self.argument))
                self.arguments = []
                return 
            elif self.token == 9:
                return (self.dow.function.append(Call(p[1].value, self.argument)))
            elif self.token == -9:
                return (self.dow.function[len(self.dow.function)-1].function.append(Call(p[1].value, self.argument)))
            
        # For
        @self.pg.production('y : FOR NUMBER TIMES')
        def ForP(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                raise SystemExit("No se han declarado variables")
                return
            elif self.token == 2:
                raise SystemExit("For() esta fuera de un procedimiento")
                return
            elif self.token == -3:
                self.fort = For(p[1].value,3)
                (self.procedures[len(self.procedures) - 1]).array.append(self.fort)
                self.token = 6
                return
            elif self.token == 3:
                self.fort = For(p[1].value,self.token)
                (self.procedures[len(self.procedures) - 1]).array.append(self.fort)
                self.token = 6
                return
            elif self.token == 4:
                raise SystemExit("For() esta fuera de un procedimiento")
                return
            # revisar
            elif self.token == 6:
                (self.fort.cycle).append(For(p[1].value,self.token))
                self.token == -6
                return
            
        #FEnd
        @self.pg.production('y : FEND SEMI_COLON')
        def FEndP(p):
            if self.token == -6:
                self.token = (self.fort.cycle[len(self.fort.cycle) -1]).token
            elif self.token == 6:
                if self.fort.token == 3:
                    self.token = self.fort.token
            return
        
        # Procedure Begin
        @self.pg.production('y : PROCEDURE TEXT OPEN_PAREN args CLOSE_PAREN BEGIN')
        def prodNP(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                raise SystemExit("No se han declarado variables")
                return
            elif self.token == 2:
                self.procedures.append(Procedure(p[1].value, self.arguments))
                self.token = -3;
                self.arguments = []
                return
            elif self.token == 3:
                raise SystemExit("No se puede crear un procedimiento dentro de otro")
                return
            elif self.token == 4:
                self.procedures.append(Procedure(p[1].value, self.arguments))
                self.token = -3;
                self.arguments = []
                return
            elif self.token == 6:
                raise SystemExit("No se puede hacer un procedimiento dentro de un For")
                return
        
        @self.pg.production('y : PROCEDURE TEXT OPEN_PAREN CLOSE_PAREN BEGIN')
        def prodP(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                raise SystemExit("No se han declarado variables")
                return
            elif self.token == 2:
                self.procedures.append(Procedure(p[1].value))
                self.token = -3;
                return
            elif self.token == 3:
                raise SystemExit("No se puede crear un procedimiento dentro de otro")
                return
            elif self.token == 4:
                self.procedures.append(Procedure(p[1].value))
                self.token = -3;
                return
            elif self.token == 6:
                raise SystemExit("No se puede hacer un procedimiento dentro de un For")
                return
        
        # Procedure End
        @self.pg.production('y : END SEMI_COLON')
        def prodEP(p):
            if self.token == 3:
                self.token = 4;
                return (self.procedures[len(self.procedures) - 1])
            elif self.token == -3:
                self.token = 4;
                return (self.procedures[len(self.procedures) - 1])
            
        # Dow
        @self.pg.production('y : DOW OPEN_PAREN TEXT COMMA NUMBER COMMA NUMBER COMMA NUMBER CLOSE_PAREN')
        def dowN(p):
            miVar = p[2].value
            valIni = (p[4].value)
            increment = (p[6].value)
            valFin = (p[8].value)
            if self.token == 9:
                self.dow.function.append(Dow(miVar,valIni,increment,valFin,self.token))
                self.token = -9
            else:
                self.dow = Dow(miVar,valIni,increment,valFin,self.token)
                self.token=9
                return 

        @self.pg.production('y : ENDDO SEMI_COLON')
        def dowe(p):
            if self.token == -9:
                self.token = 9
            elif self.dow.token == -3:
                self.token = 3
                self.procedures[len(self.procedures) - 1].array.append(self.dow)
        
        # Argumentos
        @self.pg.production('args : TEXT COMMA args')
        def argsC(p):
            self.arguments.append(p[0].value)
            return
        
        @self.pg.production('args : TEXT')
        def args(p):
            self.arguments.append(p[0].value)
            return
        
        # Error
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
