import networkx as nx

from database.DAO import DAO
from model.Country import Country


class Model:

    def __init__(self):
        #DAO.getAllNodes()
        self._graph = nx.Graph()
        self._idMap = {}
        #for country in self._countries:
            #self._idMap[country.CCode] = country
        self._year = None
        self._nodes = None



    def buildGraph(self):
        #self._graph.add_nodes_from(self._countries)
        self.addAllNodes()
        self.addAllEdges()




    def calcolaNumeroComponentiConnesse(self):
        num_componenti = nx.number_connected_components(self._graph)
        return num_componenti

    def cacolaGradoDiUnNodo(self,node: Country):
        grado = self._graph.degree[node]
        return grado



    def addAllNodes(self):
        self._nodes = DAO.getAllNodes(self._year)
        self._graph.add_nodes_from(self._nodes)
        for country in self._nodes:
            self._idMap[country.CCode] = country


    def addAllEdges(self):
        edges = DAO.getAllEdges(self._idMap, self._year)
        self._graph.add_edges_from(edges)


    def cercaNodiConnessiBFS(self,source):
        nodi = list(nx.bfs_tree(self._graph, source))
        if len(nodi) == 1:
            return None
        else:
            return nodi[1:]

    def visita_iterativa(self, source):
        visitati = set()
        da_visitare = [source]

        while da_visitare:
            nodo = da_visitare.pop()
            if nodo not in visitati:
                visitati.add(nodo)
                for vicino in self._graph.neighbors(nodo):
                    if vicino not in visitati:
                        da_visitare.append(vicino)

        return visitati




    @property
    def getNumNodes(self):
        return len(self._graph.nodes)


    @property
    def getNumEdges(self):
        return self._graph.number_of_edges()


    @property
    def getNodes(self):
        return self._nodes



    def setAnno(self, year):
        self._year = year

