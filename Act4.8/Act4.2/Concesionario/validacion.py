import json
from jsonschema import validate
# Definir el esquema
schema = {
"$schema": "http://json-schema.org/draft-07/schema#",
    "concesionario": {
      "type": "object",
      "properties": {
        "coche": {
          "type": "array",
           "minLength" : 1,
          "items": {
            "type": "object",
            "properties": {
              "codigo": {
                "type": "string",
                 "minLength" : 1
              },
              "marca": {
                "type": "string",
                 "minLength" : 1
              },
              "modelo": {
                "type": "string",
                 "minLength" : 1
              },
              "matricula": {
                "type": "string",
                 "minLength" : 1
              },
              "potencia": {
                "type": "string",
                 "minLength" : 1
              },
              "plazas": {
                "type": "integer",
                 "minLength" : 1
              },
              "puertas": {
                "type": "integer",
                 "minLength" : 1
              }
            },
            "required": ["codigo", "marca", "modelo", "matricula", "potencia", "plazas", "puertas"]
          }
        }
      },
      "required": ["coche"]
    }
  }

# Archivo JSON a validar
archivo_json = '''
{
   "concesionario": {
      "coche": [
        {
          "codigo": "001",
          "marca": "Toyota",
          "modelo": "Corolla",
          "matricula": "ABC123",
          "potencia": "120hp",
          "plazas": "5",
          "puertas": "4"
        },
        {
          "codigo": "002",
          "marca": "Honda",
          "modelo": "Civic",
          "matricula": "XYZ789",
          "potencia": "150hp",
          "plazas": "5",
          "puertas": "4"
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