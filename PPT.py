def juega(jugador):
    while True:
        eleccion = input(f"{jugador}, selecciona:\n1 (Piedra)\n2 (Papel)\n3 (Tijera)\n")
        if eleccion == '1' or eleccion == '2' or eleccion == '3':
            return int(eleccion)
        print("Escoge nuevamente")

def es_ganador(eleccion_j1, eleccion_j2, jugador1, jugador2):
    if eleccion_j1 == eleccion_j2:
        return "Empate"
    if (eleccion_j1 == 1 and eleccion_j2 == 3) or (eleccion_j1 == 2 and eleccion_j2 == 1) or (eleccion_j1 == 3 and eleccion_j2 == 2):
        return f"{jugador1} gana"
    return f"{jugador2} gana"

def inicia():
    print("PPT - PIEDRA PAPEL TIJERA")

    jugador1 = "JUAN"
    jugador2 = "PEDRO"

    eleccion_j1 = juega(jugador1)
    eleccion_j2 = juega(jugador2)

    print(f"{jugador1} eligió {eleccion_j1}")
    print(f"{jugador2} eligió {eleccion_j2}")

    resultado = es_ganador(eleccion_j1, eleccion_j2, jugador1, jugador2)
    print(f"Resultado: {resultado}")

inicia()