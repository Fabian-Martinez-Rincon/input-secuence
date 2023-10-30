import sys
from cx_Freeze import setup, Executable

# Definir los detalles de tu programa
nombre_programa = "mi_programa"
archivo_script = "mi_script.py"

# Configurar las dependencias
build_exe_options = {
    "packages": ["tkinter", "json", "pygetwindow", "pyautogui", "os"],
    "excludes": ["tkinter.tix", "tkinter.ttk"],
}

# Crear una instancia de Executable para tu script
ejecutable = Executable(
    script=archivo_script,
    base=None,  # No se necesita una base para programas simples
    targetName=nombre_programa,
)

# Configurar el setup
setup(
    name=nombre_programa,
    version="1.0",
    description="Descripción de tu programa",
    options={"build_exe": build_exe_options},
    executables=[ejecutable],
)
