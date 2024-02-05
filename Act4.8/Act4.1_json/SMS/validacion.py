import json
from jsonschema import validate
# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
       "BDsms":{
        "sms":{
            "telefono":{
                "type":"integer"
            },"fecha":{
                "type":"string","format":"date"
            },"hora":{
                "type":"string"
            },"mensaje":{
                "type":"string"
            }
        }
    }
}

# Archivo JSON a validar
archivo_json = '''
{
     "BDsms": {
       "sms": [
         {
           "telefono": "9789510445365",
           "fecha": "1/7/2011",
           "hora": "22:30",
           "mensaje": "Juego1:Tetris"
         },
         {
           "telefono": "7378287832832",
           "fecha": "2/4/2012",
           "hora": "09:23",
           "mensaje": "Juego2:Ark"
         },
         {
           "telefono": "2848080686743",
           "fecha": "3/9/2015",
           "hora": "16:46",
           "mensaje": "Juego3:Krunker"
         }
       ]
    }
}
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.