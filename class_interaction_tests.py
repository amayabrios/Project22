import unittest
import branch1_env_pycharm as b1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        m = b1.Movie()
        m.ask_title()
        id_ = m.movie_id
        self.assertEqual(id_, '12444')  # add assertion here


if __name__ == '__main__':
    unittest.main()
