import random   # Libreria para introducir numeros aleatorios

class Nodo:
    # Un nodo necesita una etiqueta para identificarlo, un ID
    def __init__(self,id):
        self.id = id
    # Se define el método para comparar 2 nodos, son iguales si sus ID son iguales
    def __eq__(self,other):
        if not isinstance(other, Nodo):
            return NotImplemented
        return self.id == other.id

class Arista:
    # Una arista necesita un nodo inicial, un nodo final, y saber si es dirigida o no
    def __init__(self,nodo1,nodo2,dirigido=False):
        self.nodo_inicial = nodo1
        self.nodo_final = nodo2
        self.dirigido = dirigido
    # Se define el método para comparar 2 aristas, son iguales si ambos nodos iniciales son identicos, y ambos 
    # finales tambien, y si es no dirigido, tambien si son iguales el nodo inicial de la arista 1 y el nodo final 
    # de la arista 2, y el nodo final de la arista 1 junto con el nodo inicial de la arista 2.
    def __eq__(self,other):
        if not isinstance(other, Arista):
            return NotImplemented
        mismo_sentido = (self.nodo_inicial == other.nodo_inicial and self.nodo_final == other.nodo_final)
        sentido_inverso = (self.nodo_inicial == other.nodo_final and self.nodo_final == other.nodo_inicial)
        if self.dirigido==False:
            return mismo_sentido or sentido_inverso
        else:
            return mismo_sentido

class Grafo:
    # Un grafo necesita saber sus nodos, sus aristas, su lista de adyacencia y si es dirigido o no.
    # Estrictamente, con la lista de adyacencia basta pero las listas de nodos y aristas nos ayudan a
    # escribir diferentes métodos necesarios de una forma más sencilla que revisar la lista.
    def __init__(self, dirigido=False):
        self.lista_adyacencia = {}
        self.dirigido = dirigido
        self.nodos = []
        self.aristas = []

    def agregar_nodo(self, id):
        # Crear el nodo
        nuevo_nodo = Nodo(id)
        # Si el nodo no esta, lo agrega
        if nuevo_nodo.id not in self.lista_adyacencia:
            self.lista_adyacencia[nuevo_nodo.id] = set()
        if nuevo_nodo not in self.nodos:
            self.nodos.append(nuevo_nodo)

    def agregar_arista(self, nodo1, nodo2):
        # No permitir aristas entre el mismo nodo (lazos)
        if nodo1 == nodo2:
            return
        # No perimitir aristas repetidas
        if nodo1 in self.lista_adyacencia and nodo2 in self.lista_adyacencia[nodo1]:
            return
        # Crear y agregar la nueva arista
        nueva_arista = Arista(nodo1, nodo2, self.dirigido)
        self.aristas.append(nueva_arista)
        # Crear los nodos si es que no existen
        if nueva_arista.nodo_inicial not in self.lista_adyacencia:
            self.agregar_nodo(nueva_arista.nodo_inicial)
        if nueva_arista.nodo_final not in self.lista_adyacencia:
            self.agregar_nodo(nueva_arista.nodo_final)
        # Añadir la arista a la lista de adyacencia
        self.lista_adyacencia[nueva_arista.nodo_inicial].add(nueva_arista.nodo_final)
        # Si el grafo no es dirigido, añadir el sentido inverso tambien
        if self.dirigido == False:
            self.lista_adyacencia[nueva_arista.nodo_final].add(nueva_arista.nodo_inicial)

    def exportar_a_GraphViz(self, nombre_archivo):
        if self.dirigido == True:
            declaracion = "digraph"
            conector = "->"
        else:
            declaracion = "graph"
            conector = "--"
        with open(nombre_archivo, "w") as archivo:
            archivo.write(f"{declaracion} G {{\n")
            for arista in self.aristas:
                archivo.write(f"{arista.nodo_inicial} {conector} {arista.nodo_final};\n")
            # Si hay un nodo que no tenga aristas, faltará en el archivo .gv, si se desease
            # agregar todos los nodos aunque no esten conectados, se podría añadir cada nodo individualmente
            #for nodo in self.nodos:
            #    archivo.write(f"{nodo.id};\n")
            archivo.write("}\n")
            archivo.close()
        return self

def grafoMalla(m, n, dirigido=False):
    grafo = Grafo(dirigido)
    for i in range(m):
        for j in range(n):
            grafo.agregar_nodo(f"{i}_{j}")
            if i+1 < m:
                grafo.agregar_arista(f"{i}_{j}",f"{i+1}_{j}")
            if j+1 < n:
                grafo.agregar_arista(f"{i}_{j}",f"{i}_{j+1}")
    return grafo

#malla_50 = grafoMalla(10,5).exportar_a_GraphViz("malla_50.gv")
#malla_200 = grafoMalla(20,10).exportar_a_GraphViz("malla_200.gv")
#malla_500 = grafoMalla(25,20).exportar_a_GraphViz("malla_500.gv")

def grafoErdosRenyi(n, m, dirigido=False):
    grafo = Grafo(dirigido)
    if dirigido == False:
        max_aristas = (n*(n-1))/2
    else:
        max_aristas = n*(n-1)
    if m > max_aristas:
        m = max_aristas

    for i in range(n):
        grafo.agregar_nodo(f"{i+1}")

    while (len(grafo.aristas) < m):
        aleatorio_1 = random.randint(1, n)
        aleatorio_2 = random.randint(1, n)
        grafo.agregar_arista(f"{aleatorio_1}", f"{aleatorio_2}")

    return grafo

