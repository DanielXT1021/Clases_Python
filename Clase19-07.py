#Slices // rebanadas 

# Nombre = 'Francisco'
# print(Nombre[0]) #Muestra la letra que se encuentra en el indice 0
# print(Nombre[0:3]) #Muestra desde el indice 0 al 2 es Decir "Fra", ademas la sintaxis tambien puede ser Nombre[:3] y realiza lo mismo. y en caso contrario [3:] que este empieza 
# print(Nombre[1:7:2]) # Muestra los limites del 1 al 7 saltando [1:7:2] Donde el valor 1 es el inicio, el 7 el final y por ultimo el 2 es la cantidad de espacio que se saltara 
# print(Nombre[::-1])# Imprime loss valores desde derexha a izquierda consiguiendo 

def definirPalindromo(Cadena):
    Cadena=Cadena.strip() #Elimina espacios al final de la oracion
    Cadena=Cadena.lower() # Convierte todo en minuscula
    Cadena=Cadena.replace(" ", "") #Elimina los espacion entre palabras
    CadenaInv= Cadena[::-1] 
    if Cadena==CadenaInv:
        return True
    else:
        return False
def main():
    Palabras=input("Ingrese una oracion: ")
    resultado = definirPalindromo(Palabras)
    if resultado:
        print("La oracion '",Palabras,"' Si es Palindromo")
    else:
        print("La oracion '",Palabras,"' No es Palindromo")

if __name__ == '__main__': #Punto de entrada
    main() 


 

# Palabras=input("Ingrese una oracion: ")
# resultado = definirPalindromo(Palabras)
# if resultado:
#     print("La oracion '",Palabras,"' Si es Palindromo")
# else:
#     print("La oracion '",Palabras,"' No es Palindromo")


 



