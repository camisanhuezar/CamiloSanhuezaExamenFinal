#FUNCIONES
#Funcion opc1 (OK)
def stock_marca(marcaConsultada, diccionario_stock):

    for codigoStock, listaAtributos in diccionario_stock.items():
        if codigoStock == marcaConsultada:
            print(f"El stock es: {listaAtributos[1]}")

#Función opc2 (in)
def búsqueda_precio(p_min, p_max, diccionario_productos, diccionario_stock):

    listaPrecios = []

    for codigoStock, listaAtributosStock in diccionario_stock:
        if (listaAtributosStock[0] >= p_min) and (listaAtributosStock[0] <= p_max):

            for codigoProductos, listaAtributosProductos in diccionario_productos.items():

                if codigoProductos == codigoStock:
                    listaPrecios.append(f"{listaAtributosProductos[0]} -- {codigoProductos}")
                    break

        else:
            listaPrecios.sort()
            for precios in listaPrecios:
                print(precios)


#Función opc3 (in)
def buscar_modelo(modelo, diccionario_stock):

    for modeloBuscado in diccionario_stock.keys():

        if modelo == modeloBuscado: 
            return True
        
    return False

def actualizar_precio(modelo, precioNuevo, diccionario_stock):
    
    if buscar_modelo(modelo, diccionario_stock) == True:

        listaAtributosStock = diccionario_stock[modelo]
        
        listaAtributosStock[0] = precioNuevo

        return True

    else:
        return False


#DICCIONARIOS
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
    'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}


#MENU PRINCIPAL
while True:
    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")
    print("************************")
    print("")

    try:
        
        opcionMenu = int(input("Ingrese una de las opciones del menú: "))
        print("")
        

        if opcionMenu == 1:
            marcaConsultada = input("Ingrese marca a consultar: ")
            stock_marca(marcaConsultada, stock)

        elif opcionMenu == 2:
            while True:
                try:
                    p_min = int(input("Ingrese el precio mínimo del rango: "))
                    p_max = int(input("Ingrese el precio máximo del rango: "))

                    if p_min < 0 or p_max < p_min:
                        print("Error, ingrese valores correctos.")
                    else:
                        búsqueda_precio(p_min, p_max, productos, stock)
                        break
                except ValueError:
                    print("Debe ingresar valores enteros!!")

                  



        elif opcionMenu == 3:
            while True:
                modeloBuscado = input("Ingrese el modelo del notebook a actualizar: ")

                while True:
                    try:
                        precioNuevo = int(input("Ingrese el precio nuevo: "))
                        if precioNuevo <= 0:
                            print("Debe ingresar valores enteros positivos")
                        else:
                            break
                    except ValueError:
                        print("Debe ingresar valores enteros positivos")

                actualizar_precio(modeloBuscado, precioNuevo, stock)

                if precioNuevo == True:
                    print("Precio actualizado!!")
                else:
                    print("El modelo no se encuentra o no existe")

                otroPrecio = input("¿Desea actualizar otro precio (s/n)?").lower()

                if otroPrecio == "si":
                    continue
                else:
                    break

        elif opcionMenu == 4:
            print("Programa finalizado.")
            print("")
            break
        
        elif opcionMenu <= 0 or opcionMenu >= 5:
            print("Debe seleccionar una opción válida!!")


    except ValueError:
        print("Debe seleccionar una opción válida!!")



