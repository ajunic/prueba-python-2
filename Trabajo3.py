"""
Autor:Armando Ugarte
Grupo:Weekend
"""
import math
import numpy as np

#Utileria para ordenar el trabajo mas bonito
print("TERCER TRABAJO")

def paso_ejercicio():
    """ Funcion para crear espacio en el programa"""
    print("Fin de ejercicio")
    print("\n")
    print("Siguiente ejercicio")    

#Programar las siguientes funciones:



def dinamica():
    """  funcion dinamica que consulte la cantidad de argumentos con la 
cual la misma funcionara y posterior a que el usuario ingrese la cantidad, tambien 
consulte los argumentos y sea capaz de determinar tanto el numero mas pequeño 
como el numero mas grande, considere que NO se podra utilizar las funciones 
min(), ni max() de python"""

    arg=int(input("Ingrese el numero de argumentos: "))
    args=[]

    for i in range(arg):
        numero_interno=int(input("Ingrese un numero: "))
        args.append(numero_interno)
       

    args.sort()
    print("Esta es la lista de argumentos")
    print(args)
    print(f"El argumento menor es: {args[0]}")
    print(f"El argumento mayor es: {args[-1]}")
    

dinamica()        
paso_ejercicio()

""". Programe una funcion que sea capaz a partir del valor del lado de un cuadrado (3 
metros), muestre el valor de su perimetro (en centimetros) y el de su area (en 
pulgadas cuadradas) -> Al convertir la escala el perimetro debe darle 12 metros y 
el area 9 metros cuadrados"""
lado_c= 3
def dimensiones(lado):
    perimetro=(lado*4*100)
    area=(lado**2*1550)
    return print(f"El perimetro es: {perimetro}cm y el area del cuadrado es:{area}pulg cuadradas")

dimensiones(lado_c)
paso_ejercicio()


#pedimos valores de entrada
def pedir_valores():
    """. Desarrolle un programa que a partir del valor de la base y de la altura de un 
triangulo (3 y 5 metros, respectivamente), muestre el valor de su area (en metros 
cuadrados). Recuerde que el area A de un triangulo se puede calcular a partir de 
la base b y la altura h como A = 1/2 bh -> Sin embargo el programa no debe de 
permitir pasar un valor cero o negativo como parametro"""

    base = int(input("Ingrese valor de base:"))
    altura=int(input("Ingrese valor de altura:"))
    
   
    while base and altura >=0:
        area= base*altura*0.5
        return print(f"El area del triangulo es:{area}")
    else:
        print("ingrese un valor mayor a 0 y no negativo")


pedir_valores()
paso_ejercicio()


def triangulo_2():
    """ 4.El area A de un triangulo se puede calcular a partir del valor de dos de sus lados, 
a y b, y del angulo θ que estos forman entre si con la formula A = 1/2 ab sin(θ). 
Desarrolle un programa que pida al usuario el valor de los dos lados (en metros), 
el angulo que estos forman (en grados), y muestre el valor del area -> Nuevamente 
el programa no debe de permitir pasar un valor cero o negativo como parametro
para ninguno de sus valores, tambien debe de mandar a imprimir por medio de un 
mensaje la explicación del porque la escala seleccionada (grados o radianes)."""
    base = int(input("Ingrese valor de base:"))
    altura=int(input("Ingrese valor de altura:"))
    angulo= int(input("Ingrese valor de angulo"))
    
   
    while base and altura and angulo >=0:
        area= base*altura*0.5*math.sin(angulo)
        return print(f"El area del triangulo es:{area}")
    else:
        print("ingrese un valor mayor a 0 y no negativo")

triangulo_2()
paso_ejercicio()


def convertandsort():
    """  programa que, dados diez numeros cualquiera, los vuelva enteros
y determine cual de los ultimos nueve numeros es mas cercano al primero. 
(Ejemplo, si el usuario introduce los numeros 2, 6, 4, 8, 12.5, 9.1, 1, 3, 1 y 10, la 
funcion respondera que el numero mas cercano al 2 es el 1 -> No se debe de 
permitir el ingreso de cero y si lo hacemos el programa no tiene porque reiniciar 
la entrada de todos los numeros."""
    numeros=[]
    
    for i in range(11):
        datos=int(input("Ingrese valores"))
        if datos>0 :
            numeros.append(datos)
        else:
            print("Debes ingresar un valor positivo y no 0")
            datos=int(input("Ingrese valor"))
          
    numeros.sort
    print(f"El numero mas cercano a {numeros[0]} es {numeros[1]}")
    

convertandsort()
paso_ejercicio()

