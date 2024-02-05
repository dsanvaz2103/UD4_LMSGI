import json
from jsonschema import validate
# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
       "InformeEsquematico":{
        "titular":{
            "type": "string",
            "minLength": 1
        },
        "titulo":{
            "type": "string"
        },
        "descripcion":{
            "type": "string"
        },
        "Fecha_Informe":{
            "type": "string",
            "format": "date"
        },
        "Datos":{
            "region":{
                "Zona":{
                    "type": "string"
                },
                "Trimestre":{
                    "num":{
                        "type":"integer",
                        "minimum": 0
                    },
                    "LibroVendidos":{
                        "type":"string"
                    }
                }
            }
        },
        "required": ["titular", "titulo","Fecha_Informe"]
    }
}

# Archivo JSON a validar
archivo_json = '''
{
     "InformeEsquematico": {
        "titular": "Ediciones Aranda",
        "titulo": "Informe regional de ventas",
        "descripcion": "Informe de ventas para las regiones Norte,Centro y Sur",
        "Fecha_Informe": "30/12/2009",
        "Datos": {
            "Region": [
                {
                    "@Zona": "Norte",
                    "Trimestre": [
                        {
                            "@num": "1",
                            "LibroVendidos": "24000"
                        },
                        {
                            "@num": "2",
                            "LibroVendidos": "38600"
                        },
                        {
                            "@num": "3",
                            "LibroVendidos": "NO_INFO"
                        },
                        {
                            "@num": "4",
                            "LibroVendidos": "NO_INFO"
                        }
                    ]
                },
                {
                    "@Zona": "Centro",
                    "Trimestre": [
                        {
                            "@num": "1",
                            "LibroVendidos": "NO_INFO"
                        },
                        {
                            "@num": "2",
                            "LibroVendidos": "16080"
                        },
                        {
                            "@num": "3",
                            "LibroVendidos": "25000"
                        },
                        {
                            "@num": "4",
                            "LibroVendidos": "29000"
                        }
                    ]
                },
                {
                    "@Zona": "Sur",
                    "Trimestre": [
                        {
                            "@num": "1",
                            "LibroVendidos": "27000"
                        },
                        {
                            "@num": "2",
                            "LibroVendidos": "31400"
                        },
                        {
                            "@num": "3",
                            "LibroVendidos": "40100"
                        },
                        {
                            "@num": "4",
                            "LibroVendidos": "30000"
                        }
                    ]
                }
            ]
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