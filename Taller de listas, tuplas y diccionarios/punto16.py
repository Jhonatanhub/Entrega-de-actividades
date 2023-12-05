persona = {
    "nombre" : "Jhonatan",
    "edad" : 19
}

claves = list(persona.keys())
valores = list(persona.values())
pares = [(claves, valores) for claves, valores in persona.items()]
print(pares)