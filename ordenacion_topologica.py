"""
Para este ejercicio, unos de los algoritmos mas aptos es el Algoritmo de Kahn.
Este algoritmo se basa en la idea de eliminar las tareas que no tienen dependencias,  
y luego repetir el proceso hasta que todas las tareas hayan sido procesadas.
El algoritmo de Kahn es práctico aquí porque es fácil de entender y eficiente para ordenar tareas con restricciones, 
detecta restricciones circulares y ofrece resultados rápidos con una complejidad de tiempo adecuada. 
Su lógica de eliminar tareas sin dependencias y procesar las restantes se adapta bien a la naturaleza del problema.
"""

from collections import defaultdict, deque

def topological_sort(num_tasks, constraints):
    # Inicializar el grafo y el contador de predecesores
    graph = defaultdict(list)
    in_degree = [0] * (num_tasks + 1)
    
    # Construir el grafo y contar los predecesores
    for constraint in constraints:
        u, v = constraint
        graph[u].append(v)
        in_degree[v] += 1
    
    # Inicializar la cola con las tareas sin predecesores
    queue = deque([i for i in range(1, num_tasks + 1) if in_degree[i] == 0])
    
    # Inicializar la lista para almacenar el orden topológico
    topological_order = []
    
    # Procesar las tareas en orden topológico
    while queue:
        task = queue.popleft()
        topological_order.append(task)
        
        # Reducir el contador de predecesores de las tareas sucesoras
        for successor in graph[task]:
            in_degree[successor] -= 1
            if in_degree[successor] == 0:
                queue.append(successor)
    
    # Si no se procesaron todas las tareas, no hay ordenación topológica
    if len(topological_order) != num_tasks:
        return None
    
    return topological_order

# Ejemplo de uso
num_tasks = 6
constraints = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (4, 6)]

result = topological_sort(num_tasks, constraints)
if result:
    print("Orden topológico de las tareas:", result)
else:
    print("No se puede encontrar una ordenación topológica debido a restricciones circulares.")
