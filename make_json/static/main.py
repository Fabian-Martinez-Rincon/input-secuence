import pandas as pd

datos = pd.read_excel('./static/Tabla_de_pagos_acotada_V4_nueva.xlsx',sheet_name=1)
campos = ['SIMBOLO', 'SIMBOLO.1', 'SIMBOLO.2', 'SIMBOLO.3', 'SIMBOLO.4', 'R1', 'R2', 'R3', 'R4', 'R5']
datos_filtrados = datos.loc[:, campos]

datos_json = datos_filtrados.to_json(orient='records', indent=4)

with open('datos.json', 'w') as archivo:
    archivo.write(datos_json)

# Para saber cuántos elementos hay en el JSON, podemos hacer lo siguiente:

import json

with open("datos.json", "r") as archivo:
    data = json.load(archivo)

cantidad_elementos = len(data)
print("Cantidad de elementos en el JSON:", cantidad_elementos)