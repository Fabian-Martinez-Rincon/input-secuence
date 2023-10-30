# input-secuence
Ingresa un conjunto de datos de un Excel a una pestaña elegida por el usuario

### Dependencias

```bash
pip install -r requirements.txt
```

### Primera Parte

Antes de usar el programa, tenemos que tener un json con la siguiente estructura:

```json
{
    "file": "path/to/file.xlsx",
    "sheet": "sheet_name",
    "start": "A1",
    "end": "A10"
}
```

### Entorno Virtual

Creamos el entorno virtual

```
python -m venv venv
```

Tenemos que ejecutar el entorno virtual

**Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\Activate
```

En caso de no tener permisos para windos, usamos el siguiente comando antes

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```


**Una vez que estamos en el entorno virtual ejecutamos el siguiente comando**

```bash
pip install altgraph==0.17.4 certifi==2023.7.22 charset-normalizer==3.3.1 docopt==0.6.2 EasyProcess==1.1 entrypoint2==1.1 et-xmlfile==1.1.0 idna==3.4 MouseInfo==0.1.3 mss==9.0.1 numpy==1.26.1 openpyxl==3.1.2 packaging==23.2 pandas==2.1.1 pefile==2023.2.7 pipreqs==0.4.13 PyAutoGUI==0.9.54 PyGetWindow==0.0.9 pyinstaller==6.1.0 pyinstaller-hooks-contrib==2023.10 PyMsgBox==1.0.9 pyperclip==1.8.2 PyRect==0.2.0 pyscreenshot==3.1 PyScreeze==0.1.29 python-dateutil==2.8.2 pytweening==1.0.7 pytz==2023.3.post1 pywin32-ctypes==0.2.2 requests==2.31.0 setuptools==68.2.2 six==1.16.0 tzdata==2023.3 urllib3==2.0.7 yarg==0.1.9
```

o tambien

```bash
pip install -r requirements.txt
```


Despues para ejecutar

```bash
python app.py
```