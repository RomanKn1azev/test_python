from input import Console
from pipeline import Executor


def main():
    params = Console().get_params()
    Executor(**params).run()


if __name__ == "__main__":
    main()