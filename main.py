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
    print("Ingrese el codigo del usuario a modificar: ")
    codigo_usuario = validaciones.es_natural()
    
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
    print("Ingrese el codigo del usuario a eliminar: ")
    codigo_usuario = validaciones.es_natural()
            
    if codigo_usuario in usuarios_codigos:
        indice = usuarios_codigos.index(codigo_usuario)
        usuarios_codigos.pop(indice)
        usuarios_nombres.pop(indice)
        print(f"Usuario con codigo {codigo_usuario} eliminado.")
    else:
        print(f"Usuario con codigo {codigo_usuario} no encontrado.")


# Funciones para libros

def añadir_libro(libros_codigos, libros_nombres, libros_cantidades, libros_precios, cantidad_reservas):
    print("Ingrese el codigo del libro: ")
    codigo_libro = validaciones.es_natural()

    nombre_libro = input("Ingrese el nombre del libro: ")
    while validaciones.cadena_vacia(nombre_libro):
        print("Debe ingresar un nombre")
        nombre_libro = input("Ingrese el nombre del libro: ")

    print("Ingrese el stock del libro: ")
    cantidad_libro = validaciones.es_natural()

    precio_valido = False
    while not precio_valido:
        precio_libro = input("Ingrese el precio del libro: ")
        if not precio_libro.isalpha():
            precio_valido = True
        else:
            print("El precio ingresado es incorrecto, intente nuevamente.")

    if codigo_libro in libros_codigos:
        print(f"Libro con codigo {codigo_libro} ya existe.")
    else:
        libros_codigos.append(codigo_libro)
        libros_nombres.append(nombre_libro)
        libros_cantidades.append(cantidad_libro)
        libros_precios.append(precio_libro)
        cantidad_reservas.append(0)
        print(f"Libro {nombre_libro} añadido.")


def modificar_libro(libros_codigos, libros_nombres, libros_cantidades, libros_precios):
    print("Ingrese el codigo del libro a modificar: ")
    codigo_libro = validaciones.es_natural()
            
    if codigo_libro in libros_codigos:
        indice = libros_codigos.index(codigo_libro)
        
        nuevo_nombre = input("Ingrese el nuevo nombre del libro: ")
        while validaciones.cadena_vacia(nuevo_nombre):
            print("Debe ingresar un nombre")
            nuevo_nombre = input("Ingrese el nuevo nombre del libro: ")
        
        print("Ingrese la nueva cantidad de libros: ")
        nueva_cantidad = validaciones.es_natural()
            
        precio_valido = False
        while not precio_valido:
            nuevo_precio = input("Ingrese el nuevo precio del libro: ")
            if not nuevo_precio.isalpha():
                precio_valido = True
            else:
                print("El precio ingresado es incorrecto, intente nuevamente.")
                
        libros_nombres[indice] = nuevo_nombre
        libros_cantidades[indice] = nueva_cantidad
        libros_precios[indice] = nuevo_precio
        print(f"Libro con codigo {codigo_libro} modificado a {nuevo_nombre} con cantidad {nueva_cantidad} y precio {nuevo_precio}")
    else:
        print(f"Libro con codigo {codigo_libro} no encontrado.")


def eliminar_libro(libros_codigos, libros_nombres, libros_cantidades, libros_precios):
    print("Ingrese el codigo del libro a eliminar: ")
    codigo_libro = validaciones.es_natural()
            
    if codigo_libro in libros_codigos:
        indice = libros_codigos.index(codigo_libro)
        libros_codigos.pop(indice)
        libros_nombres.pop(indice)
        libros_cantidades.pop(indice)
        libros_precios.pop(indice)
        cantidad_reservas.pop(indice)
        print(f"Libro con codigo {codigo_libro} eliminado.")
    else:
        print(f"Libro con codigo {codigo_libro} no encontrado.")


def mostrar_libros(libros_codigos, libros_cantidades, libros_precios):
    diccionario_libros={}
    
    for i in range(len(libros_codigos)):
        diccionario_libros[libros_codigos[i]]=[libros_cantidades[i],libros_precios[i]]
        
    print("Código, Cantidad, Precio","\n")
    for codigo,(cantidad, precio) in diccionario_libros.items():
        print(codigo,"        ",cantidad,"         ",precio)
    return diccionario_libros


