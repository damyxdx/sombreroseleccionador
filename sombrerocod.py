import random
import tkinter as tk
from tkinter import messagebox

# Definir preguntas y respuestas sin paréntesis
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
    ["HTML/CSS", "Python", "Java ", "SQL "],
    ["Con lógica ", "Con creatividad", "Con soluciones móviles ", "Con análisis estadístico"],
    ["Aplicaciones web ", "Sistemas robustos", "Aplicaciones móviles ", "Análisis y visualización de datos "],
    ["Computadoras ", "Teléfonos y tablets ", "Ambos ", "Ninguno, prefiero los datos"],
    ["No, me gusta trabajar en la interfaz ", "Sí, me encanta estructurar bases de datos ", "Solo lo necesario ", "Sí, es esencial para mis proyectos "],
    ["No, prefiero la funcionalidad ", "Sí, es clave ", "Prefiero la experiencia en apps móviles ", "No tanto, me interesa el análisis de datos"],
    ["JavaScript ", "C# ", "Kotlin", "R "],
    ["Sí, sistemas de tiempo real", "No, prefiero interfaces visuales ", "Sí, me gusta la interacción móvil", "No, prefiero la investigación de datos "],
    ["En equipo", "Solo", "Ambos", "En equipo con analistas"],
    ["Sí, mucho ", "No, prefiero construir sistemas ", "Solo lo necesario para mi app", "No, prefiero interfaces "]
]

# Puntos para las casas
casas = {
    "Frontend": 0,
    "Backend": 0,
    "Mobile": 0,
    "Data": 0
}

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Sombrero Seleccionador")

# Variables de control
indice_pregunta = 0
alumno = ""
puntos = {"Frontend": 0, "Backend": 0, "Mobile": 0, "Data": 0}

# Función para iniciar el cuestionario
def iniciar():
    global alumno
    alumno = entry_nombre.get()
    if not alumno.strip():
        messagebox.showwarning("Advertencia", "Por favor, ingresa tu nombre.")
    else:
        frame_inicio.pack_forget()
        frame_preguntas.pack(pady=10)
        mostrar_pregunta()

# Función para mostrar la siguiente pregunta
def mostrar_pregunta():
    global indice_pregunta
    if indice_pregunta < len(preguntas):
        label_pregunta.config(text=preguntas[indice_pregunta])
        for i in range(4):
            botones_respuesta[i].config(text=respuestas[indice_pregunta][i])
    else:
        determinar_casa()

# Función para manejar respuestas y sumar puntos
def manejar_respuesta(respuesta):
    global indice_pregunta
    casas["Frontend"] += 1 if respuesta == 1 else 0
    casas["Backend"] += 1 if respuesta == 2 else 0
    casas["Mobile"] += 1 if respuesta == 3 else 0
    casas["Data"] += 1 if respuesta == 4 else 0
    indice_pregunta += 1
    mostrar_pregunta()

# Función para determinar la casa y mostrar el resultado
def determinar_casa():
    frame_preguntas.pack_forget()
    max_puntos = max(casas.values())
    casas_ganadoras = [casa for casa, puntos in casas.items() if puntos == max_puntos]
    
    if len(casas_ganadoras) > 1:
        casa_elegida = random.choice(casas_ganadoras)
        resultado = f"¡Vaya! Ha sido una decisión difícil, pero {alumno}, el sombrero te ha asignado a la casa {casa_elegida}."
    else:
        casa_elegida = casas_ganadoras[0]
        resultado = f"{alumno}, el sombrero te ha asignado a la casa {casa_elegida}."
    
    label_resultado.config(text=resultado)
    frame_resultado.pack(pady=10)

# Crear los frames para organizar la interfaz
frame_inicio = tk.Frame(ventana)
frame_preguntas = tk.Frame(ventana)
frame_resultado = tk.Frame(ventana)

# Frame de inicio
label_bienvenida = tk.Label(frame_inicio, text="Bienvenido al Sombrero Seleccionador", font=("Arial", 16))
label_nombre = tk.Label(frame_inicio, text="Ingresa tu nombre:")
entry_nombre = tk.Entry(frame_inicio)
boton_iniciar = tk.Button(frame_inicio, text="Iniciar", command=iniciar)

label_bienvenida.pack(pady=10)
label_nombre.pack(pady=5)
entry_nombre.pack(pady=5)
boton_iniciar.pack(pady=10)

# Frame de preguntas
label_pregunta = tk.Label(frame_preguntas, text="", font=("Arial", 12), wraplength=400)
label_pregunta.pack(pady=10)

botones_respuesta = []
for i in range(4):
    boton = tk.Button(frame_preguntas, text="", command=lambda i=i: manejar_respuesta(i + 1))
    boton.pack(pady=5)
    botones_respuesta.append(boton)

# Frame de resultado
label_resultado = tk.Label(frame_resultado, text="", font=("Arial", 14))
label_resultado.pack(pady=10)

# Mostrar el frame de inicio al iniciar
frame_inicio.pack(pady=20)

# Iniciar la ventana principal
ventana.mainloop()

