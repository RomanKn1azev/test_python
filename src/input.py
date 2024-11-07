from argparse import ArgumentParser


class Console:
    def __init__(self):
        self.parser = ArgumentParser(
            description='Processing console arguments'
        )
        self._add_arguments()
    
    def _add_arguments(self):
        self.parser.add_argument(
            '-d',
            '--data',
            type=str,
            required=True,
            help='Path to data file. For example: *.csv'
        )

        self.parser.add_argument(
            '-t',
            '--type',
            type=str,
            required=True,
            choices=['markdown', 'html', 'xlsx'],
            help='Ouput type for saving'
        )

        self.parser.add_argument(
            '-f',
            '--filename',
            type=str,
            required=True,
            help='Out filename'
        )

        self.parser.add_argument(
            '-s',
            '--save',
            type=str,
            default='save',
            help='Path to save. By default, the path to the directory is \'save\''
        )

        self.parser.add_argument(
            '-c',
            '--config',
            type=str,
            default='config/summary.yaml',
            help='Yaml file with statistics items'
        )

    def parse_arguments(self):
        return self.parser.parse_args()
    
    def get_params(self):
        args = self.parse_arguments()

        return {
            "data_path": args.data,
            "output_type": args.type,
            "out_filename": args.filename,
            "save_path": args.save,
            "summary_config_path": args.config
        }