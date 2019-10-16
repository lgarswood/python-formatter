from typing import List


class FormatException(Exception):
    def __init__(self, *args, **kwargs):
        super(__class__, self)
        self.reason: str = args[0]


def line_length(words: List[str]) -> int:
    if not words:
        return 0
    return sum(len(w) + 1 for w in words) - 1


def group_words_by_line(paragraph: str, page_width: int) -> List[List[str]]:
    lines: List[List[str]] = []
    current_words: List[str] = []
    for word in paragraph.split():
        if line_length(current_words) + 1 + len(word) <= page_width:
            current_words.append(word)
        else:
            lines.append(current_words)
            current_words = [word]
    if current_words not in lines:
        lines.append(current_words)
    return lines


def shuffle_lines_to_fit(lines: List[List[str]], page_width: int) -> None:
    rev_lines: List[List[str]] = lines[::-1]
    for i, current_words in enumerate(rev_lines[:-1]):
        if len(current_words) == 1 and len(current_words[0]) < page_width:
            previous_words: List[str] = rev_lines[i + 1]
            if not previous_words:
                continue
            if len(previous_words[-1]) + len(current_words[0]) < page_width:
                current_words.insert(0, previous_words.pop())


def check_successfully_split(line: List[str], page_width: int) -> None:
    if len(line) == 1 and len(line[0]) != page_width:
        raise FormatException(f'"{line[0]}" cannot fit on a line alone.')
    if sum(len(w) for w in line) + len(line) - 1 > page_width:
        raise FormatException(f'Line "{line}" cannot fit in width {page_width}.')


def split_lines(paragraph: str, page_width: int) -> List[str]:
    # Initial placement
    lines: List[List[str]] = group_words_by_line(paragraph, page_width)
    # Shuffle back for lines with one word shorter than the page length
    shuffle_lines_to_fit(lines, page_width)
    # Ensure all lines are non-empty
    lines = [l for l in lines if l]
    # align the words on each line
    return [align_words(l, page_width) for l in lines]


def align_words(words: List[str], width: int) -> str:
    # validate no lines will have leading or trailing whitespace, etc
    check_successfully_split(words, width)

    padding: int = (width - sum(len(w) for w in words)) // (len(words) - 1)
    # Some words require an extra space of padding. Add it to those words
    extra_padded: int = (width - sum(len(w) for w in words)) % (len(words) - 1)
    for i in range(1, extra_padded + 1):
        words[len(words) - i] = f' {words[len(words) - i]}'

    return (' ' * padding).join(words)
