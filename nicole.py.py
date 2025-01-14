def mostrar_receta():
    print("\nReceta: Masa para preparar arepas")
    print("Ingredientes:")
    print("1 taza de agua (o 16 cucharaditas)")
    print("1 taza de harina pan (o 16 cucharaditas)")
    print("1 cucharadita de sal.")
    print("1 cucharada de aceite.")

def preparar_arepa(agua,harina,aceite):
    print("\nPreparacion de la masa:")
    print("1. En un recipiente, vierte la taza de agua.")
    print(f"2. Agrega la taza de harina pan.")
    print(f"3. Agrega {sal}cucharadita.")
    print(f"4. Incorpora{aceite}cucharadas.")
    print("5. Mezcla bien los ingredientes, hasta obtener una masa suave y homogenea.")
    print("6. Deja reposar la masa 5 minutos antes de usarla.")
    # consideramos la evaporacion del 10% del volumen de agua durante la coccion
    agua_restante = agua * 16 * 0.9 # 10% de evaporacion 
    print(f"\nDurante la coccion, se evapora el 10% del agua.")

    # Pasos adicionales de preparacion 
    print("7. Divide la masa en bolitas.")
    print("8. Aplasta las bolitas con la mano hasta formar un disco.")
    print("9. Calienta el budare y viertele un chorrito de aceite.")
    print("10. Coloca las bolitas de masa en el budare una vez caliente y cocina hasta que se dore de ambos lados.")
    
    print("\nLas arepas estan listas para servirse.")

# ingredientes de la receta en gramos
harina = 120 # gramos
agua = 240 # gramos
sal = 5 # gramos
aceite = 15 # gramos

# cantidad total de la receta antes de la evaporacion 
total_inicial = harina + agua + sal + aceite

# paso despues de la evaporacion 
total_despues_evaporacion = total_inicial * 0.90
 
# calculo del porcentaje de cada ingrediente despues de la evaporacion
porcentaje_harina = (harina / total_despues_evaporacion) * 100
porcentaje_agua = (agua / total_despues_evaporacion) * 100
porcentaje_sal = (sal / total_despues_evaporacion) * 100
porcentaje_aceite = (aceite / total_despues_evaporacion) * 100

# mostrar los resultados
print(f"Porcentaje de harina: {porcentaje_harina:.2f}%")
print(f"Porcentaje de agua: {porcentaje_agua:.2f}%")
print(f"Porcentaje de sal: {porcentaje_sal:.2f}")
print(f"Porcentaje de aceite:{porcentaje_aceite:.2f}")

def pedir_ingredientes():
    try:
        agua = float(input("¿Cuantas tazas de agua deseas usar? (por defecto 1 taza):") or 1)
        harina = float(input("¿Cuantas tazas de harina pan deseas usar? (por defecto 1 taza):") or 1)
        sal = float(input("¿Cuantas cucharaditas de sal deseas usar? (por defecto 1 cucharadita):") or 1)
        aceite = float(input("¿Cuantas cucharadas de aceite deseas usar? (por defecto 1 cucharada):") or 1)

        return agua, harina, sal, aceite 
    except ValueError:
        print("Por favor, ingresa un valor numerico valido.")
        return pedir_ingredientes ()

def main():
    print("Bienvenidos al programa de cocina de arepas.\n")
    mostrar_receta

    # Pedir al usuario la cantidad de ingredientes que quiere usar
    agua, harina, sal, aceite = pedir_ingredientes()

    # Preparar la masa con las cantidades elegidas
    preparar_masa(agua, harina, sal, aceite)


