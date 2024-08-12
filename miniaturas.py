#Konekt4
#Fecha: 11/08/2024
#Versión: 0.2

from tkinter import *
from os import system
from PIL import Image, ImageTk

def descargar_miniatura():
    video_id = video_id_entry.get()
    if video_id:
        miniatura_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        system(f"curl -k -o {video_id}.jpg {miniatura_url}")
        resultado_label.config(text="Miniatura descargada", fg="green")

        # Cargar y mostrar la miniatura descargada
        img = Image.open(f"{video_id}.jpg")
        img = img.resize((320, 180))  # Redimensionar la imagen
        img_tk = ImageTk.PhotoImage(img)
        miniatura_label.config(image=img_tk)
        miniatura_label.image = img_tk  # Mantener referencia para evitar que se borre la imagen

def salir():
    root.destroy()

# Crear ventana principal
root = Tk()
root.title("Konekt4 - Descargar Miniatura")
root.geometry("400x460")

# Etiqueta de instrucciones
instruccion_label = Label(root, text="Para descargar la miniatura, coloca el VIDEO_ID del enlace:")
instruccion_label_2 = Label(root, text="Ejemplo: https://www.youtube.com/watch?v=VIDEO_ID")
instruccion_label_2.pack(pady=12)
instruccion_label.pack(pady=10)

# Cuadro de entrada para el VIDEO_ID
video_id_entry = Entry(root, width=40)
video_id_entry.pack(pady=5)

# Botón para descargar la miniatura
descargar_btn = Button(root, text="Descargar Miniatura", command=descargar_miniatura)
descargar_btn.pack(pady=10)

# Etiqueta para mostrar resultados
resultado_label = Label(root, text="")
resultado_label.pack(pady=10)

# Crear etiqueta para la miniatura (inicialmente vacía)
miniatura_label = Label(root)
miniatura_label.pack(pady=10)

# Botón para salir
salir_btn = Button(root, text="Salir", command=salir)
salir_btn.pack(pady=5)

# Iniciar el bucle principal de la ventana
root.mainloop()