import random

def iniciar_juego():
    palabras = ["gato", "perro", "elefante", "tigre", "leon", "jirafa", "lobo", "oso", 
                "serpiente", "aguila", "caballo", "conejo", "ardilla", "zorro", "delfin"]

    random.shuffle(palabras)
    palabras = palabras[:7]  

    correctas = 0
    incorrectas = 0
    
    for palabra in palabras:
        respuesta = input(f"Escribe la palabra: {palabra}\n").strip()
        if respuesta == palabra:
            print("Correcto")
            correctas += 1
        else:
            print("Incorrecto")
            incorrectas += 1
    
    porcentaje_acierto = (correctas / 7) * 100 
    print(f"Acabaste el juego.")
    print(f"Palabras correctas: {correctas}")
    print(f"Palabras incorrectas: {incorrectas}")
    print(f"Porcentaje de precisión: {porcentaje_acierto:.2f}%")
    iniciar_juego()