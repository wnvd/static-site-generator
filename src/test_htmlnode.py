import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        node = HTMLNode("p", "this is a paragraph", None, { "class": "paragraph" }) 
        node2 = HTMLNode("p", "this is a paragraph", None, { "class": "paragraph" }) 
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = HTMLNode("a", "this is a link", None, { "href": "https://www.boot.dev/" }) 
        node2 = HTMLNode("p", "this is a paragraph", None, { "class": "paragraph" }) 
        self.assertNotEqual(node, node2)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "This is a link", { "href": "https://www.boot.dev", "target": "_blank" })
        self.assertEqual(node.to_html(), "<a href=\"https://www.boot.dev\" target=\"_blank\">This is a link</a>")

    def test_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()

    def test_no_tag(self):
        node = LeafNode(None, "this is raw text")
        self.assertEqual(node.to_html(), "this is raw text")

if __name__ == "__main__":
    unittest.main()
