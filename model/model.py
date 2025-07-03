import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._colors = DAO.getColors()
        self._selectedColor = None
        self._years = DAO.getYears()
        self._selectedYear = None
        self._graph = nx.Graph()
        self._products = DAO.getAllProducts()
        self._idMapProducts = {}
        for product in self._products:
            self._idMapProducts[product.Product_number] = product

        self._nodes = None
        self._edges = None

    def getColors(self):
        return self._colors

    def setColor(self, color):
        self._selectedColor = color

    def getYears(self):
        return self._years

    def setYear(self, year):
        self._selectedYear = year

    def buildGraph(self):
        self._graph.clear()
        self._nodes = DAO.getAllNodes(self._selectedColor)
        self._graph.add_nodes_from(self._nodes)
        # ricavare gli archi e aggiungerli
        self._edges = DAO.getAllEdges(self._selectedColor, self._selectedYear, self._idMapProducts)
        for edge in self._edges:
            u = edge.p1
            v = edge.p2
            if self._graph.has_node(u) and self._graph.has_node(v):
                if self._graph.has_edge(u, v):
                    self._graph[u][v]['weight'] += 1
                else:
                    self._graph.add_edge(u, v, weight=1)

    def graphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getArchi(self):
        return self._graph.edges(data=True)


