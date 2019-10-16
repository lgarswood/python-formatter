# python-formatter
A formatter for paragraphs which stretches each line across the full page-width.

## Requirements
This project is compliant with Python3.6+. To install for mac using the **brew** manager, run:
```bash
brew install python3
```

## Run as an application
From the command-line, in the root project directory, run:
```bash
python3 app/format.py --paragraph <quoted-paragraph> --page-width <width>
```
For example, running:
```bash
python3 app/format.py --paragraph "This sentence is not terribly large, and should be parsed fine." --page-width 20
```
Yields the result:
```bash
Array [0] = "This sentence is not"
Array [1] = "terribly large,  and"
Array [2] = "should            be"
Array [3] = "parsed         fine."
```

### Formatting errors:
If your page-width is too big for any given word or a word must be placed alone on a line without taking the full width, it will fail. For example, given the command:
```bash
python3 app/format.py --paragraph "This is a very big sentence on the subject of the disestablishmentarian movement." --page-width 20
```
You will receive the error:
```bash
Error: "disestablishmentarian" longer than width 20.
```

## Run as a python package
Ensure the root project directory is included in your **PYTHON_PATH** and use as:
```python
from typing import List
from app import format_utils

formatted_lines: List[str] = format_utils.split_lines(paragraph, width)
```

Parsing errors in the above example such as those encountered when running from the command-line will raise a **format_utils.FormatException**.

## Running tests
From the root directory, run:
```bash
python3 -m unittest tests/test*.py
```

## Notes
* This does not use any external packages and thus you will find no requirements.txt file and nothing needs to be installed
* It is best to use double-quotes instead of single-quotes from the command-line in case you use contractions in a paragraph
