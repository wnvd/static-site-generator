class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This method has not been implemented yet")

    def props_to_html(self):
        if self.props is None:
            return ""

        html_string = ""
        for pKey, pValue in self.props.items():
            html_string += f"{pKey}=\"{pValue}\" "
        return html_string.rstrip()

    def __eq__(self, node):
        return self.tag == node.tag and self.value == node.value and self.children == node.children and self.props == node.props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.tag == "img" and self.value is None:
            raise ValueError("All leaf node must have a value")
        if self.tag is None:
            return f"{self.value}"
        props_string = super().props_to_html()
        if props_string == "":
            return f"<{self.tag}>{self.value}</{self.tag}>"
        # img tag has value as empty string ("")
        # we are not going to use it here.
        if self.tag == "img":
            return f"<{self.tag} {props_string} />"
        return f"<{self.tag} {props_string}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("The object needs to tag")
        if len(self.children) == 0:
            raise ValueError("The parent node needs children")
        props_string = super().props_to_html()
        if props_string == "":
            return f"<{self.tag}>{self.children_to_string(self.children)}</{self.tag}>"
        return f"<{self.tag} {props_string}>{self.children_to_string(self.children)}</{self.tag}>"

    def children_to_string(self, children):
        if len(children) == 0:
            return ""
        return children[0].to_html() + self.children_to_string(children[1:])
