import unittest

from textnode import TextNode, TextType, text_node_to_html_node

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

    def test_image_eq(self):
        node = TextNode("This is alt for image", TextType.IMAGE, "path/to/image")
        node2 = TextNode("This is alt for image", TextType.IMAGE, "path/to/image2")
        self.assertNotEqual(node, node2)

class TestTextToHTML(unittest.TestCase):
    def test_text_to_html(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_text_to_html(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_link_text_to_html(self):
        node = TextNode("this is anchor text", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "this is anchor text")
        self.assertEqual(html_node.props, { "href": "https://www.boot.dev" })

    def test_img_text_to_html(self):
        node = TextNode("sunshine", TextType.IMAGE, "/img/sunshine.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, { "src": "/img/sunshine.png", "alt": "sunshine" })


if __name__ == "__main__":
    unittest.main()
