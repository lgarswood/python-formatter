from app import format_utils
from unittest import TestCase, main


class FormatUtilsTest(TestCase):
    # format_utils.line_length()
    def test_line_length_returns_zero_for_empty(self):
        self.assertEqual(format_utils.line_length([]), 0)

    def test_line_length_succeeds_for_two_words(self):
        self.assertEqual(format_utils.line_length(['abc', 'de']), 6)

    # format_utils.group_words_by_line()
    def test_group_words_by_line_produces_expected_line_count(self):
        result = format_utils.group_words_by_line('this is a .', 3)
        self.assertEqual(len(result), 3)

    def test_group_words_by_line_does_not_split_large_word(self):
        result = format_utils.group_words_by_line('hotdog', 5)
        self.assertEqual(result, [['hotdog']])

    # format_utils.shuffle_lines_to_fit()
    def test_shuffle_lines_to_fit_fixes_short_lone_word_for_line(self):
        input = [['this', 'is', 'yet'], ['still', 'a'], ['line']]
        expected = [['this', 'is'], ['yet', 'still'], ['a', 'line']]
        format_utils.shuffle_lines_to_fit(input, 11)
        self.assertEqual(input, expected)

    # format_utils.check_successfully_split()
    def test_check_successfully_split_fails_long_line_one_word(self):
        with self.assertRaises(format_utils.FormatException):
            format_utils.check_successfully_split(['abcdef'], 5)

    def test_check_successfully_split_fails_short_line_one_word(self):
        with self.assertRaises(format_utils.FormatException):
            format_utils.check_successfully_split(['abcd'], 5)

    def test_check_successfully_split_fails_long_line_two_words(self):
        with self.assertRaises(format_utils.FormatException):
            format_utils.check_successfully_split(['abcd', 'e'], 5)

    def test_check_successfully_split_allows_correct_length_one_word(self):
        format_utils.check_successfully_split(['abcdef'], 6)

    def test_check_successfully_split_allows_short_line_two_words(self):
        format_utils.check_successfully_split(['ab', 'e'], 6)

    # format_utils.split_lines()
    def test_split_lines_provides_expected_result_for_correct_input(self):
        input = 'this is yet still a line'
        expected = ['this     is', 'yet   still', 'a      line']
        self.assertEqual(format_utils.split_lines(input, 11), expected)

    def test_split_lines_fails_if_word_cannot_fit(self):
        input = 'and this is obviously still a row'
        with self.assertRaises(format_utils.FormatException):
            format_utils.split_lines(input, 11)

    # format_utils.align_words()
    def test_align_words_adds_extra_padding_when_necessary(self):
        result = format_utils.align_words(['abc', 'd', 'ef'], 9)
        self.assertEqual(result, 'abc d  ef')


if __name__ == '__main__':
    main()
