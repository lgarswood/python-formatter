from typing import List


def line_length(words: List[str]) -> int:
    if not words:
        return 0
    return sum(len(w) + 1 for w in words) - 1


def split_lines(paragraph: str, page_width: int) -> List[List[str]]:
    lines: List[List[str]] = [[]]
    current_words: List[str] = []
    # Initial placement
    for word in paragraph.split():
        if line_length(current_words) + 1 + len(word) <= page_width:
            current_words.append(word)
        else:
            if len(word) > page_width:
                raise Exception(f'"{word}" longer than page width {page_width}.')
            lines.append(current_words)
            current_words = [word]
    # Shuffle back for lines with one word shorter than the page length
    rev_lines: List[List[str]] = lines[::-1]
    for i, current_words in enumerate(rev_lines):
        if len(current_words) == 1 and len(current_words[0]) != page_width:
            previous_words: List[str] = rev_lines[i + 1]
            if len(previous_words) > 0:
                current_words.insert(0, previous_words.pop())
    # Ensure all lines are non-empty
    lines = [l for l in lines if l]
    # validate no lines will have leading or trailing whitespace
    for line in lines:
        if len(line) == 1 and len(line[0]) != page_width:
            raise Exception(f'"{line[0]}" cannot fit on a line alone.')
    return lines


def align_words(words: List[str]) -> str:
    # TODO: make evenly-spaced
    return ' '.join(words)
