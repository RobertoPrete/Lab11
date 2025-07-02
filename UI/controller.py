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

    def readColor(self, e):
        self._color = e.control.value

    def handle_graph(self, e):
        pass


    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
