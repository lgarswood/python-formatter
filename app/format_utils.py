from typing import List


class FormatException(Exception):
    def __init__(self, *args, **kwargs):
        super(__class__, self)
        self.reason: str = args[0]


def line_length(words: List[str]) -> int:
    if not words:
        return 0
    return sum(len(w) + 1 for w in words) - 1


def split_lines(paragraph: str, page_width: int) -> List[List[str]]:
    lines: List[List[str]] = []
    current_words: List[str] = []
    # Initial placement
    for word in paragraph.split():
        if line_length(current_words) + 1 + len(word) <= page_width:
            current_words.append(word)
        else:
            if len(word) > page_width:
                raise FormatException(f'"{word}" is over width {page_width}.')
            lines.append(current_words)
            current_words = [word]
    if current_words not in lines:
        lines.append(current_words)
    # Shuffle back for lines with one word shorter than the page length
    rev_lines: List[List[str]] = lines[::-1]
    for i, current_words in enumerate(rev_lines[:-1]):
        if len(current_words) == 1 and len(current_words[0]) != page_width:
            previous_words: List[str] = rev_lines[i + 1]
            if not previous_words:
                continue
            if len(previous_words[-1]) + len(current_words[0]) < page_width:
                current_words.insert(0, previous_words.pop())
    # Ensure all lines are non-empty
    lines = [l for l in lines if l]
    # validate no lines will have leading or trailing whitespace
    for line in lines:
        if len(line) == 1 and len(line[0]) != page_width:
            raise FormatException(f'"{line[0]}" cannot fit on a line alone.')
    return lines


def align_words(words: List[str], width: int) -> str:
    if sum(len(w) for w in words) + len(words) - 1 > width:
        raise FormatException(f'Line "{words}" cannot fit in width {width}.')
    if len(words) == 1 and len(words[0]) != width:
        raise FormatException(f'"{words[0]}" cannot fit on a line alone.')

    padding: int = (width - sum(len(w) for w in words)) // (len(words) - 1)
    # Some words require an extra space of padding. Add it to those words
    extra_padded: int = (width - sum(len(w) for w in words)) % (len(words) - 1)
    for i in range(1, extra_padded + 1):
        words[len(words) - i] = f' {words[len(words) - i]}'
    return (' ' * padding).join(words)


def format_paragraph(paragraph: str, width: int) -> List[str]:
    return [align_words(l, width) for l in split_lines(paragraph, width)]
