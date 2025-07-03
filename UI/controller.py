import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []
        self._year = None
        self._color = None


    def fillDD(self):
        self._listYear = self._model.getYears()
        self._listColor = self._model.getColors()
        for year in self._listYear:
            self._view._ddyear.options.append(ft.dropdown.Option(year))
        for colore in self._listColor:
            self._view._ddcolor.options.append(ft.dropdown.Option(colore))

        self._view.update_page()

    def readYear(self, e):
        self._year = e.control.value
        self._model.setYear(self._year)

    def readColor(self, e):
        self._color = e.control.value
        self._model.setColor(self._color)

    def handle_graph(self, e):
        self._view.txtOut.controls.clear()
        self._model.buildGraph()
        numero_vertici, numero_archi = self._model.graphDetails()
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {numero_vertici} Numero di archi: {numero_archi}"))
        # stampare i tre archi di peso maggiore
        # stampare i nodi presenti in più di uno dei tre archi

        self._view.update_page()


    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
