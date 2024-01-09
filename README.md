# input-secuence
Ingresa un conjunto de datos de un Excel a una pestaña elegida por el usuario

#### Indice

- [Crear un ejecutable](#crear-un-ejecutable)
- [Primera Configuración de uso](#primera-configuración-de-uso)
- [Manual de Uso](#manual-de-uso)

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

### Primera Configuración de uso

- Creamos el entorno virtual
    ```bash
    python -m venv env
    ```
- En caso de no tener permisos para windows, usamos el siguiente comando antes (opcional)
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

### Manual de Uso

- Ingresamos los archivos excel que queremos procesar en la carpeta `base_excel`



https://github.com/Fabian-Martinez-Rincon/input-secuence/assets/55964635/0a2f08f5-4be1-4679-ba5c-8010bbeab6ae


