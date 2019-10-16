from argparse import ArgumentParser
import format_utils


def run() -> None:
    parser = ArgumentParser()
    arg_list = [
        ('paragraph', str, 'The entire paragraph to parse'),
        ('page-width', int, 'Number of characters per line')
    ]
    for name, classe, desc in arg_list:
        parser.add_argument(f'--{name}', type=classe, required=True, help=desc)
    args = parser.parse_args()
    try:
        lines = format_utils.split_lines(args.paragraph, args.page_width)
        for index, line in enumerate(lines):
            print(f'Array [{index}] = "{line}"')
    except format_utils.FormatException as e:
        print(f'Error: {e.reason}')


if __name__ == '__main__':
    run()
