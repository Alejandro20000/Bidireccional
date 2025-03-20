#para poder usar listas que se puede manipular de mejor forma 
from collections import deque

#Grafo que se usara de ejemplo
grafo = {
    'A': ['B', 'E'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'D', 'E'],
    'D': ['C'],
    'E': ['A', 'B', 'C'],
    'F': ['D']
}

#Variables que se desea buscar
nodoInicio='A'
nodoMeta='F'

#Ruta
ruta = deque()

#Metodo de busqueda bidireccional 
def busquedaBidireccional(grafo, inicio, meta):
    # Colas para las dos busquedas
    colaInicio = deque([inicio])
    colaMeta = deque([meta])
    
    # Listas de nodos visitados
    visitadosInicio = {inicio}
    visitadosMeta = {meta}
    
    #Inicia un bucle para hallar la ruta
    while colaInicio and colaMeta:
        #Crea un deque para verificar resultados sin involucrar el inicio
        nodoActualInicio = colaInicio.popleft()
        #Inicia un bucle que verifica si el nodo esta en la lista
        for vecino in grafo[nodoActualInicio]:
            if vecino in visitadosMeta:
                if nodoInicio!=nodoActualInicio:
                    ruta.appendleft(nodoActualInicio)
                    busquedaBidireccional(grafo, nodoInicio, nodoActualInicio)
                    busquedaBidireccional(grafo, nodoActualInicio, nodoMeta)
                ruta.appendleft(nodoActualInicio)
                return
                #return f"{nodoActualInicio} -> {vecino}"
            if vecino not in visitadosInicio:
                visitadosInicio.add(vecino)
                colaInicio.append(vecino)
        
        #Crea un deque para verificar resultados sin involucrar la meta
        nodoActualMeta = colaMeta.popleft()
        #Inicia un bucle que verifica si el nodo esta en la lista
        for vecino in grafo[nodoActualMeta]:
            if vecino in visitadosInicio:
                if nodoMeta!=nodoActualMeta:
                    ruta.append(nodoActualMeta)
                    busquedaBidireccional(grafo, nodoActualMeta, nodoMeta)
                    busquedaBidireccional(grafo, nodoInicio, nodoActualMeta)
                ruta.append(nodoActualMeta)
                return 
                #return f"{vecino} -> {nodoActualMeta}"
            if vecino not in visitadosMeta:
                visitadosMeta.add(vecino)
                colaMeta.append(vecino)
    
    return "No hay ruta"

#Para ver la ruta corta que se logro conseguir
busquedaBidireccional(grafo, nodoInicio, nodoMeta)
