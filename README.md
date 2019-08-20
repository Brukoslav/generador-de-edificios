# generador-de-edificios
Python code to procedurally generate voxel cities.

It needs [py-vox](https://github.com/gromgull/py-vox-io) to export to .vox 
You can render .vox files with [MagicaVoxel](https://ephtracy.github.io/).

# Instructions
Download generaEdificios.py
Download py-vox and put it in the same file than generaEdificios.py
Run the code.

# Parameters
You can modify parameters like number of buildings, size of map (up to 126), height of buildings, etc.

# Examples

!(https://raw.githubusercontent.com/Brukoslav/generador-de-edificios/master/ejemplos/ciudad01.png "Ejemplo 1")
```python
L = 120	# Tamaño / city size 
N = 200 # Número de casas / building size
ven = 2 # Separación entre ventanas / space between windows
altura = 0.6	# 0: sin superposición, 1: gran superposición
probaLuz = 0
ciudad = 5 		# 1: Uniformemente distribuidas, 20: todos en un extremo / all buildings on one axis
saturacion = [20,40]	#0: casas grises / grey houses. 100, casas coloridas / colorful houses
valor = [70,100]	#0: casas oscuras / dark colored houses. 100, casas claras / light colored houses
bioma = 2 		#0: city, 1 desert, 2 grass
```



!(https://raw.githubusercontent.com/Brukoslav/generador-de-edificios/master/ejemplos/ciudad02.png "Ejemplo 2")
```python
L = 120	# Tamaño / city size 
N = 200 # Número de casas / building size
ven = 2 # Separación entre ventanas / space between windows
altura = 0.7	# 0: sin superposición, 1: gran superposición
probaLuz = 0
ciudad = 1 		# 1: Uniformemente distribuidas, 20: todos en un extremo / all buildings on one axis
saturacion = [0,5]	#0: casas grises / grey houses. 100, casas coloridas / colorful houses
valor = [70,100]	#0: casas oscuras / dark colored houses. 100, casas claras / light colored houses
bioma = 0 		#0: city, 1 desert, 2 grass
```

!(https://raw.githubusercontent.com/Brukoslav/generador-de-edificios/master/ejemplos/ciudad03.png "Ejemplo 3")
```python
L = 120	# Tamaño / city size 
N = 20 # Número de casas / building size
ven = 3 # Separación entre ventanas / space between windows
altura = 0	# 0: sin superposición, 1: gran superposición
probaLuz = 0
ciudad = 1 		# 1: Uniformemente distribuidas, 20: todos en un extremo / all buildings on one axis
saturacion = [0,5]	#0: casas grises / grey houses. 100, casas coloridas / colorful houses
valor = [80,100]	#0: casas oscuras / dark colored houses. 100, casas claras / light colored houses
bioma = 1 		#0: city, 1 desert, 2 grass
```

!(https://raw.githubusercontent.com/Brukoslav/generador-de-edificios/master/ejemplos/ciudad04.png "Ejemplo 4")
```python
L = 120	# Tamaño / city size 
N = 400 # Número de casas / building size
ven = 2 # Separación entre ventanas / space between windows
altura = 0.6	# 0: sin superposición, 1: gran superposición
probaLuz = 0.1	# Probabilidad que la ventana esté iluminada / probability that windows has light
ciudad = 5 		# 1: Uniformemente distribuidas, 20: todos en un extremo / all buildings on one axis
saturacion = [0,5]	#0: casas grises / grey houses. 100, casas coloridas / colorful houses
valor = [70,90]	#0: casas oscuras / dark colored houses. 100, casas claras / light colored houses
bioma = 0 		#0: city, 1 desert, 2 grass
```
