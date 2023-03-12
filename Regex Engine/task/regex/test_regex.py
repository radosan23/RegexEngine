import unittest
import regex


class TestRegex(unittest.TestCase):
    def test_compare(self):
        self.assertTrue(regex.compare('', ''))
        self.assertTrue(regex.compare('', 'abc'))
        self.assertFalse(regex.compare('a', ''))
        self.assertFalse(regex.compare('a', 'b'))
        self.assertFalse(regex.compare('abc', 'bbc'))
        self.assertFalse(regex.compare('abc', 'aba'))
        self.assertFalse(regex.compare('abc', 'ababa'))
        self.assertTrue(regex.compare('abc', 'abc'))
        self.assertTrue(regex.compare('abc', 'abcbca'))
        self.assertTrue(regex.compare('.', 'c'))
        self.assertTrue(regex.compare('...', 'abc'))
        self.assertTrue(regex.compare('a.c', 'axcb'))
        self.assertFalse(regex.compare('.', ''))
        self.assertFalse(regex.compare('..b', 'bacb'))

    def test_change_pos(self):
        self.assertTrue(regex.change_pos('', ''))
        self.assertTrue(regex.change_pos('', 'abc'))
        self.assertFalse(regex.change_pos('a', ''))
        self.assertTrue(regex.change_pos('abc', 'ababca'))
        self.assertTrue(regex.change_pos('c', 'ababc'))
        self.assertTrue(regex.change_pos('a.c', 'abacca'))
        self.assertFalse(regex.change_pos('cab', 'ababca'))
        self.assertFalse(regex.change_pos('.bb', 'ababca'))

    def test_dollar(self):
        self.assertTrue(regex.change_pos('.c$', 'abc'))
        self.assertTrue(regex.change_pos('abc$', 'abc'))
        self.assertFalse(regex.change_pos('c$', 'acb'))
        self.assertFalse(regex.change_pos('.bc$', 'abcd'))

    def test_caret(self):
        self.assertTrue(regex.check_caret('^a', 'a'))
        self.assertTrue(regex.check_caret('^abc', 'abcde'))
        self.assertTrue(regex.check_caret('abc', 'ababcde'))
        self.assertFalse(regex.check_caret('^a', 'cbab'))
        self.assertFalse(regex.check_caret('^abc', 'bcabc'))
        self.assertFalse(regex.check_caret('ab', 'cba'))

    def test_caret_dollar(self):
        self.assertTrue(regex.check_caret('^abc$', 'abc'))
        self.assertTrue(regex.check_caret('^.bc$', 'bbc'))
        self.assertFalse(regex.check_caret('^abc$', 'aabc'))
        self.assertFalse(regex.check_caret('^abc$', 'abca'))
        self.assertFalse(regex.check_caret('^...$', 'abcd'))

    def test_quantifiers(self):
        data = [('colou?r|color', True), ('colou?r|colour', True), ('colou?r|colouur', False),
                ('colou*r|color', True), ('colou*r|colour', True), ('colou*r|colouur', True),
                ('col.*r|color', True), ('col.*r|colour', True), ('col.*r|colr', True),
                ('col.*r|collar', True), ('col.*r$|colors', False), ('aa?a|aaa', True),
                ('aa?a|aa', True), ('aa*a|aaa', True), ('aa+a|aaa', True), ('aa+a|aa', False),
                ('aa*aaa|aaaa', True), ('aa+aaa|aaaa', False), ('a.+aaa|abcdaaa', True)]
        for item in data:
            self.assertEqual(regex.check_caret(*item[0].split('|')), item[1], item)

    def test_escape(self):
        data = [('\\.$|end.', True), ('3\\+3|3+3=6', True), ('\\?|Is this working?', True),
                ('\\\\|\\', True), ('colou\\?r|color', False), ('colou\\?r|colour', False)]
        for item in data:
            self.assertEqual(regex.check_caret(*item[0].split('|')), item[1], item)


if __name__ == '__main__':
    unittest.main()