def reservar_libros(libros_codigos, libros_cantidades, libros_nombres, libros_precios, usuarios_codigos, codusuarios_reservados, codlibros_reservados, precioslibros_reservados, cantidad_reservas, usuarios_a_tiempo):
    
    print("Ingrese el codigo del usuario que hace la reserva: ")
    codigo_usuario = validaciones.es_natural()
    
    if codigo_usuario not in usuarios_codigos:
        print(f"El cliente con código {codigo_usuario} no existe.")
        
        return codusuarios_reservados, codlibros_reservados, precioslibros_reservados
            
    print("Ingrese el codigo del libro que se desee reservar: ")
    codigo_libro = validaciones.es_natural()
            
    if codigo_libro in libros_codigos:
        try:
            subindice_libro = libros_codigos.index(codigo_libro)
        except ValueError:
            print("El codigo de usuario no existe")
        if libros_cantidades[subindice_libro] > 0:
            libros_cantidades[subindice_libro] -= 1
            codusuarios_reservados.append(codigo_usuario)
            codlibros_reservados.append(codigo_libro)
            precioslibros_reservados.append(libros_precios[subindice_libro])
        else:
            print(f"Todos los libros código: {codigo_libro}, nombre: {libros_nombres[subindice_libro]} se encuentran reservados")
    else:
        print(f"El libro con código {codigo_libro} no existe en el inventario.")
    cantidad_reservas[subindice_libro] += 1
    print(codusuarios_reservados, codlibros_reservados, precioslibros_reservados)      
    return codusuarios_reservados, codlibros_reservados, precioslibros_reservados

def devolver_libros(codusuarios_reservados, codlibros_reservados, libros_cantidades, precioslibros_reservados, usuarioscondeudas, deudas, cantidad_deudas, cantidad_a_tiempo, usuarios_deudas, libros_deudas):
    print("Ingrese el codigo del usuario que hace la devolución: ")
    codigo_usuario = validaciones.es_natural()

    if codigo_usuario not in codusuarios_reservados:
        print(f"El cliente con código {codigo_usuario} no tiene reservas.")
        return usuarioscondeudas, deudas
    
    print("Ingrese el codigo del libro que se desee devolver: ")
    codigo_libro = validaciones.es_natural()
    
    # Usar while con índice en lugar de for para evitar modificar listas mientras iteramos
    i = 0
    while i < len(codusuarios_reservados):
        if codusuarios_reservados[i] == codigo_usuario and codlibros_reservados[i] == codigo_libro:
            # Pregunta si el libro fue devuelto a tiempo
            tiempodevolucion = input("¿Fue el libro devuelto a tiempo? (s/n): ").lower()
            while tiempodevolucion not in ['s', 'n']:
                print("Por favor, ingrese 's' para sí o 'n' para no.")
                tiempodevolucion = input("¿Fue el libro devuelto a tiempo? (s/n): ").lower()
            
            # Si no fue devuelto a tiempo, agrega deuda
            if tiempodevolucion == 'n':
                auxiliar=int(precioslibros_reservados[i])
                multa = auxiliar * 0.50
                if codigo_usuario in usuarioscondeudas:
                    idx = usuarioscondeudas.index(codigo_usuario)
                    deudas[idx] += multa
                    cantidad_deudas[idx] += 1
                else:
                    usuarioscondeudas.append(codigo_usuario)
                    deudas.append(multa)
                    cantidad_deudas.append(1)
                usuarios_deudas.append(codigo_usuario)
                libros_deudas.append(codigo_libro)
                print(f"Se ha añadido una multa de {multa} para el usuario {codigo_usuario}")
            else:
                if codigo_usuario in usuarios_a_tiempo:
                    idx2 = usuarios_a_tiempo.index(codigo_usuario)
                    cantidad_a_tiempo[idx2] += 1
                else:
                    usuarios_a_tiempo.append(codigo_usuario)
                    cantidad_a_tiempo.append(1)
            # Devolver libro al inventario y eliminar reserva
            subindice_libro = codlibros_reservados.index(codigo_libro)
            libros_cantidades[subindice_libro] += 1
            codusuarios_reservados.pop(i)
            codlibros_reservados.pop(i)
            precioslibros_reservados.pop(i)
            print(f"Libro con código {codigo_libro} devuelto por usuario {codigo_usuario}.")
            break
        i += 1

    print("Estado actual de reservas:")
    print("Usuarios reservados:", codusuarios_reservados)
    print("Libros reservados:", codlibros_reservados)
    print("Precios reservados:", precioslibros_reservados)
    print("Usuarios con deudas:", usuarioscondeudas)
    print("Deudas:", deudas)
    print("Cantidad de Deudas: ",cantidad_deudas)
    print("Cantidad Devuelta a Tiempo: ",cantidad_a_tiempo)
    
    return usuarioscondeudas, deudas
                
