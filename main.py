import random
import validaciones

libros = []
usuarios = []

#Funciones usuarios

def añadir_usuario():
    codigo_usuario = random.randint(10, 99) 
    nombre_usuario = input("Ingrese el nombre del usuario: ")

    for usuario in usuarios:
        if usuario[0] == codigo_usuario:
            print("El código generado",codigo_usuario,"ya existe, generando un nuevo código...")
            codigo_usuario = random.randint(10, 99)  

    usuarios.append([codigo_usuario, nombre_usuario])
    print("Usuario",nombre_usuario,"añadido con código",codigo_usuario)


def modificar_usuario():
    codigo_usuario = int(input("Ingrese el código del usuario a modificar: "))
    nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
    for usuario in usuarios:
        if usuario[0] == codigo_usuario:
            usuario[1] = nuevo_nombre
            print("Usuario con código",codigo_usuario,"modificado a",nuevo_nombre)
            return
    print("Usuario con código",codigo_usuario,"no encontrado.")

def eliminar_usuario():
    codigo_usuario = int(input("Ingrese el código del usuario a eliminar: "))
    for usuario in usuarios:
        if usuario[0] == codigo_usuario:
            usuarios.remove(usuario)
            print("Usuario con código",codigo_usuario,"eliminado.")
            return
    print("Usuario con código",codigo_usuario,"no encontrado.")


#Funciones para libros

def añadir_libro():
    num_valido = False
    while not num_valido:
        codigo_libro = input("Ingrese el código del libro: ")
        if validaciones.es_entero(codigo_libro):
            codigo_libro = int(codigo_libro)
            num_valido = True
        else:
            print("El código ingresado es incorrecto, intente nuevamente.")

    nombre_libro = input("Ingrese el nombre del libro: ")

    cantidad_valida = False
    while not cantidad_valida:
        cantidad = input("Ingrese la cantidad de libros: ")
        if validaciones.es_entero(cantidad):
            cantidad = int(cantidad)
            cantidad_valida = True
        else:
            print("Cantidad no válida, por favor ingrese un número entero positivo.")

    # Verificar si el libro ya existe
    for libro in libros:
        if libro[0] == codigo_libro:
            print("Libro con código", codigo_libro, "ya existe.")
            return

    libros.append([codigo_libro, nombre_libro, cantidad])
    print("Libro", nombre_libro, "añadido.")


def modificar_libro():
    codigo_libro = int(input("Ingrese el código del libro a modificar: "))
    nuevo_nombre = input("Ingrese el nuevo nombre del libro: ")
    nueva_cantidad = int(input("Ingrese la nueva cantidad de libros: "))
    for libro in libros:
        if libro[0] == codigo_libro:
            libro[1] = nuevo_nombre
            libro[2] = nueva_cantidad
            print("Libro con código",codigo_libro,"modificado a",nuevo_nombre,"con cantidad",nueva_cantidad)
            return
    print("Libro con código",codigo_libro,"no encontrado.")

def eliminar_libro():
    codigo_libro = int(input("Ingrese el código del libro a eliminar: "))
    for libro in libros:
        if libro[0] == codigo_libro:
            libros.remove(libro)
            print("Libro con código",codigo_libro,"eliminado.")
            return
    print("Libro con código",codigo_libro,"no encontrado.")

def mostrar_libros():
    matriz = []
    for f in range(len(libros)):
        fila = []  
        fila.append(libros[f][0])  
        fila.append(libros[f][1])  
        fila.append(libros[f][2])  
        matriz.append(fila)  
    print("\n--- Matriz de Libros ---")
    for fila in matriz:
        print(fila)  


#Menu
def mostrar_menu():
    print("\n--- Menú Biblioteca ---")
    print("1. Añadir usuario")
    print("2. Modificar usuario")
    print("3. Eliminar usuario")
    print("4. Añadir libro")
    print("5. Modificar libro")
    print("6. Eliminar libro")
    print("7. Ver usuarios")
    print("8. Ver libros")
    print("9. Salir")

def ejecutar_opcion(opcion):
    opcion = int(opcion)  # Convertir a entero después de validar
    if opcion == 1:
        añadir_usuario()
    elif opcion == 2:
        modificar_usuario()
    elif opcion == 3:
        eliminar_usuario()
    elif opcion == 4:
        añadir_libro()
    elif opcion == 5:
        modificar_libro()
    elif opcion == 6:
        eliminar_libro()
    elif opcion == 7:
        print("\nUsuarios:", usuarios)
    elif opcion == 8:
        mostrar_libros()
    elif opcion == 9:
        print("Programa finalizado")
        return False  # Indica que el programa debe terminar
    return True  # Indica que el bucle debe continuar

# Programa principal
if __name__ == "__main__":
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if validaciones.opcion_valida_menu(opcion):
            continuar = ejecutar_opcion(opcion)
        else:
            print("Entrada no válida, por favor ingrese un número entero del 1 al 9.")
