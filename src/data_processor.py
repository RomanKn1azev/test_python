from utils import read_yaml
from statistical_calc import DataFrameStats


class Summary:
    def __init__(self, data, config_path):
        self.__data = data
        self.__cfg_path = config_path
        self.__cfg = read_yaml(config_path)
        self.__stats = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def cfg_path(self):
        return self.__cfg_path

    @cfg_path.setter
    def cfg_path(self, value):
        self.__cfg_path = value
        self.__cfg = read_yaml(value)

    @property
    def cfg(self):
        return self.__cfg

    @cfg.setter
    def cfg(self, value):
        self.__cfg = value

    @property
    def stats(self):
        return self.__stats

    def run(self):
        self.__stats = DataFrameStats(self.__data, self.__cfg).calc_stats()