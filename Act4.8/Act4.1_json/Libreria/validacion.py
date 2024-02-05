import json
from jsonschema import validate
# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
   "biblioteca":{
        "libro":{
            "autores":{
                "autor":{
                    "apellido1":{
                        "type":"string"
                    },"apellido2":{
                        "type":"string"
                    },"apellido3":{
                        "type":"string"
                    },"nombre":{
                        "type":"string"
                    }
                }
            },"titulo":{
                "type":"string"
            },"editorial":{
                "type":"string"
            },"fechaPublicacion":{
                "type":"string","format":"date"
            },"ISBN":{
                "type":"string"
            }
        }, "required": ["nombre", "apellido1","apellido2","titulo","editorial","fechaPublicacion","ISBN"]
    }
}

# Archivo JSON a validar
archivo_json = '''
{
  "biblioteca": {
       "libro": [
         {
           "autores": {
             "autor": [
               {
                 "apellido1": "García",
                 "apellido2": "Márquez",
                 "apellido3": "Ningun apellido",
                 "nombre": "Gabriel"
               }
             ]
           },
           "titulo": "Cien años de soledad",
           "editorial": "editorial Sudamericana",
           "fechaPublicacion": "mayo de 1967",
           "ISBN": "9789510445365"
         },
         {
           "autores": {
             "autor": [
               {
                 "apellido1": "Ronald",
                 "apellido2": "Reuel",
                 "apellido3": "Tolkien",
                 "nombre": "John"
               }
             ]
           },
           "titulo": "El señor de los anillos",
           "editorial": "Editorial Tirant Lo Blanch",
           "fechaPublicacion": "29 de julio de 1954",
           "ISBN": "9788845292613"
         },
         {
           "autores": {
             "autor": [
               {
                 "apellido1": "Collins",
                 "apellido2": "Ningun apellido",
                 "apellido3": "Ningun apellido",
                 "nombre": "Suzanne"
               }
             ]
           },
           "titulo": "Los juegos del hambre",
           "editorial": "Editorial Molino",
           "fechaPublicacion": "14 de septiembre de 2008",
           "ISBN": "9780545091022"
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