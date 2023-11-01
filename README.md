# input-secuence
Ingresa un conjunto de datos de un Excel a una pestaña elegida por el usuario

---

### Crear un ejecutable

- En caso de no tener instalado
    ```
    pip install pyinstaller
    ```
- Creamos el ejecutable
    ```
    pyinstaller --onefile app.py
    ```

---

### Pasos

- Creamos el entorno virtual
    ```bash
    python -m venv env
    ```
- En caso de no tener permisos para windows, usamos el siguiente comando antes
    ```
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
- Activamos el entorno virtual
    ```bash
    env\Scripts\activate
    ```
- Instalamos las dependencias segun nuestra version de python
    ```bash
    pip install -r ./static/requirements_3.8.10.txt
    ```
    ```bash
    pip install -r ./static/requirements_3.12.0.txt
    ```
- Ejecutamos el programa
    ```bash
    python app.py
    ```
- Desactivamos el entorno virtual (opcional)
    ```bash
    deactivate
    ```

---

### Consola

![image](https://github.com/Fabian-Martinez-Rincon/input-secuence/assets/55964635/64c45cf4-2922-4f8e-85c5-c4cf90ecd4ff)