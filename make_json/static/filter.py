import pandas as pd
import json

datos = pd.read_json('datos.json')

campos = ['SIMBOLO', 'SIMBOLO.1', 'SIMBOLO.2', 'SIMBOLO.3', 'SIMBOLO.4', 'PAGADO EN BASE A UNA APUESTA DE 25', 'APUESTA DE 1', 'R1', 'R2', 'R3', 'R4', 'R5']
datos_filtrados = datos.loc[:, campos]

datos_json = datos_filtrados.to_json(orient='records', indent=4)

with open('datos_filtrados.json', 'w') as archivo:
    archivo.write(datos_json)