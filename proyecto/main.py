# =========================
# IMPORTS
# =========================

import matplotlib.pyplot as plt


# =========================
# COLORES DE CONSOLA
# =========================

ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
RESET = "\033[0m"


# =========================
# DATOS INICIALES
# =========================

flota = {
    # mínimo 2 drones
    # mínimo 2 motos
    # mínimo 2 camiones
}

pedidos = [
    # mínimo 8 pedidos
]

restricciones = {
    "Lluvia": "Drone",
    "Tormenta": "Moto",
    "Calor extremo": None
}

consumo_acumulado = {
    "Drone": 0,
    "Moto": 0,
    "Camion": 0
}

estadisticas_vehiculos = {
    # ID: energía consumida + peso transportado
}

clima_actual = "Normal"


# =========================
# FUNCIONES AUXILIARES
# =========================

def buscar_pedido(id_pedido):
    pass


def buscar_vehiculo(id_vehiculo):
    pass


def buscar_pedido_por_vehiculo(id_vehiculo):
    pass


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
    pass


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
    pass


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