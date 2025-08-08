# Animación sencilla: serpiente de colores en la terminal
import time
import os
import random

colors = [
	'\033[91m', # rojo
	'\033[92m', # verde
	'\033[93m', # amarillo
	'\033[94m', # azul
	'\033[95m', # magenta
	'\033[96m', # cyan
	'\033[97m', # blanco
]

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def snake_animation(length=20, steps=60, delay=0.07):
	pos = 0
	direction = 1
	for _ in range(steps):
		clear()
		color = random.choice(colors)
		snake = ' ' * pos + color + '■' * length + '\033[0m'
		print(snake)
		time.sleep(delay)
		if pos >= 40:
			direction = -1
		elif pos <= 0:
			direction = 1
		pos += direction

if __name__ == "__main__":
	print("Animación: serpiente de colores. Pulsa Ctrl+C para salir.")
	try:
		snake_animation()
	except KeyboardInterrupt:
		print("\n¡Hasta luego!")
