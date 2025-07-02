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

    def graphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

