from database.DAO import DAO


class Model:
    def __init__(self):
        self._colors = DAO.getColors()
        self._years = DAO.getYears()

    def getColors(self):
        return self._colors

    def getYears(self):
        return self._years
