
import tkinter as tk
from tkinter import messagebox

# Preguntas del juego, podemos agregar mas preguntas si queremos
preguntas = [
    {
        "pregunta": "Un compañero se olvida sus útiles. ¿Qué valor ponemos en práctica si lo ayudamos?",
        "opciones": ["Respeto", "Solidaridad", "Egoísmo"],
        "correcta": "Solidaridad"
    },
    {
        "pregunta": "Encontrás una billetera en el aula. ¿Qué deberías hacer?",
        "opciones": ["Quedártela", "Ignorarla", "Devolverla"],
        "correcta": "Devolverla"
    },
    {
        "pregunta": "Llegás tarde a clase. ¿Qué actitud demuestra responsabilidad?",
        "opciones": ["Reconocerlo", "Culpar a otro", "Interrumpir la clase"],
        "correcta": "Reconocerlo"
    }
]

# Variables
puntos = 0
numero_pregunta = 0

# Función para comprobar la respuesta
def comprobar_respuesta(respuesta):
    global puntos, numero_pregunta

    if respuesta == preguntas[numero_pregunta]["correcta"]:
        puntos += 1
        messagebox.showinfo("Resultado", "¡Correcto! Muy bien.")
    else:
        messagebox.showinfo(
            "Resultado",
            "Respuesta incorrecta. La respuesta correcta es: "
            + preguntas[numero_pregunta]["correcta"]
        )

    numero_pregunta += 1
    mostrar_pregunta()


# Función para mostrar las preguntas
def mostrar_pregunta():
    if numero_pregunta < len(preguntas):
        pregunta_actual = preguntas[numero_pregunta]

        etiqueta_pregunta.config(
            text=pregunta_actual["pregunta"]
        )

        for i in range(3):
            botones[i].config(
                text=pregunta_actual["opciones"][i],
                command=lambda respuesta=pregunta_actual["opciones"][i]:
                comprobar_respuesta(respuesta)
            )

        etiqueta_progreso.config(
            text="Pregunta " + str(numero_pregunta + 1)
            + " de " + str(len(preguntas))
        )

    else:
        etiqueta_pregunta.config(
            text="¡Juego terminado!\n\nPuntaje: "
            + str(puntos) + " de " + str(len(preguntas))
        )

        for boton in botones:
            boton.config(state="disabled")

        etiqueta_progreso.config(text="Gracias por participar")


# Ventana principal
ventana = tk.Tk()
ventana.title("Juego de Valores")
ventana.geometry("550x400")
ventana.config(bg="#EAF2F8")

# Título
titulo = tk.Label(
    ventana,
    text="JUEGO DE VALORES Y CONVIVENCIA",
    font=("Arial", 16, "bold"),
    bg="#EAF2F8"
)
titulo.pack(pady=20)

# Pregunta
etiqueta_pregunta = tk.Label(
    ventana,
    text="",
    font=("Arial", 12),
    wraplength=480,
    bg="#EAF2F8"
)
etiqueta_pregunta.pack(pady=20)

# Botones de respuestas
botones = []

for i in range(3):
    boton = tk.Button(
        ventana,
        text="",
        font=("Arial", 11),
        width=30,
        command=lambda: None
    )
    boton.pack(pady=5)
    botones.append(boton)

# Progreso
etiqueta_progreso = tk.Label(
    ventana,
    text="",
    font=("Arial", 10),
    bg="#EAF2F8"
)
etiqueta_progreso.pack(pady=15)

# Iniciar juego
mostrar_pregunta()

# Mantener abierta la ventana
ventana.mainloop()
