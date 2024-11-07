from data import RawData
from data_processor import Summary
from output import OutputGenerator


class Executor:
    def __init__(
        self, 
        data_path: str, 
        output_type: str, 
        out_filename: str, 
        save_path: str,
        summary_config_path: str
    ):
        self.__data_path = data_path
        self.__output_type = output_type
        self.__out_filename = out_filename
        self.__save_path = save_path
        self.__summary_config_path = summary_config_path
    
    def run(self):
        raw_data = RawData(self.__data_path)
        
        summary = Summary(raw_data.data, self.__summary_config_path)
        summary.run()
        
        output_generator = OutputGenerator(
            stats=summary.stats,
            output_type=self.__output_type,
            output_filename=self.__out_filename,
            save_path=self.__save_path
        )

        output_generator.generate_output()