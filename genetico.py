import random
import math


def principal():
	n = 30
	poblacion = [0] * n
	for i in range(n):
		poblacion[i] = random.randint(1,15)
	return poblacion

def objetivo(poblacion):
	ma = 0
	feno = 0
	for i in range(30):
		Max=poblacion[i] ** 2 + 2
		print(Max)
		if Max > ma:
			ma = Max
			feno= poblacion[i]
	print(" El valor Mayor es ", ma ," con el numero ", feno)

# principal()
objetivo(principal())


