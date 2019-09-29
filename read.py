#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:04:30 2019

@author: samuel
"""

from verificacion import Verificacion
from main6 import Main
import subprocess
import os
import time

print ("Ingrese")
print ("0 : Servidor de prueba")
print ("1 : Servidor")
print ("2 : Pruebas de los Ciclos")
o = input()

if o.isdigit() == True:
    o = int(o)
    if o == 1:
        while (o == 1):
            # Lectura
            path = "/home/samuel/Escritorio/Compi/Prueba/gcc/object_recognition_detection/testfile.txt"
            client = open(path,'r')
            
            a = client.read()
            q = -1
            
            path = "/home/samuel/Escritorio/Compi/Prueba/gcc/gyu/datosarduino.txt"
            client = open(path,'r')
            
            f = client.read()
            objeto, move = "", ""
            for p in a:
                if p.isdigit():
                    if q == 0:
                        objeto += p
                    elif q == 1:
                        move += p
                else:
                    q += 1
            vibracion, inclinacion, temperatura, brightness, sounds = "","","","",""
            q = 0
            for p in f:
                if p.isdigit():
                    if q == 0:
                        vibracion += p
                    elif q == 1:
                        inclinacion += p
                    elif q == 2:
                        temperatura += p
                    elif q == 3:
                        brightness += p
                    elif q == 4:
                        sounds += p
                else:
                    q += 1
            
            # Escribir
            data = "// datos \nDECLARE x = " + objeto + ";\nDECLARE y = " + move + ";\nDECLARE z = " + vibracion + ";\nDECLARE c = " + inclinacion + ";\nDECLARE v = " + temperatura + ";\nDECLARE b = " + brightness + ";\nDECLARE n = " + sounds + ";"
            #data = "// datos \nDECLARE y = 1;\nProcedure suma () \nbegin \nInc(y,1); \nend;"
            path = '/home/samuel/Escritorio/Compi/Prueba/gcc/data.txt'
            file = open(path,'w')
            file.write(data)
            file.close()
            
            # Compilador
            print("")
            print("Compilador")
            print("")
            Main().eval('/home/samuel/Escritorio/Compi/Prueba/gcc/input.txt')
            
            # Output
            os.system("llc -filetype=obj output.ll")
            os.system("gcc output.o -o output")
            print("")
            print("Generador de codigo")
            print("")
            y = subprocess.getoutput("./output")
            print(y)
            
            # Enviar
            print("")
            y = y.replace("Safe" , "0")
            y = y.replace("Cool" , "1")
            y = y.replace("Peligro" , "1")
            y = y.replace("Very bright" , "1")
            y = y.replace("Very dark" , "1")
            y = y.replace("Hot" , "1")
            y = y.replace("\n" , "")
            y = y.replace(" " , "")
            print(y)
            
            path = '/home/samuel/Escritorio/Compi/Prueba/gcc/gyu/datostoarduino.txt'
            file = open(path,'w')
            file.write(y)
            file.close()
            
            print("")
            print("Informacion enviada")
            print("")
            time.sleep(5)
    elif o == 0:
        while(o == 0):
            # Obtener datos
            print ("¿A que distacia hay un objeto?")
            objeto = input()
            if Verificacion().eval(objeto) == False:
                break
            print ("¿A que distacia hay un objeto en movimiento?")
            move = input()
            if Verificacion().eval(move) == False:
                break
            print ("¿Cuanta vibracion hay?")
            vibracion = input()
            if Verificacion().eval(vibracion) == False:
                break
            print ("¿Cuanta inclinacion hay?")
            inclinacion = input()
            if Verificacion().eval(inclinacion) == False:
                break
            print ("¿Cual es la temperatura?")
            temperatura = input()
            if Verificacion().eval(temperatura) == False:
                break
            print ("¿Cuanta luminicidad hay?")
            brightness = input()
            if Verificacion().eval(brightness) == False:
                break
            print ("¿Cuanto sonido hay?")
            sounds = input()
            if Verificacion().eval(sounds) == False:
                break
            
            # Escribir
            data = "// datos \nDECLARE x = " + objeto + ";\nDECLARE y = " + move + ";\nDECLARE z = " + vibracion + ";\nDECLARE c = " + inclinacion + ";\nDECLARE v = " + temperatura + ";\nDECLARE b = " + brightness + ";\nDECLARE n = " + sounds + ";"
            path = '/home/samuel/Escritorio/Compi/Prueba/gcc/data.txt'
            file = open(path,'w')
            file.write(data)
            file.close()
            
            # Compilador
            print("")
            print("Compilador")
            print("")
            Main().eval('/home/samuel/Escritorio/Compi/Prueba/gcc/input.txt')
            
            # Output
            os.system("llc -filetype=obj output.ll")
            os.system("gcc output.o -o output")
            print("")
            print("Generador de codigo")
            print("")
            datosgen = subprocess.getoutput("./output")
            print(datosgen)
            
            # Enviar
            print("")
            datosgen = datosgen.replace("Safe" , "0")
            datosgen = datosgen.replace("Cool" , "1")
            datosgen = datosgen.replace("Peligro" , "1")
            datosgen = datosgen.replace("Very bright" , "1")
            datosgen = datosgen.replace("Very dark" , "1")
            datosgen = datosgen.replace("Hot" , "1")
            datosgen = datosgen.replace("\n" , "")
            datosgen = datosgen.replace(" " , "")
            print(datosgen)
            
            path = '/home/samuel/Escritorio/Compi/Prueba/gcc/gyu/datostoarduino.txt'
            file = open(path,'w')
            file.write(datosgen)
            file.close()
            print("")
            print("Informacion enviada")
            print("")
            
            print ("Ingrese")
            print ("0 : Otra prueba")
            print ("1 : Terminar")
            o = input()
            if o.isdigit() == True:
                o = int(o)
                if (o < 0) or (o > 1):
                    print("Ingrese 1 o 0")
                    break
            else:
                print("Ingrese numeros")
    elif o == 2:
        print ("Ingrese")
        print ("0 : For")
        print ("1 : Case")
        print ("2 : Dow")
        print ("3 : Ciclos anidados")
        o = input()
        if o.isdigit() == True:
            o = int(o)
            if (o < 0) or (o > 3):
                raise SystemExit("Ingrese 0 o 1 o 2 o3")
        else:
            raise SystemExit("Ingrese numeros")
        if (o != 1 and o != 3):
            if o == 0:
                print ("Ingrese, cuantos ciclos?")
            else:
                print ("Ingrese, Valor final, sabiendo que se va a iniciar en 1 y se aumenta en 2")
            y = input()
            if y.isdigit() == True:
                y = int(y)
                if y < 1:
                    raise SystemExit("Ingrese numeros mayores que 1")
            else:
                raise SystemExit("Ingrese numeros")
        if o == 0:
            data = ("// import for \nDECLARE y = 1;\nProcedure for ()\nbegin\nFor "+ str(y) +" Times\nInclination(y);\nInc(y,10);\nFend;\nend;")
            path = '/home/samuel/Escritorio/Compi/Prueba/gcc/importfor.txt'
            eval_path = '/home/samuel/Escritorio/Compi/Prueba/gcc/inputfor.txt'
            print("For")
        elif o == 1:
            data = ("// import case \nDECLARE y = 1;\nProcedure case ()\nbegin\nCASE\nWHEN y = 1\nTHEN\nInc(y,15);\nELSE\nInclination(y);\nEND CASE;\nend;")
            path = '/home/samuel/Escritorio/Compi/Prueba/gcc/importcase.txt'
            eval_path = '/home/samuel/Escritorio/Compi/Prueba/gcc/inputcase.txt'
            print("Case")
        elif o == 2:
            data = ("// import dow \nDECLARE y;\nProcedure dow ()\nbegin\nDow(y,1,2," + str(y) + ")\nTemperature(y);\nEnddo;\nend;")
            #data = ("// import dow \nDECLARE y = 1;\nProcedure dow ()\nbegin\nInclination(y);\nend;")
            path = '/home/samuel/Escritorio/Compi/Prueba/gcc/importdow.txt'
            eval_path = '/home/samuel/Escritorio/Compi/Prueba/gcc/inputdow.txt'
            print("Dow")
        else:
            eval_path = '/home/samuel/Escritorio/Compi/Prueba/gcc/inputg.txt'
            print("Ciclos anidados")
        
        if o != 3:
            file = open(path,'w')
            file.write(data)
            file.close()
        
        print("")
        print("Compilador")
        print("")
        Main().eval(eval_path)
        os.system("llc -filetype=obj output.ll")
        os.system("gcc output.o -o output")
        print("")
        print("Generador de codigo")
        print("")
        print(subprocess.getoutput("./output"))
        print("")
        
    else:
        print("Ingrese 0 o 1 o 2 o 3")
else:
    print("Ingrese numeros")
print("Proceso Terminado")