#Funciones para archivos

def generar_archivo_libros(libros_codigos, libros_cantidades, libros_precios):
    print(libros_codigos, libros_cantidades, libros_precios)
    try:
        archivo_libros = open("libros.csv", mode='wt')
    except IOError:
        print("No se pudo crear el archivo")
    else:
        for elemento in range (len(libros_codigos)):
            archivo_libros.write(str(libros_codigos[elemento])+";"+str(libros_cantidades[elemento])+";"+str(libros_precios[elemento])+"\n")
        archivo_libros.close()
    
    return

def generar_archivo_usuarios(usuarios_codigos, usuarios_nombres):
    print(usuarios_codigos, usuarios_nombres)
    try:
        archivo_usuarios = open("usuarios.csv", mode='wt')
    except IOError:
        print("No se pudo crear el archivo")
    else:
        for elemento in range (len(usuarios_codigos)):
            archivo_usuarios.write(str(usuarios_codigos[elemento])+";"+str(usuarios_nombres[elemento])+"\n")
        archivo_usuarios.close()
    
    return

def generar_archivo_reservas(codusuarios_reservados, codlibros_reservados):
    try:
        archivo_libros_reservados = open("reservas.csv", mode='wt')
    except IOError:
        print("No se pudo crear el archivo")
    else:
        for elemento in range (len(codusuarios_reservados)):
            archivo_libros_reservados.write(str(codusuarios_reservados[elemento])+";"+str(codlibros_reservados[elemento])+"\n")
        archivo_libros_reservados.close()
    
    return

def generar_archivo_historial_reservas(libros_codigos, libros_nombres, cantidad_reservas):
    try:
        archivo_historial_reservas = open("historialreservas.csv", mode='wt')
    except IOError:
        print("No se pudo crear el archivo")
    else:
        for elemento in range (len(libros_codigos)):
            archivo_historial_reservas.write(str(libros_codigos[elemento])+";"+str(libros_nombres[elemento])+";"+str(cantidad_reservas[elemento])+"\n")
        archivo_historial_reservas.close()
    
    return

def generar_archivo_historial_deudas(usuarios_deudas, deudas, cantidad_deudas):
    try:
        archivo_historial_deudas = open("historialdeudas.csv", mode='wt')
    except IOError:
        print("No se pudo crear el archivo")
    else:
        for elemento in range (len(usuarios_deudas)):
            archivo_historial_deudas.write(str(usuarios_deudas[elemento])+";"+str(deudas[elemento])+";"+str(cantidad_deudas[elemento])+"\n")
        archivo_historial_deudas.close()
    
    return

def generar_archivo_devoluciones_tarde(libros_deudas, cantidad_deudas):
    try:
        archivo_devoluciones_tarde = open("devolucionestarde.csv", mode='wt')
    except IOError:
        print("No se pudo crear el archivo")
    else:
        for elemento in range (len(libros_deudas)):
            archivo_devoluciones_tarde.write(str(libros_deudas[elemento])+";"+str(cantidad_deudas[elemento])+"\n")
        archivo_devoluciones_tarde.close()
    
    return 

