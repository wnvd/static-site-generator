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
