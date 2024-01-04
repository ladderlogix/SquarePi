# SquarePi
There are many werid ways to calculate pi. This way uses a squre and a circle with the radius of one and randomly points the dots and using some math with can aproxmityly find pi

## How to use
Run main.py and edit the config that pops up

## Installation

1.) Clone
``` Bash
git clone github.com/sglombicki/SqurePi.git
```
2.) Install Requirements
``` Bash
pip install PyQt5
pip install Pygame
```

3.) Run main.py
``` Bash
python3 main.py
```
## Math behind the idea
```python
pi = 4*(NumberInCircle/NumberOfCircles)
```
The idea is that generating random numbers and ploting them on a graph with a circle we can aproximate its area by finding the ratio and times it by the area
