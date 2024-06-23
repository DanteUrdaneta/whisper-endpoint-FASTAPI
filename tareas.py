from apscheduler.schedulers.background import BackgroundScheduler
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import os

# Mapeo de días de la semana de español a inglés
dias_ingles = {
    "Lunes": "mon",
    "Martes": "tue",
    "Miércoles": "wed",
    "Jueves": "thu",
    "Viernes": "fri",
    "Sábado": "sat",
    "Domingo": "sun",
}


# Modificación en la función programar_tarea para usar la ruta actual del archivo .py
def programar_tarea():
    dia = dia_combobox.get()
    hora = int(hora_spinbox.get())
    minuto = int(minuto_spinbox.get())
    periodo = periodo_combobox.get()
    # Convertir hora de 12 a 24 horas
    if periodo == "PM" and hora < 12:
        hora += 12
    elif periodo == "AM" and hora == 12:
        hora = 0
    comando = comando_entry.get()
    # Obtener la ruta actual del script
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    comando_completo = f"cd {ruta_actual} && {comando}"
    print(
        f"Programando tarea para {dia} a las {hora}:{minuto:02} para ejecutar: {comando_completo}"
    )
    # Convertir el día de español a inglés
    dia_ingles = dias_ingles[dia]
    # Añadir la tarea al programador
    scheduler.add_job(
        lambda: subprocess.run(comando_completo, shell=True),
        "cron",
        day_of_week=dia_ingles,
        hour=hora,
        minute=minuto,
    )
    actualizar_lista_tareas()


def imprimir_tareas_programadas():
    trabajos = scheduler.get_jobs()
    if trabajos:
        print("Tareas programadas:")
        for trabajo in trabajos:
            print(
                f"ID: {trabajo.id}, Próxima ejecución: {trabajo.next_run_time}, Función: {trabajo.func.__name__}"
            )
    else:
        print("No hay tareas programadas.")


def actualizar_lista_tareas():
    tareas_listbox.delete(0, tk.END)  # Limpiar la lista antes de actualizar
    trabajos = scheduler.get_jobs()
    if trabajos:
        for trabajo in trabajos:
            tareas_listbox.insert(
                tk.END,
                f"ID: {trabajo.id}, Próxima ejecución: {trabajo.next_run_time}, Función: {trabajo.func.__name__}",
            )
    else:
        tareas_listbox.insert(tk.END, "No hay tareas programadas.")


def eliminar_tarea_seleccionada():
    seleccion = (
        tareas_listbox.curselection()
    )  # Obtener el índice del elemento seleccionado
    if not seleccion:
        messagebox.showinfo(
            "Eliminar Tarea", "Por favor, seleccione una tarea para eliminar."
        )
        return
    tarea_seleccionada = tareas_listbox.get(
        seleccion[0]
    )  # Obtener el texto del elemento seleccionado
    tarea_id = (
        tarea_seleccionada.split(",")[0].split(":")[1].strip()
    )  # Extraer el ID de la tarea
    scheduler.remove_job(tarea_id)  # Eliminar la tarea del programador
    actualizar_lista_tareas()  # Actualizar la lista de tareas


root = tk.Tk()
root.title("Programador de Tareas")


# Widgets para seleccionar la hora en formato 12 horas
hora_label = tk.Label(root, text="Hora (HH:MM):")
hora_label.pack()
hora_spinbox = tk.Spinbox(root, from_=1, to=12, format="%02.0f", width=5)
minuto_spinbox = tk.Spinbox(root, from_=0, to=59, format="%02.0f", width=5)
periodo_combobox = ttk.Combobox(root, values=["AM", "PM"], width=3)
hora_spinbox.pack()
minuto_spinbox.pack()
periodo_combobox.pack()


# Widgets para seleccionar el día
dia_label = tk.Label(root, text="Día de la semana:")
dia_label.pack()
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
dia_combobox = ttk.Combobox(root, values=dias)
dia_combobox.pack()

# Widget para ingresar el comando
comando_label = tk.Label(root, text="Comando:")
comando_label.pack()
comando_entry = tk.Entry(root)
comando_entry.pack()

# Botón para programar la tarea
programar_button = tk.Button(root, text="Programar Tarea", command=programar_tarea)
programar_button.pack()

# Listbox y botón para ver tareas programadas
tareas_listbox_label = tk.Label(root, text="Tareas Programadas:")
tareas_listbox_label.pack()
tareas_listbox = tk.Listbox(root, width=50, height=10)
tareas_listbox.pack()
ver_tareas_button = tk.Button(
    root, text="Ver Tareas Programadas", command=actualizar_lista_tareas
)
ver_tareas_button.pack()

# Botón para eliminar la tarea seleccionada
eliminar_tarea_button = tk.Button(
    root, text="Eliminar Tarea Seleccionada", command=eliminar_tarea_seleccionada
)
eliminar_tarea_button.pack()

# Iniciar el programador de tareas
scheduler = BackgroundScheduler()
scheduler.start()

root.mainloop()
