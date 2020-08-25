"""
sphinxcontrib.prettyproof.nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enumerable and unenumerable nodes

:copyright: Copyright 2020 by the QuantEcon team, see AUTHORS
:licences: see LICENSE for details
"""
from sphinx.builders.html import HTMLTranslator
from docutils import nodes
from docutils.nodes import Node


class proof_node(nodes.Admonition, nodes.Element):
    pass


class enumerable_node(nodes.Admonition, nodes.Element):
    pass


class unenumerable_node(nodes.Admonition, nodes.Element):
    pass


def visit_enumerable_node(self, node: Node) -> None:
    self.body.append(self.starttag(node, "div", CLASS="admonition"))


def depart_enumerable_node(self, node: Node) -> None:
    typ = node.attributes.get("type", "")

    # Find index in list of 'Proof #'
    number = get_node_number(self, node)
    idx = self.body.index(f"Proof {number} ")
    self.body[idx] = f"{typ.title()} {number} "
    self.body.append("</div>")


def visit_unenumerable_node(self, node: Node) -> None:
    self.body.append(self.starttag(node, "div", CLASS="admonition"))


def depart_unenumerable_node(self, node: Node) -> None:
    typ = node.attributes.get("type", "")
    title = node.attributes.get("title", "")
    _id = node.attributes.get("ids", [])[0]

    if title == "":
        idx = len(self.body) - self.body[-1::-1].index('<p class="admonition-title">')
    else:
        idx = self.body.index(title)

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
