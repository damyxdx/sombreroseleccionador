import random

# Definir preguntas y respuestas
preguntas = [
    "¿Qué tecnología prefieres aprender primero?",
    "¿Cómo te gusta resolver problemas?",
    "¿Qué tipo de proyectos te interesan más?",
    "¿Qué tipo de dispositivos prefieres?",
    "¿Te gustaría trabajar con bases de datos?",
    "¿Te interesa el diseño de interfaces de usuario?",
    "¿Qué lenguaje de programación prefieres?",
    "¿Te gustan los proyectos en tiempo real?",
    "¿Prefieres trabajar en equipo o solo?",
    "¿Te gustan los proyectos de análisis de datos?"
]

respuestas = [
    ["HTML/CSS (Frontend)", "Python (Backend)", "Java (Mobile)", "SQL (Data)"],
    ["Con lógica (Backend)", "Con creatividad (Frontend)", "Con soluciones móviles (Mobile)", "Con análisis estadístico (Data)"],
    ["Aplicaciones web (Frontend)", "Sistemas robustos (Backend)", "Aplicaciones móviles (Mobile)", "Análisis y visualización de datos (Data)"],
    ["Computadoras (Backend)", "Teléfonos y tablets (Mobile)", "Ambos (Frontend)", "Ninguno, prefiero los datos (Data)"],
    ["No, me gusta trabajar en la interfaz (Frontend)", "Sí, me encanta estructurar bases de datos (Backend)", "Solo lo necesario (Mobile)", "Sí, es esencial para mis proyectos (Data)"],
    ["No, prefiero la funcionalidad (Backend)", "Sí, es clave (Frontend)", "Prefiero la experiencia en apps móviles (Mobile)", "No tanto, me interesa el análisis de datos (Data)"],
    ["JavaScript (Frontend)", "C# (Backend)", "Kotlin (Mobile)", "R (Data)"],
    ["Sí, sistemas de tiempo real (Backend)", "No, prefiero interfaces visuales (Frontend)", "Sí, me gusta la interacción móvil (Mobile)", "No, prefiero la investigación de datos (Data)"],
    ["En equipo (Frontend)", "Solo (Backend)", "Ambos (Mobile)", "En equipo con analistas (Data)"],
    ["Sí, mucho (Data)", "No, prefiero construir sistemas (Backend)", "Solo lo necesario para mi app (Mobile)", "No, prefiero interfaces (Frontend)"]
]

# Puntos para las casas
casas = {
    "Frontend": 0,
    "Backend": 0,
    "Mobile": 0,
    "Data": 0
}

# Preguntar el nombre del alumno
alumno = input("Bienvenido al sombrero seleccionador. ¿Cuál es tu nombre? ")

# Hacer las preguntas y recolectar respuestas
for i, pregunta in enumerate(preguntas):
    print(f"\nPregunta {i+1}: {pregunta}")
    for j, respuesta in enumerate(respuestas[i]):
        print(f"{j + 1}. {respuesta}")
    
    respuesta_elegida = int(input("Selecciona una opción (1-4): "))
    
    # Asignar puntos según la respuesta
    if respuesta_elegida == 1:
        casas["Frontend"] += 1
    elif respuesta_elegida == 2:
        casas["Backend"] += 1
    elif respuesta_elegida == 3:
        casas["Mobile"] += 1
    elif respuesta_elegida == 4:
        casas["Data"] += 1

# Mostrar resultados
max_puntos = max(casas.values())
casas_ganadoras = [casa for casa, puntos in casas.items() if puntos == max_puntos]

# Resolver empates
if len(casas_ganadoras) > 1:
    casa_elegida = random.choice(casas_ganadoras)
    print(f"\n¡Vaya! Ha sido una decisión difícil, pero {alumno}, el sombrero te ha asignado a la casa {casa_elegida}!")
else:
    casa_elegida = casas_ganadoras[0]
    print(f"\n{alumno}, el sombrero te ha asignado a la casa {casa_elegida}!")
