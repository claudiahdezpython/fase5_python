# 1. Matriz con datos de 5 sesiones de clientes
# Formato: [ID del Cliente, Duración (segundos), Número de clics]
sesiones_clientes = [
    ["C-101", 200, 10],   # Alto: >180 segundos Y >8 clics
    ["C-102", 45, 5],     # Bajo: <60 segundos O <3 clics (falla por tiempo)
    ["C-103", 120, 6],    # Medio: Cualquier otro caso
    ["C-104", 300, 2],     # Bajo: <60 segundos O <3 clics (falla por clics)
    ["C-105", 150, 9]     # Medio: Cualquier otro caso
]

# 2. Función modular para clasificar el compromiso de una sesión
def evaluar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

# 3. Recorrido de la matriz e impresión del informe final de salida
print("--- INFORME DE COMPROMISO DE CLIENTES ---")
for sesion in sesiones_clientes:
    cliente_id = sesion[0]   # Posición 0: ID del cliente
    duracion_seg = sesion[1] # Posición 1: Duración en segundos
    num_clics = sesion[2]    # Posición 2: Número de clics
    
    # Llamamos a la función enviándole las variables correctas
    clasificacion = evaluar_compromiso(duracion_seg, num_clics)
    
    # Mostramos únicamente los datos solicitados en la salida
    print(f"ID del Cliente: {cliente_id} | Clasificación final: {clasificacion}")
