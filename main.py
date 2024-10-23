import random
import validaciones


# Funciones para usuarios

def añadir_usuario(usuarios_codigos, usuarios_nombres):
    codigo_usuario = random.randint(10, 99)
    nombre_usuario = input("Ingrese el nombre del usuario: ")
    while not nombre_usuario.isalpha():
        print("Solo se pueden ingresar letras")
        nombre_usuario = input("Ingrese el nombre del usuario: ")

    while codigo_usuario in usuarios_codigos:
        print(f"El codigo {codigo_usuario} ya existe, generando un nuevo código...")
        codigo_usuario = random.randint(10, 99)

    usuarios_codigos.append(codigo_usuario)
    usuarios_nombres.append(nombre_usuario)
    print(f"Usuario {nombre_usuario} añadido con codigo {codigo_usuario}")


def modificar_usuario(usuarios_codigos, usuarios_nombres):
    while True:
        try:
            codigo_usuario = int(input("Ingrese el codigo del usuario a modificar: "))
            break
        except ValueError:
            print("Ingrese un numero valido")
    
    if codigo_usuario in usuarios_codigos:
        nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
        while not nuevo_nombre.isalpha():
            print("Solo se pueden ingresar letras")
            nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
        indice = usuarios_codigos.index(codigo_usuario)
        usuarios_nombres[indice] = nuevo_nombre
        print(f"Usuario con codigo {codigo_usuario} modificado a {nuevo_nombre}")
    else:
        print(f"Usuario con codigo {codigo_usuario} no encontrado.")


def eliminar_usuario(usuarios_codigos, usuarios_nombres):
    while True:
        try:
            codigo_usuario = int(input("Ingrese el codigo del usuario a eliminar: "))
            break
        except ValueError:
            print("Ingrese un numero valido")
    if codigo_usuario in usuarios_codigos:
        indice = usuarios_codigos.index(codigo_usuario)
        usuarios_codigos.pop(indice)
        usuarios_nombres.pop(indice)
        print(f"Usuario con codigo {codigo_usuario} eliminado.")
    else:
        print(f"Usuario con codigo {codigo_usuario} no encontrado.")


# Funciones para libros

def añadir_libro(libros_codigos, libros_nombres, libros_cantidades, libros_precios):
    num_valido = False
    while not num_valido:
        codigo_libro = input("Ingrese el codigo del libro: ")
        if not codigo_libro.isalpha() and validaciones.es_entero(codigo_libro):
            codigo_libro = int(codigo_libro)
            num_valido = True
        else:
            print("El codigo ingresado es incorrecto, intente nuevamente.")

    nombre_libro = input("Ingrese el nombre del libro: ")
    while validaciones.cadena_vacia(nombre_libro):
        print("Debe ingresar un nombre")
        nombre_libro = input("Ingrese el nombre del libro: ")

    cantidad_valida = False
    while not cantidad_valida:
        cantidad_libro = input("Ingrese la cantidad de libros: ")
        if not cantidad_libro.isalpha() and validaciones.es_entero(cantidad_libro):
            cantidad_libro = int(cantidad_libro)
            cantidad_valida = True
        else:
            print("La cantidad ingresada es incorrecta, intente nuevamente.")

    precio_valido = False
    while not precio_valido:
        precio_libro = input("Ingrese el precio del libro: ")
        if not precio_libro.isalpha() and validaciones.es_entero(precio_libro):
            precio_libro = int(precio_libro)
            precio_valido = True
        else:
            print("El precio ingresado es incorrecto, intente nuevamente.")

    if codigo_libro in libros_codigos:
        print(f"Libro con codigo {codigo_libro} ya existe.")
        return

    libros_codigos.append(codigo_libro)
    libros_nombres.append(nombre_libro)
    libros_cantidades.append(cantidad_libro)
    libros_precios.append(precio_libro)
    print(f"Libro {nombre_libro} añadido.")


