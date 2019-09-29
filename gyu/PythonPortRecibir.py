# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 09:31:13 2019

@author: eduso
"""


import serial
#import time


def BuscarPuerto():
    """Busca el puerto en donde este el dispositivo conectado"""
    global arduinoData
    Puertos=['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2','/dev/ttyACM3','/dev/ttyS0','/dev/ttyUSB0']
    for Port in Puertos:
        
        try:
            arduinoData = serial.Serial(Port,baudrate=9600) 
            print("Conectado")
        except:
            "Puerto Invalido"                 
BuscarPuerto()

def enviarDatosToArduino(dato):

    try:
        arduinoData.write(dato.encode())
    except:
        BuscarPuerto()  
        enviarDatosToArduino(dato)
     
    # Cerrando puerto serial
    #arduinoPort.close()
        
while True: #
                  
    try:    #############################################################
        """Convierte el dato recibido del puerto
        en un numero entero, con 2 decimales """
        line = arduinoData.readline()
        #for i in line.decode('ascii'):                          #recorre el string recibido 
        print("        vi,inc,te,luz,son")
        print("Datos: ",line.decode('ascii'))
        
        #Crear Txt con las mediciones desde el arduino
        file = open("datosarduino.txt","w") 
        stringlist=str(line.decode('ascii'))
        file.write(stringlist.replace(' ', '')) 
        file.close()
        
        # archivo-entrada.py del peligro que se enviara a arduino
        f = open ('datostoarduino.txt','r')
        mensaje = f.read()
        print(mensaje)
        f.close()
        enviarDatosToArduino(mensaje)
                
    except:
        print ("Not Conn.")
        BuscarPuerto()              #intenta nuevamente buscar el puerto
