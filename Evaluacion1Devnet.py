# Definir el menú de productos y sus precios
menu = {
    "Espresso".lower(): 750,
    "Capucchino".lower(): 850,
    "Latte".lower(): 800,
    "Mocha".lower(): 830
}

# Precios de los agregados
precio_leche = 300
precio_chocolate = 200

# Solicitar al cliente que elija un tipo de café
print("Menú de Café:")
for producto, precio in menu.items():
    print(f"{producto}: ${precio}")

# Validar la selección del cliente
while True:
    seleccion = input("Por favor, elija un tipo de café: ")
    if seleccion in menu:
        break
    else:
        print("Selección inválida. Por favor, elija un tipo de café válido.")

# Solicitar al cliente que agregue leche y/o chocolate
agregar_leche = input("¿Desea agregar leche? (Sí/No): ").lower() == "si"
agregar_chocolate = input("¿Desea agregar chocolate? (Sí/No): ").lower() == "si"

# Calcular el total de la cuenta
subtotal = menu[seleccion]

if agregar_leche:
    subtotal += precio_leche

if agregar_chocolate:
    subtotal += precio_chocolate

# Imprimir el total de la cuenta
print(f"Total a pagar: ${subtotal}")
