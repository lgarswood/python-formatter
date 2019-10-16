from argparse import ArgumentParser
import format_utils


def run() -> None:
    parser = ArgumentParser()
    parser.add_argument('--paragraph', type=str, required=True,
        help='The entire paragraph to parse')
    parser.add_argument('--page-width', type=int, required=True,
        help='Number of characters per line')
    args = parser.parse_args()
    try:
        lines = format_utils.format_paragraph(args.paragraph, args.page_width)
        for i, line in enumerate(lines):
            print(f'Array [{i}] = "{line}"')
    except format_utils.FormatException as e:
        print(f'Error: {e.reason}')


if __name__ == '__main__':
    run()
