#// ----- Juan Pablo Gomez Sapuy ----- // 
#Programa de simulación de modelado de agentes

#Propagacion de una enfermedad

import random


# \U0001F603 SANO
# \U0001F927 ENFERMO
# \U0001F637 RECUPERACION
# \U0001F480 MUERTE
# \U0001F60E PERSONA SANA

# Solicitar al usuario las variables 
num = int(input("Por favor, ingrese el número de elementos que desea en el arreglo: "))

proMuerte = int(input("Ingrese la probabilidad de muerte: (Ej: %50 es 1) %"))

proEnfermarse = int(input("Ingrese la probabilidad de enfermarse: (Ej: %50 es 1) %"))

repetir = int(input("Ingrese las veces que se repetira el ciclo: "))

# Creamos el arreglo vacio 
lista = []

# Agregamos los valores al arreglo 
for k in range(num):
    lista.append("\U0001F603")

# Con el for haremos que se repita las veces que el usuario necesite 
for i in range(0,repetir):

    #las valiables random = igual a la probabilidad 
    ran = random.randint(0,2)                               #probabilidad de caer en sano, enfermo o recuperacion                
    rlist = random.randint(0,num - 1)                       #indice del agente, le restamos uno para que no se salga del limite del arreglo 
    rmlist = random.randint(0,proMuerte)                    #probabilidad de muerte 
    plist = random.randint(0,proEnfermarse)                 #probabilidad de enfermarse 
    vlist = 0       
    vmlist = 0                         
    
    #si ran es igual a 0 y lista es igual sano entonces
    if (ran == 0) and (lista[rlist] == "\U0001F603"):  
        #lista sub indice rlist sea igual a enfermo               
        lista[rlist] = "\U0001F927" 
        #aqui hacemos que no se salga de los limites del arreglo 
        if (plist == 0):  
            if(rlist == 0):
                vlist = rlist + 1
                if(lista[vlist] == '\U0001F603'):
                    lista[vlist] = '\U0001F927'
            elif(rlist == 4):
                vmlist = vmlist - 1
                if(lista[vmlist] == '\U0001F603'): 
                    lista[vmlist] = '\U0001F927'
            elif(rlist > 0 and rlist < (num - 1)):
                vlist = rlist + 1
                vmlist = rlist - 1
                if(lista[vlist] == '\U0001F603' or lista[vmlist] == '\U0001F603'): 
                    lista[vlist] = '\U0001F927'
                    lista[vmlist] = '\U0001F927'     
    #si ran es igual a 1 y lista es igual enfermo entonces           
    elif (ran == 1) and (lista[rlist] == "\U0001F927"):            
        if (rmlist == 0):
            #lista sub indice rlist sea igual a muerte                                         
            lista[rlist] = "\U0001F480"                            
        else:
            #sino a recuperacion                                                 
            lista[rlist] = "\U0001F637"  
    #si ran es igual a 2 y lista es igual recuperacion entonces                                      
    elif (ran == 2) and (lista[rlist] == "\U0001F637"):
        #lista sub indice rlist sea igual a persona sana     
        lista[rlist] = "\U0001F60E"                               
    
    print(lista)                                                