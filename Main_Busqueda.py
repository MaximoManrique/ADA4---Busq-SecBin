import tkinter as tk
from tkinter import messagebox

from Busqueda import linear_search, busqueda_binaria, busqueda_hash

def ejecutar_busqueda():
    try:
        entrada_lista = entry_lista.get()
        entrada_objetivo = entry_objetivo.get()

        if not entrada_lista or not entrada_objetivo:
            messagebox.showwarning("Error", "Faltan datos.")
            return

        lista_numeros = [int(x.strip()) for x in entrada_lista.split(",")]
        objetivo = int(entrada_objetivo)
        
        algoritmo = var_opcion.get()
        resultado = -1
        nota = ""

        if algoritmo == 1: 
         
            resultado = linear_search(lista_numeros, objetivo)
            
        elif algoritmo == 2:
           
            lista_numeros.sort()
            nota = "(Nota: Lista ordenada automáticamente)"
            resultado = busqueda_binaria(lista_numeros, objetivo)

        elif algoritmo == 3:
           
            nota = "(Nota: Usando Tabla Hash / Diccionario)"
            resultado = busqueda_hash(lista_numeros, objetivo)

        if resultado != -1:
            lbl_resultado.config(
                text=f" Encontrado en índice: {resultado}\n{nota}",
                fg="green"
            )
        else:
            lbl_resultado.config(
                text=f"❌ No se encuentra en la lista.\n{nota}",
                fg="red"
            )
            
        lbl_lista_actual.config(text=f"Lista usada: {lista_numeros}")

    except ValueError:
        messagebox.showerror("Error", "Revisa que los números estén bien escritos.")


ventana = tk.Tk()
ventana.title("Buscador: Lineal, Binario y Hash")
ventana.geometry("400x420") 
tk.Label(ventana, text="Lista (ej: 10, 20, 5, 40):").pack()
entry_lista = tk.Entry(ventana)
entry_lista.pack()

tk.Label(ventana, text="Número a buscar:").pack()
entry_objetivo = tk.Entry(ventana)
entry_objetivo.pack()

tk.Label(ventana, text="Selecciona Algoritmo:", font=("Arial", 10, "bold")).pack(pady=10)

var_opcion = tk.IntVar(value=1)

# Los 3 Radiobuttons
tk.Radiobutton(ventana, text="1. Búsqueda Lineal (Sencilla)", variable=var_opcion, value=1).pack(anchor="w", padx=80)
tk.Radiobutton(ventana, text="2. Búsqueda Binaria (Requiere Orden)", variable=var_opcion, value=2).pack(anchor="w", padx=80)
tk.Radiobutton(ventana, text="3. Búsqueda Hash (Más Rápida)", variable=var_opcion, value=3).pack(anchor="w", padx=80)

tk.Button(ventana, text="BUSCAR", command=ejecutar_busqueda, bg="#dddddd").pack(pady=15)

lbl_lista_actual = tk.Label(ventana, text="...", fg="gray")
lbl_lista_actual.pack()

lbl_resultado = tk.Label(ventana, text="Esperando...", font=("Arial", 12))
lbl_resultado.pack(pady=5)

ventana.mainloop()