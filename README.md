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

### Filtrar los datos

```python
import pandas as pd

datos = pd.read_excel('./static/Tabla de pagos_acotada_v4.xlsx',sheet_name=1)
campos = ['SIMBOLO', 'SIMBOLO.1', 'SIMBOLO.2', 'SIMBOLO.3', 'SIMBOLO.4', 'R1', 'R2', 'R3', 'R4', 'R5']
datos_filtrados = datos.loc[:, campos]

datos_json = datos_filtrados.to_json(orient='records', indent=4)

with open('datos.json', 'w') as archivo:
    archivo.write(datos_json)
```

### Saber la cantidad de elementos del json

```python
# Para saber cuántos elementos hay en el JSON, podemos hacer lo siguiente:

import json

with open("datos.json", "r") as archivo:
    data = json.load(archivo)

cantidad_elementos = len(data)
print("Cantidad de elementos en el JSON:", cantidad_elementos)
```