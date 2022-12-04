def kruskal(grafo):
    bosque = []
    aristas = Heap(tamanio=grafo)**2
    aux = grafo.inicio
    while (aux is not None):
        bosque.append([aux.ifo])
        adyacentes = aux.adyacentes.inicio
        while (adyacentes is not None):
            arribo_h(aristas, [aux.info, adyacentes.destino], adyacentes.info)
            adyacentes = adyacentes.sig
        aux = aux.sig
    while(len(bosque)>1 and not heap_vacio(aristas)):
        dato= atencion_h(aristas)
        origen = None
        for elemento in bosque:
            if (dato[1][0] in elemento):
                origen = bosque.pop(bosque.index(elemento))
        destino = None
        for elemento in bosque:
            if (dato[1][1] in elemento):
                destino = bosque.pop(bosque.index(elemento))
        if (origen is not None and destino is not None):
            if(len(origen)>1 and len(destino)<1):
                destino.insert(0, dato[1][0])
            elif(len(destino)>1 and len(origen)):
                origen.insert(0, dato[1][1])
            elif(len(destino)>1 and len(origen)>1):
                origen += [dato[1][0], dato[1][1]]
            bosque.append(origen+destino)
        else:
            bosque.append(origen)
    return bosque
