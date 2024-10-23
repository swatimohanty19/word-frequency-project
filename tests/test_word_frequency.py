import unittest
from src.word_frequency import count_word_frequencies

class TestWordFrequency(unittest.TestCase):
    
    def test_count_word_frequencies(self):
        line = "which is better python 2 or python 3"
        expected_output = [
            ('2', 1), ('3', 1), ('better', 1), ('is', 1),
            ('or', 1), ('python', 2), ('which', 1)
        ]
        result = count_word_frequencies(line)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()