#erdosrenyi_50 = grafoErdosRenyi(50,200).exportar_a_GraphViz("Erdos_50.gv")
#erdosrenyi_200 = grafoErdosRenyi(200,550).exportar_a_GraphViz("Erdos_200.gv")
#erdosrenyi_500 = grafoErdosRenyi(500, 1500).exportar_a_GraphViz("Erdos_500.gv")

def grafoGilbert(n, p, dirigido=False):
    grafo = Grafo(dirigido)
    
    for i in range(n):
        grafo.agregar_nodo(f"{i+1}")

    for i in range(n):
        if dirigido:
            inicio_j = 0
        else:
            inicio_j = i+1

        for j in range(inicio_j, n):
            if j==i:
                continue
            aleatorio = random.random()
            if aleatorio <= p:
                grafo.agregar_arista(f"{i+1}",f"{j+1}")
    return grafo

#gilbert_50 = grafoGilbert(50, 0.08).exportar_a_GraphViz("gilbert_50.gv")       # 50 nodos, 8% de probabilidad de arista
#gilbert_200 = grafoGilbert(200, 0.025).exportar_a_GraphViz("gilbert_200.gv")   # 200 nodos, 2.5% de probabilidad de arista
#gilbert_500 = grafoGilbert(500, 0.01).exportar_a_GraphViz("gilbert_500.gv")    # 500 nodos, 1% de probabilidad de arista

def grafoGeografico(n, r, dirigido=False):
    grafo = Grafo(dirigido)
    lista_x = list()
    lista_y = list()

    for i in range(n):
        coordenada_x = random.random()
        coordenada_y = random.random()
        grafo.agregar_nodo(f"{i+1}")
        lista_x.append(coordenada_x)
        lista_y.append(coordenada_y)
    
    for i in range(n):
        for j in range(i+1, n):
            delta_x = lista_x[i] - lista_x[j]
            delta_y = lista_y[i] - lista_y[j]
            distancia = (delta_x**2)+(delta_y**2)
            if distancia <= r**2:
                grafo.agregar_arista(f"{i+1}", f"{j+1}")
                if dirigido == True:
                    grafo.agregar_arista(f"{j+1}", f"{i+1}")
    return grafo
    
#geo_50 = grafoGeografico(50, 0.25).exportar_a_GraphViz("geo_50.gv")
#geo_200 = grafoGeografico(200, 0.15).exportar_a_GraphViz("geo_200.gv")
#geo_500 = grafoGeografico(500, 0.1).exportar_a_GraphViz("geo_500.gv")

def grafoBarabasiAlbert(n, d, dirigido=False):
    grafo = Grafo(dirigido)
    lista_grados = list()
    
    for i in range(d):
        grafo.agregar_nodo(f"{i+1}")
    
    for i in range(d):
        if dirigido:
            inicio_j = 0
        else:
            inicio_j = i + 1
        for j in range(inicio_j, d):
            grafo.agregar_arista(f"{i+1}",f"{j+1}")
        lista_grados.append(d-1)
    
    for i in range(d, n):
        grafo.agregar_nodo(f"{i+1}")
        muestras = set()
        while len(muestras) < d:
            nodo_seleccionado = random.choices(grafo.nodos[:-1], lista_grados)
            nodo_sel_id = nodo_seleccionado[0].id
            if nodo_sel_id not in muestras:
                grafo.agregar_arista(f"{i+1}",nodo_sel_id)
                muestras.add(nodo_sel_id)
                lista_grados[int(nodo_sel_id) - 1] += 1
        lista_grados.append(d)
    return grafo

#barabasi_50 = grafoBarabasiAlbert(50, 2).exportar_a_GraphViz("barabasi_50.gv")
#barabasi_200 = grafoBarabasiAlbert(200, 2).exportar_a_GraphViz("barabasi_200.gv")
#barabasi_500 = grafoBarabasiAlbert(500, 3).exportar_a_GraphViz("barabasi_500.gv")

def grafoDorogovstevMendes(n, dirigido=False):
    grafo = Grafo(dirigido)

    for i in range(3):
        grafo.agregar_nodo(f"{i+1}")

    for i in range(3):
        for j in range(i+1, 3):
            grafo.agregar_arista(f"{i+1}",f"{j+1}")

    for i in range(3, n):
        aleatorio = random.randint(0, len(grafo.aristas) - 1)
        arista_seleccionada = grafo.aristas[aleatorio]
        grafo.agregar_nodo(f"{i+1}")
        grafo.agregar_arista(f"{i+1}", arista_seleccionada.nodo_inicial)
        grafo.agregar_arista(f"{i+1}", arista_seleccionada.nodo_final)
    
    return grafo

#dorogovstev_50 = grafoDorogovstevMendes(50).exportar_a_GraphViz("dorogovstev_50.gv")
#dorogovstev_200 = grafoDorogovstevMendes(200).exportar_a_GraphViz("dorogovstev_200.gv")
#dorogovstev_500 = grafoDorogovstevMendes(500).exportar_a_GraphViz("dorogovstev_500.gv")
