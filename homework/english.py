"""
  Дано предложение. Необходимо проверить правильность артиклей a/an.
  Правило: перед гласной буквой и перед u,y ставим a, перед согласной - an.
  Не проверяем(!!!): нечитаемые согласные в начале слова, например, honor, и другие исключения в англ языке
  Правило очень простое:
  перед qwrtzuypsdfghjklmnbvcx ставим a, во всех остальных случаях an.
  Артикль a/an не должен быть в конце предложения.
  Предложение всегда заканчивается точкой.
  Примеры смотрите в тестах.
"""
import unittest

def correct_sentense(sentence):
    #  Incorrect solution!!!
    correct = True
    words = sentence.split()
    for i in range(len(words)):
        if words[i] == "an" and words[i+1][0] in "qwrtzuypsdfghjklmnbvcx":
            correct = False
    return correct


class TestEnglish(unittest.TestCase):
    def test_simple_correct(self):
        self.assertEqual(correct_sentense("This is a book."), True)

    def test_simple_incorrect(self):
        self.assertEqual(correct_sentense("This is an book."), False)

    def test_no_article(self):
        self.assertEqual(correct_sentense("This is book."), True)

    def test_no_article_in_the_end(self):
        self.assertEqual(correct_sentense("This is book a."), False)

    def test_double_article(self):
        self.assertEqual(correct_sentense("This is a a book"), False)

    def test_double_article_a_an(self):
        self.assertEqual(correct_sentense("This is an a book"), False)

    def test_article_at_the_beginning(self):
        self.assertEqual(correct_sentense("A book is interesting."), True)

    def test_upper_case(self):
        self.assertEqual(correct_sentense("A University is important"), True)

    def test_article_at_the_beginning_upper(self):
        self.assertEqual(correct_sentense("An book is interesting."), False)

    def test_two_articles(self):
        self.assertEqual(correct_sentense("A mouse with bluetooth is better than a mouse without bluetooth"), True)

    def test_two_articles_incorrect(self):
        self.assertEqual(correct_sentense("A mouse with bluetooth is better than an mouse without bluetooth"), False)


if __name__ == '__main__':
    unittest.main()