def modificar_libro(libros_codigos, libros_nombres, libros_cantidades, libros_precios):
    while True:
        try:
            codigo_libro = int(input("Ingrese el codigo del libro a modificar: "))
            break
        except ValueError:
            print("Ingrese un numero valido")
            
    if codigo_libro in libros_codigos:
        indice = libros_codigos.index(codigo_libro)
        
        nuevo_nombre = input("Ingrese el nuevo nombre del libro: ")
        while validaciones.cadena_vacia(nuevo_nombre):
            print("Debe ingresar un nombre")
            nuevo_nombre = input("Ingrese el nuevo nombre del libro: ")
        
        cantidad_valida = False
        while not cantidad_valida:
            nueva_cantidad = input("Ingrese la nueva cantidad de libros: ")
            if not nueva_cantidad.isalpha() and validaciones.es_entero(nueva_cantidad):
                nueva_cantidad = int(nueva_cantidad)
                cantidad_valida = True
            else:
                print("La cantidad ingresada es incorrecta, intente nuevamente.")
            
        precio_valido = False
        while not precio_valido:
            nuevo_precio = input("Ingrese el nuevo precio del libro: ")
            if not nuevo_precio.isalpha() and validaciones.es_entero(nuevo_precio):
                nuevo_precio = int(nuevo_precio)
                precio_valido = True
            else:
                print("El precio ingesado es incorrecto, intente nuevamente.")
                
        libros_nombres[indice] = nuevo_nombre
        libros_cantidades[indice] = nueva_cantidad
        libros_precios[indice] = nuevo_precio
        print(f"Libro con codigo {codigo_libro} modificado a {nuevo_nombre} con cantidad {nueva_cantidad} y precio {nuevo_precio}")
    else:
        print(f"Libro con codigo {codigo_libro} no encontrado.")


def eliminar_libro(libros_codigos, libros_nombres, libros_cantidades, libros_precios):
    while True:
        try:
            codigo_libro = int(input("Ingrese el codigo del libro a eliminar: "))
            break
        except ValueError:
            print("Ingrese un numero valido")
            
    if codigo_libro in libros_codigos:
        indice = libros_codigos.index(codigo_libro)
        libros_codigos.pop(indice)
        libros_nombres.pop(indice)
        libros_cantidades.pop(indice)
        libros_precios.pop(indice)
        print(f"Libro con codigo {codigo_libro} eliminado.")
    else:
        print(f"Libro con codigo {codigo_libro} no encontrado.")


# def mostrar_libros(libros_codigos, libros_cantidades, libros_precios):
    # Imprimir archivo con nombre de libro, precio...


# def reservar_libros(libros_codigos_cantidades):
    
        
        
#Funciones para archivos

def generar_archivo_libros(libros_codigos, libros_cantidades, libros_precios):
    try:
        archivo_libros = open("libros.csv", mode='wt')
    except IOError:
        print("No se pudo crear el archivo")
    else:
        for elemento in range (len(libros_codigos)):
            archivo_libros.write(str(libros_codigos[elemento])+";"+str(libros_cantidades[elemento])+";"+str(libros_precios[elemento])+"\n")
        archivo_libros.close()
    
    return


# Menú

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
    print("9. Hacer una reserva")
    print("10. Salir")


def ejecutar_opcion(opcion, usuarios_codigos, usuarios_nombres, libros_codigos, libros_nombres, libros_cantidades, libros_precios):
    if opcion == 1:
        añadir_usuario(usuarios_codigos, usuarios_nombres)
    elif opcion == 2:
        modificar_usuario(usuarios_codigos, usuarios_nombres)
    elif opcion == 3:
        eliminar_usuario(usuarios_codigos, usuarios_nombres)
    elif opcion == 4:
        añadir_libro(libros_codigos, libros_nombres, libros_cantidades, libros_precios)
    elif opcion == 5:
        modificar_libro(libros_codigos, libros_nombres, libros_cantidades, libros_precios)
    elif opcion == 6:
        eliminar_libro(libros_codigos, libros_nombres, libros_cantidades, libros_precios)
    elif opcion == 7:
        print("\nUsuarios:")
        for i in range(len(usuarios_codigos)):
            print(f"Codigo: {usuarios_codigos[i]}, Nombre: {usuarios_nombres[i]}")
    elif opcion == 8:
        mostrar_libros(libros_codigos, libros_cantidades, libros_precios)
    elif opcion == 9:
        reservar_libros(libros_codigos_cantidades)
    elif opcion == 10:
        generar_archivo_libros(libros_codigos, libros_cantidades, libros_precios)
        print("Programa finalizado")
        return False  # Indica que el programa debe terminar
    return True  # Indica que el bucle debe continuar


# Función principal

def main():
    usuarios_codigos = []
    usuarios_nombres = []
    libros_codigos = []
    libros_nombres = []
    libros_cantidades = []
    libros_precios = []

    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if validaciones.opcion_valida_menu(opcion):
            continuar = ejecutar_opcion(int(opcion), usuarios_codigos, usuarios_nombres, libros_codigos, libros_nombres, libros_cantidades, libros_precios)
        else:
            print("Entrada no valida, por favor ingrese un numero entero del 1 al 10.")


if __name__ == "__main__":
    main()
