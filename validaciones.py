def es_entero(numero):
    return numero.isdigit() and int(numero) > 0

def opcion_valida_menu(opcion):
    return opcion.isdigit() and 1 <= int(opcion) <= 11

def cadena_vacia(cadena):
    if len(cadena) == 0:
        return True
    else:
        return False
    
def es_natural():
    # Verifica que numero sea natural con excepciones
    while True:
        try:
                numero=int(input())
                division=10/numero
        except ValueError:
                print("No se puede ingresar texto, o numeros decimales")
                continue
        except ZeroDivisionError:
                print("No se puede ingresar 0")
                continue
        try:
            assert numero>0
        except AssertionError:
            print("No se pueden ingresar números negativos")
            continue
        break
    return numero
