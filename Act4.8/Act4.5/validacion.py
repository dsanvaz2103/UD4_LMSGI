import json
from jsonschema import validate

# Definir el esquema
schema = {
     "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Alumnos",
    "type": "object",
    "properties": {
      "alumnos": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "NIF": {
              "type": "string",
              "pattern": "^\\d{8}[A-Z]$"
            },
            "Nombre": {
              "type": "string"
            },
            "Apellido": {
              "type": "string"
            },
            "FechaNacimiento": {
              "type": "string",
              "format": "date"
            },
            "Resultado": {
              "type": "string",
              "enum": ["apto", "No apto"]
            },
            "Observaciones": {
              "type": "string"
            },
            "IP": {
              "type": "string",
              "format": "ipv4"
            },
            "MAC": {
              "type": "string",
              "format": "mac"
            }
          },
          "required": ["NIF", "Nombre", "Apellido", "FechaNacimiento", "Resultado", "Observaciones"],
          "additionalProperties": false
        }
      }
    },
    "required": ["alumnos"],
    "additionalProperties": false
}

# Archivo JSON a validar
archivo_json = '''
{
  "alumnos": [
      {
        "NIF": "12345678A",
        "Nombre": "Juan",
        "Apellido": "Pérez",
        "FechaNacimiento": "1990-05-15",
        "Resultado": "apto",
        "Observaciones": "Excelente rendimiento",
        "IP": "192.168.1.1"
      },
      {
        "NIF": "98765432B",
        "Nombre": "Maria",
        "Apellido": "Gómez",
        "FechaNacimiento": "1992-08-20",
        "Resultado": "No apto",
        "Observaciones": "Se necesita mejorar en programación",
        "MAC": "00:1A:2B:3C:4D:5E"
      }
    ]
}
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.