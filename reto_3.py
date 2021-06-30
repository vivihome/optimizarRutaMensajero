def optimizar_ruta (distancias: dict, rutas: list):
    grafo_valido = validar_puntos(distancias)
    optimizacion = list()
    if grafo_valido:
        for ruta in rutas:
            mejoroDistancia = False
            #distanciaTotal, gasolinaTotal = calcular_distancia(distancias, ruta)
            rutaIteracion = ruta.copy()
            posiblesParejas:list = posibles_parejas(rutaIteracion)
            i = 0
            while i < 1:
                for pareja in posiblesParejas:
                    rutaIntercambio = ejecutar_cambio(pareja, ruta)
                    distanciaIntercambio, gasolinaIntercambio = calcular_distancia(distancias, rutaIntercambio)
                    distanciaIteracion, gasolinaIteracion = calcular_distancia(distancias, rutaIteracion)
                    if distanciaIntercambio < distanciaIteracion and gasolinaIntercambio < gasolinaIteracion :                
                        mejoroDistancia = True
                        rutaIteracion = rutaIntercambio
                        distancia = distanciaIntercambio
                        gasolina = gasolinaIntercambio
                if mejoroDistancia == True:
                    mejoroDistancia = False
                    rutaActual= rutaIteracion.copy()
                    rutaFinal = escribir_ruta(rutaActual)
                    i = 0
                else:
                    salida = {'ruta': rutaFinal, 'kilometraje': distancia, 'gasolina': gasolina}
                    optimizacion.append(salida)
                    i = 1
        return optimizacion
    else:
        return "La distancia o el consumo de combustible no pueden ser menores a cero o deben ser cero cuando se identifica un mismo punto."

def validar_puntos(distancias: dict):
    validas = True
    for keys in distancias.keys():
        key1,key2 = keys
        if key1 == key2:
            if (distancias[keys][0] != 0 and distancias[keys][1] != 0):
                validas = False
                break
        elif distancias[keys][0] < 0 or distancias[keys][1] < 0:
            validas = False
            break
    return validas

def calcular_distancia(distancias: dict, ruta: list):
    sumaDistancia, sumaGasolina, j = 0 ,0, 0
    for i in range(0, len(ruta)-1):
        j += 1
        nodo = (ruta[i],ruta[j])
        sumaDistancia += distancias[nodo][0]
        sumaGasolina += distancias[nodo][1]
    return (sumaDistancia, sumaGasolina)

def posibles_parejas (ruta:list):
    numeroNodos = len(ruta) -1
    i = 0
    j = 0
    arcosComparacion = []
    for i in range( 1 , numeroNodos-1):
        for j in range( i+1 , numeroNodos):
            arco = ( ruta[i], ruta[j] )
            arcosComparacion += [arco]
    return arcosComparacion

def ejecutar_cambio (arco: tuple, ruta_actual:list):
    nuevaRuta = ruta_actual.copy()
    for nodoX, nodoY in [arco]:
        indices = [nuevaRuta.index(nodoX), nuevaRuta.index(nodoY)]
        for indiceX, indiceY in [indices]:
            nuevaRuta[indiceX]= nodoY
            nuevaRuta[indiceY]= nodoX
    return nuevaRuta

def escribir_ruta (ruta_actual:list):
    rutaActual = ruta_actual.copy()
    rutaFinal = ''
    for nodo in rutaActual:
        rutaFinal += str(nodo) + '-' 
    cadena = len(rutaFinal) - 1
    return rutaFinal[0:cadena]


rutas = [['H', 'A', 'B', 'C', 'D', 'E','F'],['A', 'H', 'D', 'F', 'B', 'E','C']]

distancias={
('H', 'H'): (0, 0), ('H', 'A'): (21, 34), ('H', 'B'): (57, 56),('H', 'C'): (58, 78), ('H', 'D'):(195, 90), 
('H', 'E'): (245, 123), ('H', 'F'): (241, 134),('A', 'H'): (127, 89), ('A', 'A'):(0, 0), ('A', 'B'): (231, 132),
('A', 'C'): (113, 76), ('A', 'D'): (254, 200), ('A', 'E'): (179, 102), ('A', 'F'): (41, 8),('B', 'H'): (153, 56), 
('B', 'A'): (252, 102), ('B', 'B'): (0, 0),('B', 'C'): (56, 21), ('B', 'D'): (126, 76), ('B', 'E'): (160, 56), 
('B', 'F'): (269, 125),('C', 'H'): (196, 87), ('C', 'A'):(128, 56), ('C', 'B'): (80, 34),('C', 'C'): (0, 0), 
('C', 'D'): (136, 98), ('C', 'E'): (37, 9),('C', 'F'): (180, 98),('D', 'H'): (30,90), ('D', 'A'):(40, 97), 
('D', 'B'): (256, 102), ('D', 'C'): (121, 95),('D', 'D'): (0, 0), ('D', 'E'):(194, 43), ('D', 'F'): (109, 26),
('E', 'H'): (33, 10), ('E', 'A'): (144, 87), ('E', 'B'): (179, 54), ('E', 'C'): (114, 132),('E', 'D'): (237, 192), 
('E', 'E'): (0, 0), ('E', 'F'): (119, 78),('F', 'H'): (267, 87), ('F', 'A'):(61, 23), ('F', 'B'): (79, 80),
('F', 'C'): (39, 10), ('F', 'D'):(135, 76), ('F', 'E'): (55, 10),('F', 'F'): (0,0)
}

print(optimizar_ruta(distancias,rutas))