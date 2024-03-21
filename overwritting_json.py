import json

# Datos existentes
data = [

]

# Nueva información
nueva_informacion = {
    "image": "https://www.ejemplo.com/imagen-futbol.jpg"
}

if len(data)==0:
   print("Esta vacio")
   data.append(nueva_informacion)

else:
   data[-1].update(nueva_informacion)

# Imprimir resultado
print(json.dumps(data, indent=4))
