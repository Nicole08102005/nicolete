#con ciclos
def es_bisiesto(anio):
    if (anio  % 4 == 0 and anio  % 100 != 0) or (anio  %  400 == 0):
        return True
    return False

def contar_bisiestos_con_ciclo(anio):
    contador = 0
    for i in range(1900, anio  + 1):
        if es_bisiesto(i):
            contador += 1
    return contador

anio_usuario = int(input("Ingrese un año entre 1900 y 2199: "))
if 1900 <= anio_usuario <= 2199:
    print(f"El año {anio_usuario} {'es' if es_bisiesto(anio_usuario) else 'no es'} bisiesto.")
    print(f"Número de años bisiestos entre 1900 y {anio_usuario}: {contar_bisiestos_con_ciclo(anio_usuario)}")
else:
    print("El año ingresado no está en el rango permitido.")

    #sin ciclos 

def es_bisiesto (anio):
    return (anio  % 4 == 0 and anio  % 100 != 0) or ( anio  % 400 == 0)

def contar_bisiestos_sin_ciclo(anio ):
    bisiestos = [i for i in range(1900, anio + 1) if es_bisiesto(i)]
    return len(bisiestos)

anio_usuario = int(input("Ingrese un año entre 1900 y 2199: "))
if 1900 <=año_usuario <= 2199:
    print(f"El año {anio_usuario} {'es' if es_bisiesto(anio_usuario) else 'no es'} bisiesto.")
    print(f"Número de años bisiestos entre 1900 y {anio_usuario}: {contar_bisiestos_sin_ciclo(anio_usuario)}")
else:
    print("El año ingresado no está en el rango permitido.")