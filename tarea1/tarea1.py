### Tarea 1 ###

### Queue ###
# Hay una manera estándar para poder declarar queues, o filas.
## de la librería
from collections import dequeue
import Queue
import Stack
# Declarar una fila
queue = deque([])

# Insertar datos en la fila
queue.append('hello')
queue.append('world')

# Sacar datos datos a la derecha de la fila
queue.pop()

# Sacar datos a la izquierda de la fila
queue.popleft()

### La otra manera de hacer un Queue o fila sería creando la clase manualmente, como en el ejemplo
### En este ejemplo creé mi propia API para interactuar con la clase Queue, que también creé desde cero.
q = Queue.Queue()

# Insertar datos a la fila
q.push(1)
q.push(2)
q.push(21)
q.push(22)
q.push(23)

# Ver el primer dato de la fila

print(q.front()) # 1

# Ver el último dato de la fila

print(q.back()) # 23

# Sacar el primer elemento de la lista

q.pop_front() # 1

# Sacar el último elemento del a lista

q.pop_back() # 23

# Ver el elemento en posición x
q.at(2) # 21

# Ver el tamaño del a lista

print(q.length()) # 3

# Imprimir la lista

q.display()
# 2
# 2
# 21
# 22

### Stack ###
# Un stack puede funcionar como una lista normal
stack = []

# Insertar valores en el stack
stack.append('Hello')
stack.append('World')

# Sacar el primer valor de la lista
stack.pop() # World

# Igual que en Filas, hice mi propia clase de Stack
# Inizializar un stack
s = Stack.Stack()

# Agregar datos al stack
s.push(10)
s.push('hola')
s_2 = Stack.Stack()
s.push(500)
s.push(stack_2)
s.push('Mundo')

# Ver el primer dato
print(s.top()) # Mundo

# Pop - regresa el dato de mero arriba y lo saca
s.pop() # 'Mundo'

# Ver el dato en posición x
s.at(5) # 'Mundo'

# Desplegar el stack
s.display()

### Diccionarios ###
diccionario = {}
diccionario['hola'] = 'mundo'

# sacar las llaves
diccionario.keys() # hola

# sacar los valores
diccionario.values() # Mundo

# quitar un llave- valor
del diccionario['hola']

# Checar si hay un valor con una llave

'hola' in diccionario # false
