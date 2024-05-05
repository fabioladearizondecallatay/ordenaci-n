"""
Especificaciones del predicado está_explorado:

Precondición:
La tabla t debe contener elementos comparables.
La parte t[inicio .. fin] debe representar un segmento válido de la tabla t.

Postcondición:
Después de la ejecución del predicado está_explorado sobre la parte t[inicio .. fin] de la tabla t, 
cada componente estará colocado después de la serie más grande de componentes de la que es el máximo.

Explicación:
Para cada componente t[i] en el segmento t[inicio .. fin], se verifica que esté colocado después 
de la serie más grande de componentes de la que es el máximo.
Se entiende que la serie más grande de componentes de la que es el máximo es aquella serie consecutiva 
de elementos que comienza desde el máximo valor en el segmento y se extiende hasta el final del segmento.
Para lograr esto, el predicado está_explorado realiza los siguientes pasos:
- Hace copia de seguridad del máximo del segmento: mi = t[di], donde di es el índice del primer componente del segmento.
- Desplaza los elementos de t[di+1 .. fi] una celda hacia la izquierda.
- Coloca el elemento más grande del segmento "en lo alto": t[fi] = mi.
"""


def esta_explorado(t, inicio, fin):
    maximo = max(t[inicio:fin+1])
    indice_max = t.index(maximo)
    for i in range(indice_max, fin):
        t[i] = t[i+1]
    t[fin] = maximo
    return t

# Ejemplo de uso
t = [4, 8, 12, 18, 10, 15, 21, 7, 14, 18, 21]
inicio = 5
fin = 9

print("Tabla original:", t)
t = esta_explorado(t, inicio, fin)
print("Tabla después de explorar:", t)
