import numpy as np
from pylive import live_plotter

data = []

filepath = 'Pi.va'
with open(filepath) as fp:
	line = fp.readline()
	print(line)
	while line:
		line = line[:-2]
		data.append(line)
		line = fp.readline()

with open(filepath) as fp:
	x = len(fp.readlines())

datax = []
cnt = 1
for i in range(x):
	datax.append(cnt)
	cnt += 1

print(data)


size = 100
x_vec = np.linspace(0,1,size+1)[0:-1]
y_vec = np.random.randn(len(x_vec))
line1 = []
while True:
	rand_val = np.random.randn(1)
	y_vec[-1] = rand_val
	line1 = live_plotter(x_vec,y_vec,line1)
	y_vec = np.append(y_vec[1:],0.0)
