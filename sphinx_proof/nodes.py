"""
sphinx_proof.nodes
~~~~~~~~~~~~~~~~~~

Enumerable and unenumerable nodes

:copyright: Copyright 2020 by the QuantEcon team, see AUTHORS
:licences: see LICENSE for details
"""
from sphinx.builders.html import HTMLTranslator
from docutils import nodes
from docutils.nodes import Node
from sphinx.writers.latex import LaTeXTranslator

CR = '\n'

class proof_node(nodes.Admonition, nodes.Element):
    pass


class enumerable_node(nodes.Admonition, nodes.Element):
    pass


class unenumerable_node(nodes.Admonition, nodes.Element):
    pass


def visit_enumerable_node(self, node: Node) -> None:
    if isinstance(self, LaTeXTranslator):
        self.body.append(CR + '\\begin{sphinxadmonition}{note}')
    else:
        self.body.append(self.starttag(node, "div", CLASS="admonition"))


def depart_enumerable_node(self, node: Node) -> None:
    typ = node.attributes.get("type", "")
    if isinstance(self, LaTeXTranslator):
        number = get_node_number_latex(self, node)
        text = node.children[0].astext()
        idx = list_rindex(self.body,CR + '\\begin{sphinxadmonition}{note}') + 2
        self.body.insert(idx, f"{typ.title()} {number}")
        self.body.append('\\end{sphinxadmonition}' + CR)
    else:
        # Find index in list of 'Proof #'
        number = get_node_number(self, node)
        idx = self.body.index(f"Proof {number} ")
        self.body[idx] = f"{typ.title()} {number} "
        self.body.append("</div>")


def visit_unenumerable_node(self, node: Node) -> None:
    if isinstance(self, LaTeXTranslator):
        self.body.append(CR + '\\begin{sphinxadmonition}{note}')
    else:
        self.body.append(self.starttag(node, "div", CLASS="admonition"))


def depart_unenumerable_node(self, node: Node) -> None:
    typ = node.attributes.get("type", "")
    title = node.attributes.get("title", "")
    if isinstance(self, LaTeXTranslator):
        if title == "":
            idx = (len(self.body) - self.body[-1::-1].index(CR + '\\begin{sphinxadmonition}{note}')) + 1
        else:
            text = node.children[0].astext()
            idx = list_rindex(self.body,CR + '\\begin{sphinxadmonition}{note}') + 2
        self.body.insert(idx, f"{typ.title()}")
        self.body.append('\\end{sphinxadmonition}' + CR)
    else:
        if title == "":
            idx = len(self.body) - self.body[-1::-1].index('<p class="admonition-title">')
        else:
            idx = list_rindex(self.body,title)

        element = f"<span>{typ.title()} </span>"
        self.body.insert(idx, element)
        self.body.append("</div>")


def visit_proof_node(self, node: Node) -> None:
    pass


def depart_proof_node(self, node: Node) -> None:
    pass


def get_node_number(self: HTMLTranslator, node: Node) -> str:
    key = "proof"
    ids = node.attributes.get("ids", [])[0]
    number = self.builder.fignumbers.get(key, {}).get(ids, ())
    return ".".join(map(str, number))

def find_parent(env, node , parent_tag):
    """Find the parent node."""
    while True:
        node = node.parent
        if node is None:
            return None
        # parent should be a document in toc
        if (
            "docname" in node.attributes
            and env.titles[node.attributes["docname"]].astext().lower()
            in node.attributes["names"]
        ):
            return node.attributes['docname']

    if node.tagname == parent_tag:
        return node.attributes['docname']

    return None

def get_node_number_latex(self, node: Node) -> str:
    key = "proof"
    docname = find_parent(self.builder.env, node, "section")
    ids = node.attributes.get("ids", [])[0]
    fignumbers = self.builder.env.toc_fignumbers.get(docname, {})
    number = fignumbers.get(key, {}).get(ids, ())
    return ".".join(map(str, number))

def list_rindex(li, x):
    for i in reversed(range(len(li))):
        if li[i] == x:
            return i
    raise ValueError("{} is not in list".format(x))