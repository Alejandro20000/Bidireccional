from collections import deque

grafo = {
    'A': ['C'],
    'C': ['A', 'D', 'F'],
    'D': ['C'],
    'F': ['C', 'G', 'I'],
    'G': ['L', 'K', 'F'],
    'H': ['X', 'P', 'R'],
    'I': ['F', 'X'],
    'K': ['G'],
    'L': ['G'],
    'M': ['Y'],
    'N': ['Y'],
    'P': ['H'],
    'R': ['H'],
    'X': ['I', 'Y', 'H'],
    'Y': ['M', 'N', 'X']
}

nodoInicio = 'A'
nodoMeta = 'R'

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
    rutaDeInicio = []
    actual = puntoDeEncuentro
    while actual is not None:
        rutaDeInicio.append(actual)
        actual = visitadosInicio[actual]
    
    rutaDeMeta = []
    actual = puntoDeEncuentro
    while actual is not None:
        rutaDeMeta.append(actual)
        actual = visitadosMeta[actual]
    
    rutaDeInicio.reverse()
    rutaDeMeta = rutaDeMeta[1:]
    caminoCompleto = rutaDeInicio + rutaDeMeta
    
    return caminoCompleto

ruta = busquedaBidireccional(grafo, nodoInicio, nodoMeta)
if ruta:
    print("Camino encontrado:", ruta)
else:
    print("No se encontró un camino.")