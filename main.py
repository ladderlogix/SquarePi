import pygame
import random
import time
from math import sqrt
import json

f = open("Settings.json")
Settings = json.load(f)

BackgroundRedValue = Settings['BackgroundRedValue']
BackgroundBlueValue = Settings['BackgroundBlueValue']
BackgroundGreenValue = Settings['BackgroundGreenValue']
CircleRedValue = Settings['CircleRedValue']
CircleBlueValue = Settings['CircleBlueValue']
CircleGreenValue = Settings['CircleGreenValue']
DotsRedValue = Settings['DotsRedValue']
DotsBlueValue = Settings['DotsBlueValue']
DotsGreenValue = Settings['DotsGreenValue']
f.close()

pygame.init()

NumberOfCircles = 0
NumberInCircle = 0
pi = 3

ForceReloadA = False

screen = pygame.display.set_mode([500, 500])
screen.fill((BackgroundRedValue,BackgroundGreenValue,BackgroundBlueValue))

pygame.draw.circle(screen, (CircleRedValue, CircleGreenValue, CircleBlueValue), (250, 250), 250)

def ForceReload():
	f = open("Settings.json")
	Settings = json.load(f)

	BackgroundRedValue = Settings['BackgroundRedValue']
	BackgroundBlueValue = Settings['BackgroundBlueValue']
	BackgroundGreenValue = Settings['BackgroundGreenValue']
	CircleRedValue = Settings['CircleRedValue']
	CircleBlueValue = Settings['CircleBlueValue']
	CircleGreenValue = Settings['CircleGreenValue']
	DotsRedValue = Settings['DotsRedValue']
	DotsBlueValue = Settings['DotsBlueValue']
	DotsGreenValue = Settings['DotsGreenValue']

	screen.fill((BackgroundRedValue, BackgroundGreenValue, BackgroundBlueValue))
	pygame.draw.circle(screen, (CircleRedValue, CircleGreenValue, CircleBlueValue), (250, 250), 250)
	dataX = []
	dataY = []

	filepath = 'Points.va'
	with open(filepath) as fp:
		line = fp.readline()
		while line:
			PosOfMid = str.find(line,",")
			X = line[:PosOfMid]
			X = str.replace(X, " ", "")
			Y = line[PosOfMid:]
			Y = str.replace(Y,"\n","")
			Y = str.replace(Y, ", ", "")
			dataX.append(X)
			dataY.append(Y)
			line = fp.readline()

	with open(filepath) as fp:
		x = len(fp.readlines())

	for i in range(x):
		try:
			pygame.draw.circle(screen, (DotsRedValue, DotsGreenValue, DotsBlueValue), (int(dataX[i]), int(dataY[i])), 3)
		except:
			pass

def GenerateCircles(size):
	f = open("Settings.json")
	Settings = json.load(f)

	DotsRedValue = Settings['DotsRedValue']
	DotsBlueValue = Settings['DotsBlueValue']
	DotsGreenValue = Settings['DotsGreenValue']

	f.close()

	posx = random.randint(0,500)
	posy = random.randint(0,500)
	pygame.draw.circle(screen, (DotsRedValue,DotsGreenValue,DotsBlueValue), (posx, posy), size)
	distance = sqrt((posx - 250)**2 + (posy - 250)**2)
	with open("Points.va", "a+") as file_object:
		file_object.write("\n")
		file_object.write(str(posx) + " , " + str(posy))
		file_object.close()
	if distance**2 <= 250**2:
		global NumberInCircle
		NumberInCircle += 1

def PygameMain():
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		GenerateCircles(3)
		time.sleep(.1)
		global NumberOfCircles
		NumberOfCircles += 1

		global pi
		pi = 4*(NumberInCircle/NumberOfCircles)
		pi = str(pi)

		pygame.display.flip()
		with open("Pi.va", "a+") as file_object:
			file_object.write("\n")
			file_object.write(pi)
			file_object.close()

		return pi, NumberInCircle, NumberOfCircles
