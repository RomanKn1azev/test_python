import pandas as pd
import numpy as np
import json


class DataFrameStats:
    def __init__(self, data, cfg):
        self.__data = data
        self.__numeric_stats = cfg['numeric']
        self.__categorical_stats = cfg['categorical']
        self.__ignore = cfg.get('ignore', None)

        if self.__ignore:
            self.__data.drop(columns=self.__ignore, inplace=True)
    
    def calc_stats(self):
        stats = {}

        numeric_cols = self.__data.select_dtypes(include=['number']).columns
        categorical_cols = self.__data.select_dtypes(include=['object', 'category']).columns

        for col in numeric_cols:
            stats[col] = {}
            for stat in self.__numeric_stats:
                if stat == 'type':
                    stats[col]['type'] = self.__data[col].dtype
                elif stat == 'mean':
                    stats[col]['mean'] = self.__data[col].mean().round(3)
                elif stat == 'median':
                    stats[col]['median'] = self.__data[col].median().round(3)
                elif stat == 'std':
                    stats[col]['std'] = self.__data[col].std().round(3)
                elif stat == 'min':
                    stats[col]['min'] = self.__data[col].min().round(3)
                elif stat == 'max':
                    stats[col]['max'] = self.__data[col].max().round(3)
                elif stat == 'mode':
                    stats[col]['mode'] = self.__data[col].mode()[0].round(3)
                elif stat == 'percent_zero':
                    stats[col]['percent_zero'] = ((self.__data[col] == 0).mean() * 100).round(3)
                elif stat == 'variance':
                    stats[col]['variance'] = self.__data[col].var().round(3)
                elif stat == 'std':
                    stats[col]['std'] = self.__data[col].std().round(3)
                elif stat == 'iqr':
                    stats[col]['iqr'] = (np.percentile(self.__data[col], 75) - np.percentile(self.__data[col], 25)).round(3)
                elif stat == 'coef_variation':
                    stats[col]['coef_variation'] = (self.__data[col].std() / self.__data[col].mean()).round(3)
                elif stat == 'unique_count':
                    stats[col]['unique_count'] = self.__data[col].nunique()

        for col in categorical_cols:
            stats[col] = {}
            for stat in self.__categorical_stats:
                if stat == 'type':
                    stats[col]['type'] = self.__data[col].dtype
                elif stat == 'mode':
                    stats[col]['mode'] = self.__data[col].mode()[0]
                elif stat == 'unique_count':
                    stats[col]['unique_count'] = self.__data[col].nunique()
                elif stat == 'value_counts':
                    stats[col]['value_counts'] = self.__data[col].value_counts().to_dict()#.apply(json.dumps)

        return stats