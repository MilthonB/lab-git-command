import datetime

# Obtener nombre del usuario
nombre = input("¿Cómo te llamas? ")

# Obtener hora actual
hora_actual = datetime.datetime.now()
hora_formateada = hora_actual.strftime("%H:%M:%S")

# Mostrar mensaje
print(f"\n¡Hola {nombre}! 👋")
print(f"Son las {hora_formateada} en Mexico 🇲🇽")

# Preguntar qué quiere hacer
respuesta = input("\n¿Quieres saber la fecha actual? (s/n): ")

if respuesta.lower() == "s":
    fecha_actual = hora_actual.strftime("%d/%m/%Y")
    print(f"Hoy es {fecha_actual}")
else:
    print("¡Que tengas un buen día!")
