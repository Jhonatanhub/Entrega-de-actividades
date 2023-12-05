personas = {
    "Jhonatan": 19,
    "Jheison": 17,
    "Jakeline": 21
}

mayores = [nombre for nombre, edad in personas.items() if edad >= 18]
print(mayores)