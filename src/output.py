import pandas as pd
import os


from utils import full_path, stats_dict_to_dataframe


class OutputGenerator:
    def __init__(self, stats=None, output_type=None, output_filename="", save_path=""):
        self.__stats = stats
        self.__output_stats = stats_dict_to_dataframe(stats)
        self.__output_type = output_type
        self.__output_filename = output_filename
        self.__save_path = save_path

    @property
    def stats(self):
        return self.__stats

    @property
    def output_type(self):
        return self.__output_type
    
    @property
    def output_filename(self):
        return self.__output_filename
    
    @property
    def save_path(self):
        return self.__save_path
    
    @stats.setter
    def stats(self, new_stats):
        self.__stats = new_stats

    @output_type.setter
    def output_type(self, new_output_type):
        self.__output_type = new_output_type

    @output_filename.setter
    def output_filename(self, new_output_filename):
        self.__output_filename = new_output_filename

    @save_path.setter
    def save_path(self, new_save_path):
        self.__save_path = new_save_path
    
    def generate_output(self):
        self.__path = full_path(
            os.path.join(os.getcwd(), self.__save_path), 
            self.__output_filename,
            self.__output_type
        )
        
        if self.__output_type == 'markdown':
            self._generate_markdown()
        elif self.__output_type == 'html':
            self._generate_html()
        elif self.__output_type == 'xlsx':
            self._generate_xlsx()
        else:
            print(f"Unsupported output type: {self.__output_type}")

    def _generate_markdown(self):
        markdown_table = self.__output_stats.to_markdown(index=False, tablefmt='pipe')

        with open(self.__path, 'w') as file:
            file.write(markdown_table)

    def _generate_html(self):
        self.__output_stats.to_html(self.__path, index=False)

    def _generate_xlsx(self):
        self.__output_stats.to_excel(self.__path, index=False)