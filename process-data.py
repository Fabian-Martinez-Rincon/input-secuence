import pandas as pd
import json

datos = pd.read_excel('./static/excels/example.xlsx',sheet_name=1)
campos = ['SIMBOLO', 'SIMBOLO.1', 'SIMBOLO.2', 'SIMBOLO.3', 'SIMBOLO.4', 'R1', 'R2', 'R3', 'R4', 'R5']

print('Cabeceras del excel:')
print(datos.columns)

datos_filtrados = datos.loc[:, campos]

datos_json = datos_filtrados.to_json(orient='records', indent=4)

with open('./static/json/datos.json', 'w') as archivo:
    archivo.write(datos_json)

# Para saber cuántos elementos hay en el JSON:

with open("./static/json/datos.json", "r") as archivo:
    data = json.load(archivo)

cantidad_elementos = len(data)
print("Cantidad de elementos en el JSON:", cantidad_elementos)