import json
from jsonschema import validate

# Definir el esquema
schema = {
     "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "clientes": {
        "type": "object",
        "properties": {
          "sede": {
            "type": "object",
            "properties": {
              "dir1": { "type": "string" },
              "dir2": { "type": "string" },
              "empleado": { "type": "string" },
              "fecha": { "type": "string", "format": "date" }
            },
            "required": ["dir1", "dir2", "empleado", "fecha"]
          },
          "cliente": {
            "type": "object",
            "properties": {
              "descripcionCliente": { "type": "string" },
              "numViviendas": { "type": "integer" },
              "costeVivienda": { "type": "number" },
              "resumenViviendas": { "type": "string" },
              "plazoHacienda": { "type": "string", "format": "date" }
            },
            "required": ["descripcionCliente", "numViviendas", "costeVivienda", "resumenViviendas", "plazoHacienda"]
          }
        },
        "required": ["sede", "cliente"]
      }
    },
    "required": ["clientes"]
}

# Archivo JSON a validar
archivo_json = '''
{
 "clientes": {
      "sede": {
        "dir1": "Calle Principal,  123",
        "dir2": "Piso  4",
        "empleado": "Juan Pérez",
        "fecha": "22-01-2024"
      },
      "cliente": {
        "descripcionCliente": "Inmobiliaria XYZ",
        "numViviendas":  30,
        "costeVivienda":  300000,
        "resumenViviendas": "Moderno edificio de apartamentos con excelentes comodidades.",
        "plazoHacienda": "31-01-2025"
      }
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