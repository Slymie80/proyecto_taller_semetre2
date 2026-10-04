
import matplotlib.pyplot as plt



# COLORES DE CONSOLA
# =========================

ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
RESET = "\033[0m"


# DATOS INICIALES
# =========================
flota = {
    "D01": {
        "tipo": "Drone",
        "capacidad_maxima": 5,
        "bateria": 100,
        "estado": "Disponible",
        "ubicacion_actual": "Base"
    },

    "D02": {
        "tipo": "Drone",
        "capacidad_maxima": 5,
        "bateria": 85,
        "estado": "Disponible",
        "ubicacion_actual": "Base"
    },

    "M01": {
        "tipo": "Moto",
        "capacidad_maxima": 25,
        "bateria": 100,
        "estado": "Disponible",
        "ubicacion_actual": "Base"
    },

    "M02": {
        "tipo": "Moto",
        "capacidad_maxima": 25,
        "bateria": 70,
        "estado": "Disponible",
        "ubicacion_actual": "Base"
    },

    "C01": {
        "tipo": "Camion",
        "capacidad_maxima": 150,
        "bateria": 100,
        "estado": "Disponible",
        "ubicacion_actual": "Base"
    },

    "C02": {
        "tipo": "Camion",
        "capacidad_maxima": 150,
        "bateria": 90,
        "estado": "Disponible",
        "ubicacion_actual": "Base"
    }
}

pedidos = [
    {
        "id": 1,
        "destino": "La Fortuna",
        "peso": 3,
        "prioridad": 5,
        "estado": "Pendiente",
        "vehiculo": None
    },

    {
        "id": 2,
        "destino": "Ciudad Quesada",
        "peso": 15,
        "prioridad": 3,
        "estado": "Pendiente",
        "vehiculo": None
    },

    {
        "id": 3,
        "destino": "Florencia",
        "peso": 4,
        "prioridad": 4,
        "estado": "Pendiente",
        "vehiculo": None
    },

    {
        "id": 4,
        "destino": "Aguas Zarcas",
        "peso": 20,
        "prioridad": 3,
        "estado": "Pendiente",
        "vehiculo": None
    },

    {
        "id": 5,
        "destino": "Pital",
        "peso": 70,
        "prioridad": 2,
        "estado": "Pendiente",
        "vehiculo": None
    },

    {
        "id": 6,
        "destino": "Venecia",
        "peso": 5,
        "prioridad": 5,
        "estado": "Pendiente",
        "vehiculo": None
    },

    {
        "id": 7,
        "destino": "Los Chiles",
        "peso": 100,
        "prioridad": 1,
        "estado": "Pendiente",
        "vehiculo": None
    },

    {
        "id": 8,
        "destino": "Muelle",
        "peso": 18,
        "prioridad": 4,
        "estado": "Pendiente",
        "vehiculo": None
    }
]

restricciones = {
    "Lluvia": "Drone",
    "Tormenta": "Moto",
    "Calor extremo": None
}

clima_actual = "Normal"

# =========================
# DATOS HISTÓRICOS
# =========================

consumo_acumulado = {
    "Drone": 0,
    "Moto": 0,
    "Camion": 0
}

estadisticas_vehiculos = {
    "D01": {
        "energia_consumida": 0,
        "peso_transportado": 0
    },

    "D02": {
        "energia_consumida": 0,
        "peso_transportado": 0
    },

    "M01": {
        "energia_consumida": 0,
        "peso_transportado": 0
    },

    "M02": {
        "energia_consumida": 0,
        "peso_transportado": 0
    },

    "C01": {
        "energia_consumida": 0,
        "peso_transportado": 0
    },

    "C02": {
        "energia_consumida": 0,
        "peso_transportado": 0
    }
}


#funciones validacion

def vehiculo_disponible (id_vehiculo):
    if id_vehiculo in flota and flota[id_vehiculo]["estado"] == "Disponible":
        return True
    return False

# =========================
# FUNCIONES AUXILIARES
# =========================

def buscar_pedido(id_pedido):
    pass


def buscar_vehiculo(id_vehiculo):
    pass


def buscar_pedido_por_vehiculo(id_vehiculo):
    for vehiculo in flota:
        if vehiculo == id_vehiculo:
            for pedido in pedidos:
                if pedido["vehiculo"] == id_vehiculo:
                    return pedido
    return None


# =========================
# OPCIÓN 1
# REGISTRAR / VISUALIZAR PEDIDOS
# =========================

def registrar_visualizar_pedidos():
    pass


# =========================
# OPCIÓN 2
# ASIGNAR ENVÍO
# =========================


def asignar_envio(id_pedido, id_vehiculo):
        if vehiculo_disponible(id_vehiculo):
            for pedido in pedidos:
                if pedido["id"] == id_pedido:
                    pedido["vehiculo"] = id_vehiculo
                    pedido["estado"] = "Enviado"
                    flota[id_vehiculo]["estado"] = "Enviado"
                    print(f"{VERDE}El pedido {id_pedido} ha sido asignado al vehículo {id_vehiculo}.{RESET}")
                    return
        else:
            print(f"{ROJO}El vehículo {id_vehiculo} no está disponible o no existe.{RESET}")                                


# =========================
# OPCIÓN 3
# SIMULAR CLIMA
# =========================

def simular_clima(nuevo_clima):
    pass


# =========================
# OPCIÓN 4
# CALCULAR RUTA
# =========================

def calcular_ruta_eficiente():
    pass


# =========================
# OPCIÓN 5
# ESTADO DE FLOTA
# =========================

def mostrar_estado_flota():
    for id_vehiculo, datos in flota.items():
        print(
            f"ID: {id_vehiculo}",
            f"Tipo: {datos['tipo']}",
            f"Capacidad Máxima: {datos['capacidad_maxima']} kg, ",
            f"Batería: {datos['bateria']}%,"
            f"Estado: {datos['estado']}",
            f"Ubicación Actual: {datos['ubicacion_actual']}"
            )
        

# =========================
# OPCIÓN 6
# AVANCE DE TIEMPO
# =========================

def avanzar_tiempo():
    pass


# =========================
# OPCIÓN 7
# CARGAR VEHÍCULO
# =========================

def cargar_vehiculo(id_vehiculo):
    pass


# =========================
# OPCIÓN 8
# REPORTE DE EFICIENCIA
# =========================

def reporte_eficiencia():
    pass


# =========================
# OPCIÓN 9
# GRÁFICOS
# =========================

def grafico_consumo():
    pass


def grafico_climas():
    pass


def mostrar_graficos():
    grafico_consumo()
    grafico_climas()


# =========================
# MENÚ PRINCIPAL
# =========================

def menu():
    pass


# =========================
# INICIO DEL PROGRAMA
# =========================

menu()
