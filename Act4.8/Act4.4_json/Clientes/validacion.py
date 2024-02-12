import json
from jsonschema import validate

# Definir el esquema
schema = {
     "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "clientes": {
        "type":"object","minLength" : 1,
        "properties": {
          "sede": {
            "type":"object","minLength" : 1,
            "properties": {
              "dir1": { "type": "string" ,"minLength" : 1},
              "dir2": { "type": "string" ,"minLength" : 1},
              "empleado": { "type": "string" ,"minLength" : 1},
              "fecha": { "type": "string", "format": "date","minLength" : 1 }
            },
            "required": ["dir1", "dir2", "empleado", "fecha"]
          },
          "cliente": {
            "type":"object","minLength" : 1,
            "properties": {
              "descripcionCliente": { "type": "string" ,"minLength" : 1},
              "numViviendas": { "type": "integer","minLength" : 1 },
              "costeVivienda": { "type": "number","minLength" : 1 },
              "resumenViviendas": { "type": "string","minLength" : 1 },
              "plazoHacienda": { "type": "string", "format": "date","minLength" : 1 }
            },
            "required": ["descripcionCliente", "numViviendas", "costeVivienda", "resumenViviendas", "plazoHacienda"]
          }
        },"required": ["sede", "clientes"]
      }
    },"required": ["clientes"]
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