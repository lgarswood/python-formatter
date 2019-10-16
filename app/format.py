from argparse import ArgumentParser
from format_utils import split_lines


def run() -> None:
    parser = ArgumentParser()
    parser.add_argument('--paragraph', type=str, required=True,
        help='The entire paragraph to parse')
    parser.add_argument('--page-width', type=int, required=True,
        help='Number of characters per line')
    args = parser.parse_args()
    print(split_lines(**args.__dict__))


if __name__ == '__main__':
    run()
