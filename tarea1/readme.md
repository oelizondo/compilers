## Tarea 1

### Stack (LIFO)

```python
import Stack

# Inizializar un stack
stack = Stack.Stack()

# Agregar datos al stack
stack.push(10)
stack.push('hola')
stack_2 = Stack.Stack()
stack_2.push(500)
stack.push(stack_2)

# Ver el primer dato
print(stack.top())

# Pop - regresa el dato de mero arriba y lo saca
stack.pop()

# Ver el dato en posición x
stack.at(5)

# Desplegar el stack
stack.display()
```

### Queue (FIFO)

```python
import Queue

# Inizializar un stack
queue = Queue.Queue()

# Agregar datos al queue
queue.push(10)
queue.push('hola')
queue_2 = Queue.Queue()
queue_2.push(500)
queue.push(queue_2)

# Ver el primer dato
print(queue.front())

# Ver el ultiom dato
print(queue.back())

# Pop_front - regresa el primer dato  y lo saca del queue
queue.pop_front()

# Pop_back - regresa el ultimo dato y lo saca del queue

# Ver el dato en posición x
queue.at(5)

# Imprimir el tamaño del queue
print(queue.length())

# Imprimir el queue
queue.display()
```

### Dictionary / Hash
