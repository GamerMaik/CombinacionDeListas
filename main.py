import json
from itertools import product

# Definir las listas de colores, frases, me gusta y no me gusta
colores = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
frases = ["frase positiva", "frase negativa","frase neutra"]
reacciones = ["me gusta", "no me gusta"]
horas = ["am", "pm"]

# Generar todas las combinaciones posibles de las variables
combinaciones = list(product(colores, colores, frases, reacciones, horas))

# Estructura para almacenar los resultados
resultados = []

# Analizar cada combinación y determinar la emoción o actitud
for combinacion in combinaciones:
    fondo, texto, frase, reaccion, hora = combinacion
    # Realizar el análisis de la combinación aquí según tus criterios
    # Puedes agregar lógica para determinar la emoción basada en las combinaciones

    # Agregar resultados al diccionario de resultados
    resultado = {
        "fondo": fondo,
        "texto": texto,
        "frase": frase,
        "reaccion": reaccion,
        "hora": hora,
        # Agregar aquí los resultados del análisis
        # Por ejemplo: "emocion": "triste"
    }
    resultados.append(resultado)

# Guardar los resultados en un archivo JSON
with open("resultados_experimento.json", "w") as outfile:
    json.dump(resultados, outfile)

print("Experimento completado. Los resultados se han guardado en 'resultados_experimento.json'.")

