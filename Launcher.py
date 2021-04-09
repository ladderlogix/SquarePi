import os
import UI

try:
	os.remove("Pi.va")
	os.remove("Points.va")
except:
	pass

UI.run()
