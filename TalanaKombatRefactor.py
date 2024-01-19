class Personaje:
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = energia


def ejecutar_movimiento(atacante, defensor, movimiento, golpe):
    key = atacante.nombre
    combination = movimiento+golpe
    
    if key in movimientos_dict:
        combinaciones_validas = [k for k in movimientos_dict[key] if k.endswith(combination)]
        print(combinaciones_validas)
        if combinaciones_validas:
            combinacion_valida = combinaciones_validas[0]
            danio = movimientos_dict[key][combinacion_valida]["energia"]
            mensaje_movimiento = movimientos_dict[key][combinacion_valida]["mensaje"]

            defensor.energia -= danio
            print(f"{atacante.nombre} ejecuta {mensaje_movimiento} y quita {danio} de energía a {defensor.nombre}")
        else:
            print(f"{atacante.nombre} realiza un movimiento y no causa daño a {defensor.nombre}")
    else:
        print(f"No existe información para la clave {key} en movimientos_dict")





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

movimientos_dict = {
    "Tonyn Stallone": {
        "DSDP": {"energia": 3, "mensaje": "Taladoken"},
        "SDK": {"energia": 2, "mensaje": "Remuyuken"},
        "P": {"energia": 1, "mensaje": "Puño"},
        "K": {"energia": 1, "mensaje": "Patada"}
    },
    "Arnaldor Shuatseneguer": {
        "SAK": {"energia": 3, "mensaje": "Remuyuken"},
        "ASAP": {"energia": 2, "mensaje": "Taladoken"},
        "P": {"energia": 1, "mensaje": "Puño"},
        "K": {"energia": 1, "mensaje": "Patada"}
    }
}

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