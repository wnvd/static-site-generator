import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        node_one = LeafNode("span", "this is a span", { "class": "color-red-100" })
        node_two = LeafNode("p", "this is a paragraph", { "class": "color-slate-300" })
        parent_node = ParentNode("div", [node_one, node_two])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span class=\"color-red-100\">this is a span</span><p class=\"color-slate-300\">this is a paragraph</p></div>"
        )

if __name__ == "__main__":
    unittest.main()
