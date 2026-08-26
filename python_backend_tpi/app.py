#python ./python_backend_tpi/app.py
# productos = [
#     {"nombre": "Laptop", "precio": 1200, "stock": 15},
#     {"nombre": "Mouse", "precio": 25, "stock": 5},
#     {"nombre": "Teclado", "precio": 75, "stock": 25},
#     {"nombre": "Monitor", "precio": 300, "stock": 8},
# ]

# productos_bajo_stock = []  # se crea la lista para almacenar los productos con bajo stock

# for producto in productos: # se crea una variable "producto" que recorre la lista de productos
#     print(f"Producto: {producto['nombre']}, Precio: ${producto['precio']}") #se imprime el nombre y precio de cada producto
#     if producto['stock'] < 10: # Condicional por si hay menos de 10 unidades
#         productos_bajo_stock.append(producto) # se agrega el producto a la lista de bajo stock

# print("\nProductos con bajo stock:") # se imprime una nueva linea con un mensaje
# print(productos_bajo_stock) #se imprime la lista de productos con bajo stock

# ------------------------------------------------------------------------------------------------------------

# def calcular_promedio_precio(lista): # se define la función que recibe una lista de productos
#   if not lista: # si la lista está vacía, se retorna 0
#     return 0 # retorna 0
#   total_precio = sum(p['precio'] for p in lista) # se calcula el total de los precios de los productos en la lista
#   return total_precio / len(lista) # se retorna el promedio de los precios dividiendo el total de precios entre la cantidad de productos en la lista

# precio_promedio = calcular_promedio_precio(productos) # se llama a la función calcular_promedio_precio con la lista de productos y se almacena el resultado en la variable precio_promedio
# print(f"\nEl precio promedio de los productos es: ${precio_promedio:.2f}") # se imprime el precio promedio de los productos con dos decimales


# import csv
# productos_desde_csv = []

# with open('datos.csv', mode='r', encoding='utf-8') as archivo_csv:
#     lector_diccionario = csv.DictReader(archivo_csv)
#     for fila in lector_diccionario:
#         fila['id'] = int(fila['id'])
#         fila['precio'] = int(fila['precio'])
#         fila['stock'] = int(fila['stock'])

#         productos_desde_csv.append(fila)
                            
# print("Lista de productos desde el archvio CSV: ")
# print(productos_desde_csv)

# ------------------------------------------------------------------------------------------------------------