def generar_archivo_devoluciones_a_tiempo(usuarios_a_tiempo, cantidad_a_tiempo):
    try:
        archivo_devoluciones_a_tiempo = open("devolucionesatiempo.csv", mode='wt')
    except IOError:
        print("No se pudo crear el archivo")
    else:
        for elemento in range (len(usuarios_a_tiempo)):
            archivo_devoluciones_a_tiempo.write(str(usuarios_a_tiempo[elemento])+";"+str(cantidad_a_tiempo[elemento])+"\n")
        archivo_devoluciones_a_tiempo.close()
    
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
    print("10. Devolver un libro")
    print("11. Salir")


def ejecutar_opcion(opcion, usuarios_codigos, usuarios_nombres, libros_codigos, libros_nombres, libros_cantidades, libros_precios, codusuarios_reservados, codlibros_reservados, precioslibros_reservados, usuarioscondeudas, deudas, cantidad_reservas, cantidad_deudas, cantidad_a_tiempo, usuarios_deudas, libros_deudas, usuarios_a_tiempo):
    if opcion == 1:
        añadir_usuario(usuarios_codigos, usuarios_nombres)
    elif opcion == 2:
        modificar_usuario(usuarios_codigos, usuarios_nombres)
    elif opcion == 3:
        eliminar_usuario(usuarios_codigos, usuarios_nombres)
    elif opcion == 4:
        añadir_libro(libros_codigos, libros_nombres, libros_cantidades, libros_precios, cantidad_reservas)
    elif opcion == 5:
        modificar_libro(libros_codigos, libros_nombres, libros_cantidades, libros_precios)
    elif opcion == 6:
        eliminar_libro(libros_codigos, libros_nombres, libros_cantidades, libros_precios)
    elif opcion == 7:
        print("\nUsuarios:")
        for codigo, nombre in zip(usuarios_codigos, usuarios_nombres):
            print(f"Codigo: {codigo}, Nombre: {nombre}")
    elif opcion == 8:
        mostrar_libros(libros_codigos, libros_cantidades, libros_precios)
    elif opcion == 9:
        codusuarios_reservados, codlibros_reservados, precioslibros_reservados = reservar_libros(libros_codigos, libros_cantidades, libros_nombres, libros_precios, usuarios_codigos, codusuarios_reservados, codlibros_reservados, precioslibros_reservados, cantidad_reservas, usuarios_a_tiempo)
    elif opcion == 10:
        usuarioscondeudas, deudas = devolver_libros(codusuarios_reservados, codlibros_reservados, libros_cantidades, precioslibros_reservados, usuarioscondeudas, deudas, cantidad_deudas, cantidad_a_tiempo, usuarios_deudas, libros_deudas)
    elif opcion == 11:
        generar_archivo_libros(libros_codigos, libros_cantidades, libros_precios)
        generar_archivo_reservas(codusuarios_reservados, codlibros_reservados)
        generar_archivo_historial_reservas(libros_codigos, libros_nombres, cantidad_reservas)
        generar_archivo_historial_deudas(usuarios_deudas, deudas, cantidad_deudas)
        generar_archivo_devoluciones_tarde(libros_deudas, cantidad_deudas)
        generar_archivo_usuarios(usuarios_codigos, usuarios_nombres)
        generar_archivo_devoluciones_a_tiempo(usuarios_a_tiempo, cantidad_a_tiempo)
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
    codusuarios_reservados=[]
    codlibros_reservados=[]
    precioslibros_reservados=[]
    usuarioscondeudas=[]
    deudas=[]
    cantidad_reservas = []
    cantidad_deudas = []
    cantidad_a_tiempo = []
    usuarios_deudas = []
    libros_deudas = []
    usuarios_a_tiempo = []
    
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if validaciones.opcion_valida_menu(opcion):
            continuar = ejecutar_opcion(int(opcion), usuarios_codigos, usuarios_nombres, libros_codigos, libros_nombres, libros_cantidades, libros_precios, codusuarios_reservados, codlibros_reservados, precioslibros_reservados, usuarioscondeudas, deudas, cantidad_reservas, cantidad_deudas,cantidad_a_tiempo, usuarios_deudas, libros_deudas, usuarios_a_tiempo)
        else:
            print("Entrada no valida, por favor ingrese un numero entero del 1 al 10.")


if __name__ == "__main__":
    main()

