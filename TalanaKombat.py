class Personaje:
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = energia

def ejecutar_movimiento(atacante, defensor, movimiento, golpe):
    if atacante.nombre == "Tonyn Stallone":
        if movimiento.endswith("DSD") and golpe == "P":
            defensor.energia -= 3
            print(f"{atacante.nombre} ejecuta Taladoken y quita 3 de energía a {defensor.nombre}")
        elif movimiento.endswith("SD") and golpe == "K":
            defensor.energia -= 2
            print(f"{atacante.nombre} ejecuta Remuyuken y quita 2 de energía a {defensor.nombre}")
        elif golpe == "P" or golpe == "K":
            defensor.energia -= 1
            nombre_golpe = "Puño" if golpe == "P" else "Patada"
            print(f"{atacante.nombre} realiza un {nombre_golpe} y quita 1 de energía a {defensor.nombre}")
        else:
            print(f"{atacante.nombre} realiza un movimiento y no causa daño a {defensor.nombre}")

    elif atacante.nombre == "Arnaldor Shuatseneguer":
        
        if movimiento.endswith("SA") and golpe == "K":
            defensor.energia -= 3
            print(f"{atacante.nombre} ejecuta Remuyuken y quita 3 de energía a {defensor.nombre}")
        elif movimiento.endswith("ASA") and golpe == "P":
            defensor.energia -= 2
            print(f"{atacante.nombre} ejecuta Taladoken y quita 2 de energía a {defensor.nombre}")
        elif golpe == "P" or golpe == "K":
            defensor.energia -= 1
            nombre_golpe = "Puño" if golpe == "P" else "Patada"
            print(f"{atacante.nombre} realiza un {nombre_golpe} y quita 1 de energía a {defensor.nombre}")
        else:
            print(f"{atacante.nombre} realiza un movimiento y no causa daño a {defensor.nombre}")




def pelea(json_pelea):
    tonyn = Personaje("Tonyn Stallone", 6)
    arnaldor = Personaje("Arnaldor Shuatseneguer", 6)

    secuencia_p1 = json_pelea["player1"]["movimientos"]
    golpes_p1 = json_pelea["player1"]["golpes"]

    secuencia_p2 = json_pelea["player2"]["movimientos"]
    golpes_p2 = json_pelea["player2"]["golpes"]

    for movimiento_p1, golpe_p1, movimiento_p2, golpe_p2 in zip(secuencia_p1, golpes_p1, secuencia_p2, golpes_p2):
        ejecutar_movimiento(tonyn, arnaldor, movimiento_p1, golpe_p1)
        if arnaldor.energia <= 0:
            print(f"{arnaldor.nombre} Gana la pelea y aún le queda {arnaldor.energia + 1} de energía")
            break

        ejecutar_movimiento(arnaldor, tonyn, movimiento_p2, golpe_p2)
        if tonyn.energia <= 0:
            print(f"{tonyn.nombre} Gana la pelea y aún le queda {tonyn.energia + 1} de energía")
            break


json_pelea_1 = {
    "player1": {"movimientos": ["D", "DSD", "S", "DSD", "SD"], "golpes": ["K", "P", "", "K", "P"]},
    "player2": {"movimientos": ["SA", "SA", "SA", "ASA", "SA"], "golpes": ["K", "", "K", "P", "P"]}
}
json_pelea_2 = {
    "player1": {"movimientos": ["SDD", "DSD", "SA", "DSD"], "golpes": ["K", "P", "K", "P"]},
    "player2": {"movimientos": ["DSD", "WSAW", "ASA", "", "ASA", "SA"], "golpes": ["P", "K", "K", "K", "P","k"]}
}
json_pelea_3 = {
    "player1": {"movimientos":["DSD", "S"], "golpes": [ "P", ""]},
    "player2": {"movimientos":["", "ASA", "DA", "AAA", "", "SA"], "golpes": ["P", "", "P", "K", "K", "K"]}
    }

pelea(json_pelea_1)
print("*****************************************************************")
pelea(json_pelea_2)
print("*****************************************************************")
pelea(json_pelea_3)
