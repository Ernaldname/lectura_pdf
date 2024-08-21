import pdfplumber
from tkinter import Tk, filedialog

# Función para seleccionar un archivo PDF
def seleccionar_archivo_pdf():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter
    archivo_pdf = filedialog.askopenfilename(
        title="Selecciona un archivo PDF",
        filetypes=[("Archivos PDF", "*.pdf")]
    )
    return archivo_pdf

# Ruta del archivo PDF
archivo_pdf = seleccionar_archivo_pdf()

if archivo_pdf:
    # Abrir el archivo PDF con pdfplumber
    with pdfplumber.open(archivo_pdf) as pdf:
        texto_completo = ""
        for pagina in pdf.pages:
            texto_completo += pagina.extract_text()
        
        # Mostrar el texto extraído
        print(texto_completo)
else:
    print("No se seleccionó ningún archivo.")
 