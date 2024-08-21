import pdfplumber
import tkinter as tk
from tkinter import filedialog, messagebox

def seleccionar_pdf():
    # Abre el cuadro de diálogo para seleccionar un archivo PDF
    archivo_pdf = filedialog.askopenfilename(
        title="Selecciona un archivo PDF", 
        filetypes=[("Archivos PDF", "*.pdf")]
    )
    
    if archivo_pdf:
        guardar_texto(archivo_pdf)

def guardar_texto(ruta_pdf):
    # Abre el archivo PDF y extrae el texto
    try:
        with pdfplumber.open(ruta_pdf) as pdf:
            # Abre un archivo de texto para guardar el contenido extraído
            archivo_texto = filedialog.asksaveasfilename(
                defaultextension=".txt", 
                filetypes=[("Archivo de Texto", "*.txt")],
                title="Guardar archivo de texto"
            )
            if archivo_texto:
                with open(archivo_texto, "w", encoding="utf-8") as archivo:
                    # Recorre todas las páginas del PDF
                    for pagina in pdf.pages:
                        # Extrae el texto de cada página
                        texto = pagina.extract_text()
                        if texto:  # Verifica si hay texto en la página
                            archivo.write(texto + "\n")
                messagebox.showinfo("Éxito", "Texto extraído y guardado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

# Configuración de la interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Extractor de Texto de PDF")

# Etiqueta de bienvenida
label = tk.Label(root, text="Selecciona un archivo PDF para extraer su texto:")
label.pack(pady=10)

# Botón para seleccionar el archivo PDF
boton_seleccionar = tk.Button(root, text="Seleccionar PDF", command=seleccionar_pdf)
boton_seleccionar.pack(pady=20)

# Inicia el bucle principal de la ventana
root.mainloop()
