# Calculadora

nombre = input("Ingresa nombre del producto: ")
precio = float("Ingrese el precio: ")
cantidad = int("Ingrese cantidad: ")

while True: 
    try:
        precio = float(input("Ingrese el precio el producto: "))
        if precio < 0: 
            print("Error: el precio no puede ser negativo")
        else: 
            break
    except:
        print("Error: ingrese un numero entero valido")
        
        #validar cantidad
    
    while True:
        try: 
            cantidad = int(input("ingrese la cantidad del producto: "))
        
            if cantidad < 0: 
                print("Error la cantidad no puede ser negativa: ")
            else:
                break
        except:
            print("Error: Ingrse un numero entero valido")
#calcular costo total
Costo_total = precio * cantidad

#mostrar resultados
print("\n--- RESULTADO ---")
print(f"producto: {nombre} | precio: {precio} | cantidad {cantidad} | total: {Costo_total}")