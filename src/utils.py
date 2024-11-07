import pandas as pd
import yaml
import os


def read_csv(path: str):
    return pd.read_csv(path)


def read_yaml(path: str):
    with open(path, 'r') as file:
        return yaml.safe_load(file)
    

def full_path(dir, filename, type="txt"):
    return os.path.join(dir, f"{filename}.{type}")


def stats_dict_to_dataframe(stats):
    df_stats = pd.DataFrame(stats)
    transposed_data = df_stats.T
    transposed_data.reset_index(inplace=True)
    transposed_data.columns = ['Column'] + list(transposed_data.columns[1:])

    return transposed_data