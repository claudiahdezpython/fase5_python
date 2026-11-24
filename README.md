# Análisis de Compromiso de Clientes - Fase 5

Este proyecto es la solución al **Problema 1** en el lenguaje Python. El programa organiza los datos de las sesiones de los usuarios y calcula de forma automática qué tan comprometidos están con la plataforma digital.

## 📊 ¿Cómo funciona la clasificación?
El programa revisa el tiempo que dura la sesión del cliente y los clics que realiza:
* **Alto:** Si la sesión dura más de 180 segundos Y tiene más de 8 clics.
* **Bajo:** Si la sesión dura menos de 60 segundos Ó tiene menos de 3 clics.
* **Medio:** Cualquier otro caso intermedio que no cumpla las anteriores.

## 🛠️ Estructura del Código
* **Matriz:** Los datos se guardan ordenados en una lista de listas.
* **Función:** Se usa una función separada para evaluar las condiciones de forma ordenada.
* **Ciclo For:** Se recorre de forma automática a cada cliente uno por uno para mostrar el reporte en la pantalla.
