import unittest

from generate_hello_html import generate_hello_html


class TestGenerateHelloHTML(unittest.TestCase):
    def test_hello_gihub_actions(self):
        self.assertEqual(generate_hello_html(""), "<span>Hello Github Actions!</span>")

    def test_hello_someone(self):
        self.assertEqual(generate_hello_html("Athibet"), "<span>Hello Athibet!</span>")


if __name__ == "__main__":
    unittest.main()