"""
Desarrolle un programa que dado cinco puntos en el plano cartesiano, determine 
cual de los cuatro ultimos puntos es mas cercano al primero. Un punto se 
representara con dos variables: una para la abcisa y otra para la ordenada. La 
distancia entre dos puntos (x1, y1) y (x2, y2) es !(x1 − x2)! + (x1 − x2)!
"""
def distancia():
    while True:
        try:
            from math import sqrt
            #prueba1
            x1 = float(input('Escribe el eje de x1: '))
            y1 = float(input('Escribe el eje de y1: '))
            x2 = float(input('Escribe el eje de x2: '))
            y2 = float(input('Escribe el eje de y2: '))
            x3 = float(input('Escribe el eje de x3: '))
            y3 = float(input('Escribe el eje de y3: '))
            x4 = float(input('Escribe el eje de x4: '))
            y4 = float(input('Escribe el eje de y4: '))
            x5 = float(input('Escribe el eje de x5: '))
            y5 = float(input('Escribe el eje de y5: '))
    
            xy1 = sqrt((x1 - x2)**2+(y1 - y2)**2)
            xy2 = sqrt((x1 - x3)**2+(y1 - y3)**2)
            xy3 = sqrt((x1 - x4)**2+(y1 - y4)**2)
            xy4 = sqrt((x1 - x5)**2+(y1 - y5)**2)
    
            candidato = xy1
            if x1 == 0:
                break
            if candidato > xy2:
                candidato = xy2
            if candidato > xy3:
                candidato = xy3
            if candidato > xy4:
                candidato = xy4
    
            if candidato == xy1:
                masCerca = x2,y2
            if candidato == xy2:
                masCerca = x3,y3
            if candidato == xy3:
                masCerca = x4,y4
            if candidato == xy4:
                masCerca = x5,y5
            print ('El punto más cercano a x1 = {0} y y1 = {1} es: {2}'.format(x1,y1,masCerca))
        except ValueError:
            print ('No puedes dejar la entrada en blanco, ni escribir letras.')

paso_ejercicio()


def multiplos():
    """ Implemente un programa o funcion que muestre todos los multiplos de n entre n y 
    m*n, ambos inclusive, donde n y m son numeros introducidos por el usuario."""
    
    n = int(input("Ingrese valor de n:"))
    m = int(input("Ingrese valor de m:"))
    division= n/n
    producto= n*m

    for i in range(n,producto+1,n):
        print(i)

multiplos()
paso_ejercicio()

"""Desarrolle un programa que dada una cantidad dada por el cliente de un banco, 
solicite el desglose en billetes y monedas de una cantidad entera de euros. En la 
actualidad existen billetes de 500, 200, 100, 50, 20, 10 y 5 € y monedas de 2 y 1 
€, por lo cual se debe recorrer los valores de billete y monedas disponibles 
almacenados en la bobeda con uno o mas bucles for-in para lograr determinar 
cuantos billetes y monedas entregar, asi como saber cuanto queda aun disponible 
para atender a los demas clientes, esta sucursal al inicio del dia llama a la oficina 
central para informar con que cantidad quiere operar todos los dias. """

def desglose():
    
    deposito=int(input("Ingrese valor de deposito:"))
    billetes=[]
    monedas=[]
    i=0

    while deposito>0:
        if deposito>=500:
            deposito-=500
            billetes.append(500)
        elif deposito>=200:
            deposito-=200
            billetes.append(200)
        elif deposito>=100:
            deposito-=100
            billetes.append(100)
        elif deposito>=50:
            deposito-=50
            billetes.append(50)
        elif deposito>=20:
            deposito-=20
            billetes.append(20)
        elif deposito>=10:
            deposito-=10
            billetes.append(10)
        elif deposito>=5:
            deposito-=5
            billetes.append(5)
        elif deposito>=2:
            deposito-=2
            monedas.append(2)
        elif deposito>=1:
            deposito-=1
            monedas.append(1)
        i+=1
    print("Billetes:",billetes)
    print("Monedas:",monedas)
    
desglose()


"""Escriba un programa que sea capaz de dibujar las siguientes formas a partir de la 
seleccion y valores introducidos por el usuario, ejemplo"""

def figuras():

    select= int(input("Elije las opciones entre 1 a 3:"))
    print("Primero le pedimos nos suministre los siguientes valores:")
    lado=int(input("Lado: Escriba un valor numerico:"))
    altura=int(input("Altura: Escriba un valor numerico:"))
    ancho=int(input(" Ancho: Escriba un valor numerico:"))
    
    if select==1:
        for i in range((lado*2)-1):
           print(" "*(lado-i),"*"*(lado*i) ," "*(lado-i))

    elif select==2:
        for i in range(altura):
            print("*"*ancho)
    elif select==3:
        for i in range(altura):
            print("*"*(i+1))
            
    else:
        print("Escriba un valor entre 1 a 3")    



figuras()  

"""10.La secuencia de Collatz de un número entero se construye de la siguiente forma:
• Si el número es par, se lo divide por dos;
• Si es impar, se le multiplica tres y se le suma uno;
• La sucesión termina al llegar a uno.
La conjetura de Collatz (https://es.wikipedia.org/wiki/Conjetura_de_Collatz) afirma que, 
al partir desde cualquier número, la secuencia siempre llegará a 1. A pesar de ser una 
afirmación a simple vista muy simple, no se ha podido demostrar si es cierta o no.
Usando computadores, se ha verificado que la sucesión efectivamente llega a 1 
partiendo desde cualquier número natural menor que 2"#. Desarrolle un programa que 
grafique los largos de las secuencias de Collatz de los números enteros positivos 
menores que el ingresado por el usuario"""

number=int(input("Ingrese un numero: "))
def collatz(number=number):
    while number != 1:
        if number%2==0:
            number=int(number/2)
            print(number, "*")

        else:
            number=int(number*3+1)
            print(number, "*")
        


collatz(number)


print("Final del programa")