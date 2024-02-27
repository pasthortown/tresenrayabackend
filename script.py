juego = [[0, 1, 0],
         [0, 1, 0],
         [1, 10, 0]]

cuadrado_magico = [[2, 7, 6],
                   [9, 5, 1],
                   [4, 3, 8]]

visual = [["","",""],
          ["","",""],
          ["","",""]]

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def validar_condicion(matriz, valor):
    for indice, fila in enumerate(matriz):
        suma_fila = sum(fila)
        if suma_fila == valor:
            return "Fila", indice
    for indice_columna in range(len(matriz[0])):
        suma_columna = sum(matriz[fila][indice_columna] for fila in range(len(matriz)))
        if suma_columna == valor:
            return "Columna", indice_columna
    suma_diagonal_principal = sum(matriz[i][i] for i in range(len(matriz)))
    if suma_diagonal_principal == valor:
        return "Diagonal Principal", None
    suma_diagonal_secundaria = sum(matriz[i][len(matriz) - 1 - i] for i in range(len(matriz)))
    if suma_diagonal_secundaria == valor:
        return "Diagonal Secundaria", None    
    return None, None

def evaluar_ganar_perder(matriz):
    resultado = validar_condicion(matriz, 20)
    if resultado[0] is not None:
        return "Puedo ganar", resultado
    else:
        resultado = validar_condicion(matriz, 2)
        if resultado[0] is not None:
            return "Puedo perder", resultado
        else:
            return resultado

def revelar_cuadrado_magico(matriz_cuadrado_magico, matriz_juego):
    matriz_resultado = []
    for i in range(len(matriz_cuadrado_magico)):
        fila_resultado = []
        for j in range(len(matriz_cuadrado_magico[i])):
            if matriz_juego[i][j] == 0:
                fila_resultado.append(0)
            else:
                fila_resultado.append(matriz_cuadrado_magico[i][j])
        matriz_resultado.append(fila_resultado)
    return matriz_resultado

def suma_matriz(condicion, indice, matriz):
    if condicion == "Fila":
        suma = sum(matriz[indice])
    elif condicion == "Columna":
        suma = sum(fila[indice] for fila in matriz)
    elif condicion == "Diagonal Principal":
        suma = sum(matriz[i][i] for i in range(len(matriz)))
    elif condicion == "Diagonal Secundaria":
        n = len(matriz)
        suma = sum(matriz[i][n - i - 1] for i in range(n))
    return suma

def encontrar_coordenadas(numero, cuadrado_magico):
    for i in range(len(cuadrado_magico)):
        for j in range(len(cuadrado_magico[i])):
            if cuadrado_magico[i][j] == numero:
                return (i, j)

def jugar_coordenadas(matriz, numero, coordenadas):
    fila, columna = coordenadas
    matriz[fila][columna] = numero
    return matriz

def posiciones_disponibles(matriz):
    coordenadas_ceros = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                coordenadas_ceros.append((i, j))
    return coordenadas_ceros

def actualizar_tablero(tablero, player_1, player_2, juego):
    for i in range(len(juego)):
        for j in range(len(juego[i])):
            if juego[i][j] == 1:
                tablero[i][j] = player_1
            elif juego[i][j] == 10:
                tablero[i][j] = player_2
            elif juego[i][j] == 0:
                tablero[i][j] = ""
    return tablero