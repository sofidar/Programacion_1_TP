def es_entero(valor):
    return valor.isdigit() and int(valor) > 0

def opcion_valida_menu(opcion):
    return opcion.isdigit() and 1 <= int(opcion) <= 9