import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        node = HTMLNode("p", "this is a paragraph", None, { "class": "paragraph" }) 
        node2 = HTMLNode("p", "this is a paragraph", None, { "class": "paragraph" }) 
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = HTMLNode("a", "this is a link", None, { "href": "https://www.boot.dev/" }) 
        node2 = HTMLNode("p", "this is a paragraph", None, { "class": "paragraph" }) 
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
