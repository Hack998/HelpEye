#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:16:26 2019

@author: samuel
"""

from llvmlite import ir

# Number
class Number():
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        return int(self.value)
    
# Operations
class BinaryOp():
    def __init__(self, builder, module, printf, left, right, name):
        self.builder = builder
        self.module = module
        self.printf = printf
        self.left = left
        self.right = right
        self.name  = name
    
# Gen
class Gen():
    def __init__(self, builder, module, printf):
        self.builder = builder
        self.module = module
        self.printf = printf
        
    def evalpop(self,i,namex, fmt):
        # Declare argument list
        voidptr_ty = ir.IntType(8).as_pointer()
        
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
                            bytearray(fmt.encode("utf8")))
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name=namex)
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)

        # Call Print Function
        self.builder.call(self.printf, [fmt_arg, i])
        return
    
class Inc(BinaryOp):
    def evalc(self, declarations,local):
        if local != []:
            dCopy = local
            for k in dCopy:
                if(k.name == self.left): 
                    local.remove(k)
                    local.append(Variable(self.left, str(int(k.value) + self.right.eval())))
                    
                    r = ir.Constant(ir.IntType(8), int(k.value))
                    e = ir.Constant(ir.IntType(8), int(self.right.eval()))
                    i = self.builder.add(r,e)
                    
                    fmt = "%i \n\0"
                    self.name += "ta"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                    print(int(k.value) + self.right.eval())
                    return [declarations,local]
        dCopy = declarations
        for k in dCopy:
            if(k.name == self.left): 
                declarations.remove(k)
                declarations.append(Variable(self.left, str(int(k.value) + self.right.eval())))
                
                r = ir.Constant(ir.IntType(8), int(k.value))
                e = ir.Constant(ir.IntType(8), int(self.right.eval()))
                i = self.builder.add(r,e)
                
                fmt = "%i \n\0"
                self.name += "tp"
                Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                print(int(k.value) + self.right.eval())
                
                return [declarations,local]
    
class Dec(BinaryOp):
    def evalc(self, declarations, local):
        if local != []:
            dCopy = local
            for k in dCopy:
                if(k.name == self.left): 
                    local.remove(k)
                    local.append(Variable(self.left, str(int(k.value) + self.right.eval())))
                    
                    r = ir.Constant(ir.IntType(8), int(k.value))
                    e = ir.Constant(ir.IntType(8), int(self.right.eval()))
                    i = self.builder.sub(r,e)
                    
                    fmt = "%i \n\0"
                    self.name += "t"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                    print(int(k.value) - self.right.eval())
                    
                    return [declarations,local]
        for k in dCopy:
            if(k.name == self.left): 
                declarations.remove(k)
                declarations.append(Variable(self.left, str(int(k.value) - self.right.eval())))
               
                r = ir.Constant(ir.IntType(8), int(k.value))
                e = ir.Constant(ir.IntType(8), int(self.right.eval()))
                i = self.builder.sub(r,e)
                
                fmt = "%i \n\0"
                self.name += "t"
                Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                print(int(k.value) - self.right.eval())
                
                return [declarations,local]
    
#Declare Variable Class
class Variable():
    def __init__(self, name, value=None):
        self.name = name 
        self.value = value 
        
    def eval(self, declarations):
        dCopy = declarations
        for i in dCopy:
            if(i.name == self.name):    
                declarations.remove(i)
                declarations.append(Variable(self.name, self.value))
                return declarations
        raise SystemExit("No existe la variable")
        return
    
    def evalp(self, declarations, local):
        dCopy = local
        for i in dCopy:
            if(i.name == self.name):    
                local.remove(i)
                local.append(Variable(self.name, self.value))
                return [declarations,local]
        dCopy = declarations
        for i in dCopy:
            if(i.name == self.name):    
                declarations.remove(i)
                declarations.append(Variable(self.name, self.value))
                return [declarations,local]
        raise SystemExit("No existe la variable")
        return    
    
# Class CASE
class Case():
    def __init__(self, cToken):
        self.whenDec = []
        self.cToken = cToken          

    def evalf(self,procedures, declarations, local):
        wCopy = self.whenDec
        for i in wCopy:
            if(i.evalf(procedures, declarations, local)):
                print("Hey you!")
                return[declarations,local]

# Class WHEN Function
class When():
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.function = []

    def evalf(self,procedures, declarations, local):
        dCopy = declarations
        if(self.name == None and self.value == None):
            for x in self.function:
                try:
                    x.eval(procedures, declarations)
                except:
                    try:
                        x.evalp(declarations,[])
                        #declarations = j[0]
                    except:
                        try:
                            x.evalf(procedures, declarations, local)
                            #declarations = j[0]
                            #local = j[1]
                        except:
                            x.evalc(declarations, local)
                            #declarations = j[0]
                            #local = j[1]
            return True
        for i in dCopy:
            if((i.name == self.name) and (i.value == self.value)):
                for x in self.function:
                    try:
                        x.eval(procedures, declarations)
                    except:
                        try:
                            x.evalp(declarations,[])
                            #declarations = j[0]
                        except:
                            try:
                                x.evalf(procedures, declarations, local)
                                #declarations = j[0]
                                #local = j[1]
                            except:
                                x.evalc(declarations, local)
                                #declarations = j[0]
                                #local = j[1]
                return True
        return False

class Inclination():
    def __init__(self,builder,module,printf,value,name):
        self.builder =builder
        self.module = module
        self.printf = printf
        self.value = value
        self.name = name
        
    def evalc(self, declarations, local):
        if local != []:
            for y in local:
                if y.name == self.value:
                    if int(y.value) >= 15:
                        
                        i = ir.Constant(ir.IntType(8), int(y.value))
            
                        fmt = "Peligro \n\0"
                        self.name += "ts"
                        Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                        print("Peligro")
                        return[declarations,local]
                        
                    i = ir.Constant(ir.IntType(8), int(y.value))
            
                    fmt = "Safe \n\0"
                    self.name += "ts"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                    print("Safe")
                    return[declarations,local]
        for x in declarations:
            if x.name == self.value:
                if int(x.value) >= 15:
                    
                    i = ir.Constant(ir.IntType(8), int(x.value))
            
                    fmt = "Peligro \n\0"
                    self.name += "ts"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                    
                    print("Peligro")
                    return[declarations,local]
                
                i = ir.Constant(ir.IntType(8), int(x.value))
            
                fmt = "Safe \n\0"
                self.name += "tr"
                Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                
                print("Safe")
                return[declarations,local]

class Object():
    def __init__(self,builder,module,printf,value,name):
        self.builder =builder
        self.module = module
        self.printf = printf
        self.value = value
        self.name = name
        
    def evalc(self, declarations, local):
        if local != []:
            for y in local:
                if y.name == self.value:
                    if int(y.value) <= 15:
                        
                        i = ir.Constant(ir.IntType(8), int(y.value))
            
                        fmt = "Peligro \n\0"
                        self.name += "t"
                        Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                        print("Peligro")
                        return[declarations,local]
                        
                    i = ir.Constant(ir.IntType(8), int(y.value))
            
                    fmt = "Safe \n\0"
                    self.name += "t"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                    print("Safe")
                    return[declarations,local]
        for x in declarations:
            if x.name == self.value:
                if int(x.value) <= 15:
                    
                    i = ir.Constant(ir.IntType(8), int(x.value))
            
                    fmt = "Peligro \n\0"
                    self.name += "t"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                    
                    print("Peligro")
                    return[declarations,local]
                
                i = ir.Constant(ir.IntType(8), int(x.value))
            
                fmt = "Safe \n\0"
                self.name += "t"
                Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                
                print("Safe")
                return[declarations,local]
                
class Sounds():
    def __init__(self,builder,module,printf,value,name):
        self.builder =builder
        self.module = module
        self.printf = printf
        self.value = value
        self.name = name
        
    def evalc(self, declarations, local):
        if local != []:
            for y in local:
                if y.name == self.value:
                    if int(y.value) >= 100:
                        
                        i = ir.Constant(ir.IntType(8), int(y.value))
            
                        fmt = "Peligro \n\0"
                        self.name += "t"
                        Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                        print("Peligro")
                        return[declarations,local]
                        
                    i = ir.Constant(ir.IntType(8), int(y.value))
            
                    fmt = "Safe \n\0"
                    self.name += "t"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                    print("Safe")
                    return[declarations,local]
        for x in declarations:
            if x.name == self.value:
                if int(x.value) >= 100:
                    
                    i = ir.Constant(ir.IntType(8), int(x.value))
            
                    fmt = "Peligro \n\0"
                    self.name += "t"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                    
                    print("Peligro")
                    return[declarations,local]
                
                i = ir.Constant(ir.IntType(8), int(x.value))
            
                fmt = "Safe \n\0"
                self.name += "t"
                Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                
                print("Safe")
                return[declarations,local]

class Brightness():
    def __init__(self,builder,module,printf,value,name):
        self.builder =builder
        self.module = module
        self.printf = printf
        self.value = value
        self.name = name
        
    def evalc(self, declarations, local):
        if local != []:
            for y in local:
                if y.name == self.value:
                    if int(y.value) >= 150:
                        i = ir.Constant(ir.IntType(8), int(y.value))
            
                        fmt = "Very bright \n\0"
                        self.name += "t"
                        Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                        print("Very bright")
                        return[declarations,local]
                    elif int(y.value) <= 30:
                        i = ir.Constant(ir.IntType(8), int(y.value))
            
                        fmt = "Very dark \n\0"
                        self.name += "t"
                        Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                        print("Very dark")
                        return[declarations,local]
                    else:
                        i = ir.Constant(ir.IntType(8), int(y.value))
            
                        fmt = "Safe \n\0"
                        self.name += "t"
                        Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                        print("Safe")
                        return[declarations,local]
        for x in declarations:
            if x.name == self.value:
                if int(x.value) >= 150:
                    i = ir.Constant(ir.IntType(8), int(x.value))
            
                    fmt = "Very bright \n\0"
                    self.name += "t"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                    print("Very bright")
                    return[declarations,local]
                elif int(x.value) <= 30:
                    i = ir.Constant(ir.IntType(8), int(x.value))
            
                    fmt = "Very dark \n\0"
                    self.name += "t"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                    print("Very dark")
                    return[declarations,local]
                else:
                    i = ir.Constant(ir.IntType(8), int(x.value))
            
                    fmt = "Safe \n\0"
                    self.name += "t"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                    print("Safe")
                    return[declarations,local]

class Temperature():
    def __init__(self,builder,module,printf,value,name):
        self.builder =builder
        self.module = module
        self.printf = printf
        self.value = value
        self.name = name
        
    def evalc(self, declarations, local):
        if local != []:
            for y in local:
                if y.name == self.value:
                    if int(y.value) >= 37:
                        i = ir.Constant(ir.IntType(8), int(y.value))
            
                        fmt = "Hot \n\0"
                        self.name += "t"
                        Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                        print("Hot")
                        return[declarations,local]
                    elif int(y.value) <= 13:
                        i = ir.Constant(ir.IntType(8), int(y.value))
            
                        fmt = "Cool \n\0"
                        self.name += "t"
                        Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                        print("Cool")
                        return[declarations,local]
                    else:
                        i = ir.Constant(ir.IntType(8), int(y.value))
            
                        fmt = "Safe \n\0"
                        self.name += "t"
                        Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                        print("Safe")
                        return[declarations,local]
        for x in declarations:
            if x.name == self.value:
                if int(x.value) >= 37:
                    i = ir.Constant(ir.IntType(8), int(x.value))
            
                    fmt = "Hot \n\0"
                    self.name += "t"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                    print("Hot")
                    return[declarations,local]
                elif int(x.value) <= 13:
                    i = ir.Constant(ir.IntType(8), int(x.value))
            
                    fmt = "Cool \n\0"
                    self.name += "t"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                    print("Cool")
                    return[declarations,local]
                else:
                    i = ir.Constant(ir.IntType(8), int(x.value))
            
                    fmt = "Safe \n\0"
                    self.name += "t"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                    print("Safe")
                    return[declarations,local]


class Move():
    def __init__(self,builder,module,printf,value,name):
        self.builder =builder
        self.module = module
        self.printf = printf
        self.value = value
        self.name = name
        
    def eval(self, declarations, local):
        if local != []:
            for y in local:
                if y.name == self.value:
                    if int(y.value) <= 15:
                        
                        i = ir.Constant(ir.IntType(8), int(y.value))
            
                        fmt = "Peligro \n\0"
                        self.name += "t"
                        Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                        print("Peligro")
                        return[declarations,local]
                    i = ir.Constant(ir.IntType(8), int(y.value))
            
                    fmt = "Safe \n\0"
                    self.name += "t"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                    
                    print("Safe")
                    return[declarations,local]
        for x in declarations:
            if x.name == self.value:
                if int(x.value) <= 15:
                    i = ir.Constant(ir.IntType(8), int(x.value))
            
                    fmt = "Peligro \n\0"
                    self.name += "t"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                    print("Peligro")
                    return[declarations,local]
                i = ir.Constant(ir.IntType(8), int(x.value))
            
                fmt = "Safe \n\0"
                self.name += "t"
                Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                
                print("Safe")
                return[declarations,local]


class Vibration():
    def __init__(self,builder,module,printf,value,name):
        self.builder =builder
        self.module = module
        self.printf = printf
        self.value = value
        self.name = name
        
    def evalc(self, declarations, local):
        if local != []:
            for y in local:
                if y.name == self.value:
                    if int(y.value) >= 90:
                        i = ir.Constant(ir.IntType(8), int(y.value))
            
                        fmt = "Peligro \n\0"
                        self.name += "t"
                        Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                        
                        print("Peligro")
                        return[declarations,local]
                    i = ir.Constant(ir.IntType(8), int(y.value))
            
                    fmt = "Safe \n\0"
                    self.name += "t"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                    
                    print("Safe")
                    return[declarations,local]
        for x in declarations:
            if x.name == self.value:
                if int(x.value) >= 90:
                    i = ir.Constant(ir.IntType(8), int(x.value))
            
                    fmt = "Peligro \n\0"
                    self.name += "t"
                    Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                      
                    print("Peligro")
                    return[declarations,local]
                i = ir.Constant(ir.IntType(8), int(x.value))
            
                fmt = "Safe \n\0"
                self.name += "t"
                Gen(self.builder, self.module, self.printf).evalpop(i, self.name, fmt)
                
                print("Safe")
                return[declarations,local]

class Call():
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def eval(self, procedures, declarations):
        arr = procedures
        if self.value == None:
            i = -1
            for x in procedures:
                i += 1
                if x.name == self.name:
                    if arr[i].value == None:
                        arr1 = procedures[i]
                        for u in arr1.array:
                            try:
                                u.eval(procedures, declarations)
                            except:
                                try:
                                    j = u.evalp(declarations, arr1.declaration)
                                    declarations = j[0]
                                    arr1.declaration = j[1]
                                except:
                                    try:
                                        j = u.evalf(procedures, declarations, arr1.declaration)
                                        declarations = j[0]
                                        arr1.declaration = j[1]
                                    except:
                                        j = u.evalc(declarations, arr1.declaration)
                                        declarations = j[0]
                                        arr1.declaration = j[1]
                        return[declarations, procedures]
            print("El procedimiento llamado no existe")
        self.value.reverse()
        i = -1
        for x in procedures:
            i += 1
            if x.name == self.name:
                if len(self.value) == arr[i].len:
                    arr1 = procedures[i]
                    for u in arr1.array:
                        try:
                            u.eval(procedures, declarations)
                        except:
                            try:
                                j = u.evalp(declarations, arr1.declaration)
                                declarations = j[0]
                                arr1.declaration = j[1]
                            except:
                                try:
                                    arr1.evalc(self.value,declarations)
                                    j = u.evalf(procedures, declarations, arr1.declaration)
                                    declarations = j[0]
                                    arr1.declaration = j[1]
                                except:
                                    arr1.evalc(self.value,declarations)
                                    j = u.evalc(declarations, arr1.declaration)
                                    declarations = j[0]
                                    arr1.declaration = j[1]
                    return[declarations, procedures]
        print("El procedimiento llamado no existe")

class For():
    def __init__(self, value, token):
        self.value = int(value)
        self.token = token
        self.cycle = []
    
    def evalf(self, procedures, declarations, local):
        if local != []:
            while(self.value > 0):
                for x in self.cycle:
                    try:
                        x.eval(procedures, declarations)
                    except:
                        try:
                            j = x.evalp(declarations,local)
                            declarations = j[0]
                            local = j[1]
                        except:
                            try:
                                j = x.evalf(procedures, declarations, local)
                                declarations = j[0]
                                local = j[1]
                            except:
                                j = x.evalc(declarations, local)
                                declarations = j[0]
                                local = j[1]
                self.value -= 1
            else:
                print("Ciclo terminado")
                return[declarations, local]
        while(self.value > 0):
            for x in self.cycle:
                try:
                    x.eval(procedures, declarations)
                except:
                    try:
                        j = x.evalp(declarations,[])
                        declarations = j[0]
                    except:
                        try:
                            j = x.evalf(procedures, declarations, local)
                            declarations = j[0]
                            local = j[1]
                        except:
                            j = x.evalc(declarations, local)
                            declarations = j[0]
                            local = j[1]
            self.value -= 1
        else:
            print("Ciclo terminado")
            return[declarations, local]

class Procedure():
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.array = []
        self.declaration = []
        if value != None:
            self.value.reverse()
            self.len = len(self.value)
        else:
            self.len = None
        
    def evalc(self, args, declarations):
        i = -1
        for x in args:
            i +=1
            for u in declarations:
                if x == u.name:
                    self.declaration.append(Variable(self.value[i],u.value))


class TemporalVars():
    def __init__(self, miVar, valIni, increment, valFin, token):
        self.miVar = miVar
        self.valIni = int(valIni)
        self.increment = int(increment)
        self.valFin = int(valFin)
        self.token = token
        self.function = []
        self.repos = int(valIni)

class Dow(TemporalVars):
    def evalf(self,procedures, declarations, local):
        while True:
            if (self.valIni)>=(self.valFin):
                self.valIni = self.repos
                return[declarations, local]
            for i in declarations:
                if i.name==self.miVar:
                    i.value = (self.valIni)
                    for x in self.function:
                        try:
                            x.eval(procedures, declarations)
                        except:
                            try:
                                x.evalp(declarations,[])
                                #declarations = j[0]
                            except:
                                try:
                                    x.evalf(procedures, declarations, local)
                                    #declarations = j[0]
                                    #local = j[1]
                                except:
                                    x.evalc(declarations, local)
                                    #declarations = j[0]
                                    #local = j[1]
            self.valIni+=self.increment