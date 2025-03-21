from collections import deque

grafo = {
    'A': ['B', 'F'],
    'B': ['A', 'C', 'G'],
    'C': ['B', 'D', 'H'],
    'D': ['C', 'E', 'I'],
    'E': ['D'],
    'F': ['A', 'G', 'J'],
    'G': ['B', 'F', 'H'],
    'H': ['C', 'G', 'I', 'L'],
    'I': ['D', 'H'],
    'J': ['F', 'K'],
    'K': ['J', 'L'],
    'L': ['H', 'K']
}

nodoInicio = 'A'
nodoMeta = 'L'

def busquedaBidireccional(grafo, inicio, meta):
    colaInicio = deque()
    colaMeta = deque()
    
    visitadosInicio = {}
    visitadosMeta = {}
    
    colaInicio.append(inicio)
    visitadosInicio[inicio] = None
    
    colaMeta.append(meta)
    visitadosMeta[meta] = None
    
    while colaInicio and colaMeta:
        buscarInicio = colaInicio.popleft()
        for vecino in grafo[buscarInicio]:
            if vecino not in visitadosInicio:
                visitadosInicio[vecino] = buscarInicio
                colaInicio.append(vecino)
                
            if vecino in visitadosMeta:
                return rutaCompleta(visitadosInicio, visitadosMeta, vecino)
        
        buscarMeta = colaMeta.popleft()
        for vecino in grafo[buscarMeta]:
            if vecino not in visitadosMeta:
                visitadosMeta[vecino] = buscarMeta
                colaMeta.append(vecino)
                
            if vecino in visitadosInicio:
                return rutaCompleta(visitadosInicio, visitadosMeta, vecino)
    
    return None

def rutaCompleta(visitadosInicio, visitadosMeta, puntoDeEncuentro):
    puntoDeInicio = []
    actual = puntoDeEncuentro
    while actual is not None:
        puntoDeInicio.append(actual)
        actual = visitadosInicio[actual]
    
    puntoDeMeta = []
    actual = puntoDeEncuentro
    while actual is not None:
        puntoDeMeta.append(actual)
        actual = visitadosMeta[actual]
    
    puntoDeInicio.reverse()
    puntoDeMeta = puntoDeMeta[1:]
    caminoCompleto = puntoDeInicio + puntoDeMeta
    
    return caminoCompleto

path = busquedaBidireccional(grafo, nodoInicio, nodoMeta)
if path:
    print("Camino encontrado:", path)
else:
    print("No se encontró un camino.")