import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.LINK, "https:/www.boot.dev/")
        self.assertNotEqual(node, node2)

    def test_link_eq(self):

        node = TextNode("This is a text node", TextType.LINK, "https:/www.boot.dev/")
        node2 = TextNode("This is a text node", TextType.LINK, "https:/www.boot.dev/")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
