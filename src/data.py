from utils import read_csv


class RawData:
    def __init__(self, path):
        self.__path = path
        self.__data = read_csv(path)

    @property
    def path(self):
        return self.__path

    @property
    def data(self):
        return self.__data