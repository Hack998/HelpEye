#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:26:52 2019

@author: samuel
"""

from rply import ParserGenerator
from ast8 import Number, Inc, Dec, Inclination, Call, Procedure, Variable, Brightness, Vibration, Move, For, FEnd, Dow, Case, When
from parser1 import Parserr
from lexer8 import Lexer


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['DECLARE', 'EQUAL', 'NUMBER', 'INC', 'DEC', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'COMMA', 'POINT', 'COMMENT', 'TEXT', 'INCLI', 
             'IMPORT', 'CALL', 'TIMES', 'CASE', 'WHEN', 'THEN','ELSE', 'END_CASE', 'MAIN', 
             'PROCEDURE', 'BEGIN', 'END', 'BRIGHT', 'VIB', 'MOV', 'FOR', 'DOW', 'ENDDO', 'FEND']
        )
        self.comment = ""
        self.case = ""
        self.procedures = []
        self.token = 0
        self.arguments = []
        self.declarations = []
        self.cycle = []
        self.whenDec = []
        self.dow = ''

    def parse(self):
        @self.pg.production('x : ')
        @self.pg.production('x : x program')
        @self.pg.production('program : program  y')
        def program(p):
            return
        
        @self.pg.production('program : ')
        def programE(p):
            return 
        
        # Declare
        @self.pg.production('y : DECLARE TEXT EQUAL NUMBER SEMI_COLON')
        def declare(p):
            self.declarations.append(Variable(p[1].value, p[3].value))
            return
        
        @self.pg.production('y : DECLARE TEXT SEMI_COLON')
        def emptyDeclare(p):
            self.declarations.append(Variable(p[1].value))
            return
        
        @self.pg.production('y : TEXT EQUAL NUMBER SEMI_COLON')
        def reDeclare(p):
            dCopy = self.declarations
            for i in dCopy:
                if(i.name == p[0].value):    
                    self.declarations.remove(i)
                    self.declarations.append(Variable(p[0].value, p[2].value))
                    
                    for j in self.declarations:
                        print("Name = " + j.name + "\nValue = " + j.value)
                        
                    return True
                else:
                    return False
        
        # Case
        @self.pg.production('y : CASE')
        def case(p):
            if(self.token == 8):
                self.case.whenDec[len(self.case.whenDec) - 1].function.append(Case(self.token))
                self.token = -8
            else:
                if(self.token == 3 or self.token == 5):
                    self.case = Case(self.token)
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
                
            elif(self.case.cToken == 5):
                self.case.eval(self.declarations)
                self.token = 5
            
                
            print("END")
            return
        
        # Incremento
        @self.pg.production('y : INC OPEN_PAREN NUMBER COMMA NUMBER CLOSE_PAREN SEMI_COLON')
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
            elif self.token == 3:
                left = Number(p[2].value)
                right = Number(p[4].value)
                return (self.procedures[len(self.procedures) - 1]).array.append(Inc(left, right))
            elif self.token == 4:
                raise SystemExit("Inc() esta fuera de un procedimiento")
                return
            elif self.token == 5:
                left = Number(p[2].value)
                right = Number(p[4].value)
                return print((Inc(left, right)).eval())
            elif self.token == 6:
                left = Number(p[2].value)
                right = Number(p[4].value)
                self.cycle = []
                return (self.cycle[0]).array.append(Inc(left, right))
            elif self.token == 8:
                left = Number(p[2].value)
                right = Number(p[4].value)
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function.append(Inc(left, right))
            elif self.token == -8:
                left = Number(p[2].value)
                right = Number(p[4].value)
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                j = len(self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec) - 1
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function[i].whenDec[j].function.append(Inc(left, right))
            elif self.token == 9:
                left = Number(p[2].value)
                right = Number(p[4].value)
                return (self.dow.function.append(Inc(left, right)))
            elif self.token == -9:
                left = Number(p[2].value)
                right = Number(p[4].value)
                return (self.dow.function[len(self.dow.function)-1].function.append(Inc(left, right)))
                
        
        # Decremento
        @self.pg.production('y : DEC OPEN_PAREN NUMBER COMMA NUMBER CLOSE_PAREN SEMI_COLON')
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
            elif self.token == 3:
                left = Number(p[2].value)
                right = Number(p[4].value)
                return (self.procedures[len(self.procedures) - 1]).array.append(Dec(left, right))
            elif self.token == 4:
                raise SystemExit("Dec() esta fuera de un procedimiento")
                return
            elif self.token == 5:
                left = Number(p[2].value)
                right = Number(p[4].value)
                return 1 #print((Dec(left, right)).eval()
            elif self.token == 6:
                left = Number(p[2].value)
                right = Number(p[4].value)
                self.cycle = []
                return (self.cycle[0]).array.append(Dec(left, right))
            elif self.token == 8:
                left = Number(p[2].value)
                right = Number(p[4].value)
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function.append(Dec(left, right))
            elif self.token == -8:
                left = Number(p[2].value)
                right = Number(p[4].value)
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                j = len(self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec) - 1
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function[i].whenDec[j].function.append(Dec(left, right))
            elif self.token == 9:
                left = Number(p[2].value)
                right = Number(p[4].value)
                return (self.dow.function.append(Dec(left, right)))
            elif self.token == -9:
                left = Number(p[2].value)
                right = Number(p[4].value)
                return (self.dow.function[len(self.dow.function)-1].function.append(Dec(left, right)))
                
        
        # Comentario
        @self.pg.production('y : COMMENT z')
        def CommentP(p):
            print("Comment: " + self.comment[1:len(self.comment)])
            self.comment = ""
            if self.token == 0:
                self.token = 2
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
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                raise SystemExit("No se han declarado variables")
                return
            elif self.token == 2:
                raise SystemExit("Inclination() esta fuera de un procedimiento")
                return
            elif self.token == 3:
                return (self.procedures[len(self.procedures) - 1]).array.append(Inclination(p[2].value))
            elif self.token == 4:
                raise SystemExit("Inclination() esta fuera de un procedimiento")
                return
            elif self.token == 5:
                return (Inclination(p[2].value)).eval()
            elif self.token == 6:
                self.cycle = []
                return (self.cycle[0]).array.append(Inclination(p[2].value))
            elif self.token == 8:
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function.append(Inclination(p[2].value))
            elif self.token == 8:
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                j = len(self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec) - 1
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function[i].whenDec[j].function.append(Inclination(p[2].value))
            elif self.token == 9:
                left = Number(p[2].value)
                right = Number(p[4].value)
                return (self.dow.function.append(Inclination(left, right)))
            elif self.token == -9:
                left = Number(p[2].value)
                right = Number(p[4].value)
                return (self.dow.function[len(self.dow.function)-1].function.append(Inclination(left, right)))
                
   
        #Iluminacion
        @self.pg.production('y : BRIGHT OPEN_PAREN NUMBER CLOSE_PAREN SEMI_COLON')
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
            elif self.token == 3:
                return (self.procedures[len(self.procedures) - 1]).array.append(Brightness(p[2].value))
            elif self.token == 4:
                raise SystemExit("Brightness() esta fuera de un procedimiento")
                return
            elif self.token == 5:
                return (Brightness(p[2].value)).eval()
            elif self.token == 6:
                self.cycle = []
                return (self.cycle[0]).array.append(Brightness(p[2].value))

        #Vibracion
        @self.pg.production('y : VIB OPEN_PAREN NUMBER CLOSE_PAREN SEMI_COLON')
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
            elif self.token == 3:
                return (self.procedures[len(self.procedures) - 1]).array.append(Vibration(p[2].value))
            elif self.token == 4:
                raise SystemExit("Vibration() esta fuera de un procedimiento")
                return
            elif self.token == 5:
                return (Vibration(p[2].value)).eval()
            elif self.token == 6:
                self.cycle = []
                return (self.cycle[0]).array.append(Vibration(p[2].value))

        #Movimientos
        @self.pg.production('y : MOV OPEN_PAREN NUMBER CLOSE_PAREN SEMI_COLON')
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
            elif self.token == 3:
                return (self.procedures[len(self.procedures) - 1]).array.append(Move(p[2].value))
            elif self.token == 4:
                raise SystemExit("Move() esta fuera de un procedimiento")
                return
            elif self.token == 5:
                return (Move(p[2].value)).eval()
            elif self.token == 6:
                self.cycle = []
                return (self.cycle[0]).array.append(Move(p[2].value))
        
        # Import
        @self.pg.production('y : IMPORT TEXT POINT TEXT')
        def ImportP(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 2:
                data = open(p[1].value + p[2].value + p[3].value,'r')
                text_input = data.read()
                
                lexer = Lexer().get_lexer()
                tokens = lexer.lex(text_input)
                
                pg = Parserr()
                pg.parse()
                parser = pg.get_parser()
                g = parser.parse(tokens)
                
                for k in g[1]:
                    self.procedures.append(k)
                return
            elif self.token == 4:
                raise SystemExit("IMPORT esta dentro de un procedimiento")
                return
        
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
            elif self.token == 3:
                return (self.procedures[len(self.procedures) - 1]).array.append(Call(p[1].value))
            elif self.token == 4:
                raise SystemExit("Call esta fuera de un procedimiento")
                return
            elif self.token == 5:
                return (Call(p[1].value)).eval(self.procedures, self.declarations)
            elif self.token == 6:
                self.cycle = []
                return (self.cycle[0]).array.append(Call(p[1].value))
            elif self.token == 8:
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function.append(Call(p[1].value))
            elif self.token == -8:
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                j = len(self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec) - 1
                return (self.case.whenDec[len(self.case.whenDec) - 1]).function[i].whenDec[j].function.append(Call(p[1].value))
            elif self.token == 9:
                left = Number(p[2].value)
                right = Number(p[4].value)
                return (self.dow.function.append(Call(left, right)))
            elif self.token == -9:
                left = Number(p[2].value)
                right = Number(p[4].value)
                return (self.dow.function[len(self.dow.function)-1].function.append(Call(left, right)))
                
            
        
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
            elif self.token == 3:
                (self.procedures[len(self.procedures) - 1]).array.append(Call(p[1].value, self.arguments))
                self.arguments = []
                return
            elif self.token == 4:
                raise SystemExit("Call() esta fuera de un procedimiento")
                return
            elif self.token == 5:
                (Call(p[1].value, self.arguments)).eval(self.procedures, self.declarations)
                self.arguments = []
                return
            elif self.token == 6:
                self.cycle = []
                (self.cycle[0]).array.append(Call(p[1].value, self.arguments))
                return
            elif self.token == 8:
                (self.case.whenDec[len(self.procedures) - 1]).function.append(Call(p[1].value, self.arguments))
                self.arguments = []
                return
            elif self.token == -8:
                i = len(self.case.whenDec[len(self.case.whenDec) - 1].function) - 1
                j = len(self.case.whenDec[len(self.case.whenDec) - 1].function[i].whenDec) - 1
                (self.case.whenDec[len(self.procedures) - 1]).function[i].whenDec[j].function.append(Call(p[1].value, self.arguments))
                self.arguments = []
                return
            elif self.token == 9:
                left = Number(p[2].value)
                right = Number(p[4].value)
                return (self.dow.function.append(Call(left, right)))
            elif self.token == -9:
                left = Number(p[2].value)
                right = Number(p[4].value)
                return (self.dow.function[len(self.dow.function)-1].function.append(Call(left, right)))
                
            
        #For
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
            elif self.token == 3:
                (self.procedures[len(self.procedures) - 1]).array.append(For(p[1].value))
                self.token = 6
                self.arguments = []
                return
            elif self.token == 4:
                raise SystemExit("Call() esta fuera de un procedimiento")
                return
            elif self.token == 5:
                self.token = 6
                (For(p[1].value)).eval(self.cycle)
                return
            elif self.token == 6:
                self.cycle = []
                (self.cycle[0]).array.append(For(p[1].value))
                return

        #FEnd
        @self.pg.production('y : FEND SEMI_COLON')
        def FEndP(p):
            if self.token == 6:
                self.token = 3
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
                self.token = 3;
                self.arguments = []
                return
            elif self.token == 3:
                raise SystemExit("No se puede crear un procedimiento dentro de otro")
                return
            elif self.token == 4:
                self.procedures.append(Procedure(p[1].value, self.arguments))
                self.token = 3;
                self.arguments = []
                return
            elif self.token == 5:
                raise SystemExit("No se puede crear un procedimiento dentro del Main")
                return
            elif self.token == 8:
                raise SystemExit("No se puede crear un procedimiento dentro de otro")
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
                self.token = 3;
                return
            elif self.token == 3:
                raise SystemExit("No se puede crear un procedimiento dentro de otro")
                return
            elif self.token == 4:
                self.procedures.append(Procedure(p[1].value))
                self.token = 3;
                return
            elif self.token == 5:
                raise SystemExit("No se puede crear un procedimiento dentro del Main")
                return
            elif self.token == 8:
                raise SystemExit("No se puede crear un procedimiento dentro de otro")
                return
            
        
        # Main
        @self.pg.production('y : PROCEDURE MAIN OPEN_PAREN CLOSE_PAREN BEGIN')
        def main(p):
            if self.token == 0:
                raise SystemExit("No se ha puesto un comentario al inicio")
                return
            elif self.token == 1:
                raise SystemExit("No se han declarado variables")
                return
            elif self.token == 2:
                self.token = 5
                return
            elif self.token == 3:
                raise SystemExit("No se puede crear un Main dentro de un procedimiento")
                return
            elif self.token == 4:
                self.token = 5
                return
            elif self.token == 5:
                raise SystemExit("Ya existe un Main")
                return
            elif self.token == 8:
                raise SystemExit("No se puede crear un Main dentro de un procedimiento")
                return
        
        # Procedure End
        @self.pg.production('y : END SEMI_COLON')
        def prodEP(p):
            if self.token == 3:
                self.token = 4;
                return (self.procedures[len(self.procedures) - 1]).eval()
            if self.token == 5:
                return
        ##Dow
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
            else:
                self.dow.eval(self.declarations)
                self.token = self.dow.token
        
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